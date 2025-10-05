import json
import logging
from typing import List

from django.core.paginator import Paginator
from django.db.models import Avg, Count, QuerySet, Sum
from django.shortcuts import render
from esterilizaya.constantes import CANTONES, ESPECIE, PARROQUIAS, SEXO
from registro.models import Registro

logger = logging.getLogger(__name__)


def devolver_tupla_codigo_territorio(codigos: list, tuplas: List):
    """Devuelve una lista de tuplas (codigo, display) usando un diccionario de tuplas."""
    valor_dict = dict(tuplas)
    return [(codigo, valor_dict.get(codigo, codigo)) for codigo in codigos]


def contar_datos_por_key(queryset: QuerySet, key: str):
    """Cuenta y agrupa por el campo key."""
    return queryset.values(key).order_by(key).annotate(total=Count(key))


def obtener_valores_selector(queryset: QuerySet, key: str):
    """Obtiene los valores únicos de un campo."""
    return queryset.order_by(key).distinct().values_list(key, flat=True)


def index(request):
    lista_registros = Registro.objects.all().order_by("id")
    filtros = {
        "campana": request.GET.get("campana", ""),
        "especie": request.GET.get("especie", ""),
        "genero": request.GET.get("genero", ""),
        "raza": request.GET.get("raza", ""),
        "nombre": request.GET.get("nombre", ""),
        "canton": request.GET.get("canton", ""),
        "parroquia": request.GET.get("parroquia", ""),
        "barrio": request.GET.get("barrio", ""),
        "origen": request.GET.get("origen", ""),
    }
    page_number = request.GET.get("page", 1)

    # Campañas
    campanas = (
        lista_registros.order_by("inscripcion__campana")
        .distinct()
        .values_list("inscripcion__campana", "inscripcion__campana__nombre")
    )
    campanas = [(str(id), nombre) for id, nombre in campanas]

    # Filtros dinámicos
    if filtros["nombre"]:
        if filtros["nombre"].isnumeric():
            lista_registros = lista_registros.filter(id__startswith=filtros["nombre"])
        else:
            lista_registros = lista_registros.filter(nombre__iregex=filtros["nombre"])
    if filtros["campana"]:
        lista_registros = lista_registros.filter(inscripcion__campana=filtros["campana"])

    especies_codigos = obtener_valores_selector(lista_registros, "especie")
    especies = devolver_tupla_codigo_territorio(especies_codigos, ESPECIE)
    if filtros["especie"]:
        lista_registros = lista_registros.filter(especie=filtros["especie"])

    genero_codigos = obtener_valores_selector(lista_registros, "sexo")
    generos = devolver_tupla_codigo_territorio(genero_codigos, SEXO)
    if filtros["genero"]:
        lista_registros = lista_registros.filter(sexo=filtros["genero"])

    raza_codigos = obtener_valores_selector(lista_registros, "raza_mascota")
    razas = [(cod, cod) for cod in raza_codigos]
    if filtros["raza"]:
        lista_registros = lista_registros.filter(raza_mascota=filtros["raza"])

    cantones_codigos = obtener_valores_selector(lista_registros, "canton_tutor")
    cantones = devolver_tupla_codigo_territorio(cantones_codigos, CANTONES)
    if filtros["canton"]:
        lista_registros = lista_registros.filter(canton_tutor=filtros["canton"])

    parroquias_codigos = obtener_valores_selector(lista_registros, "parroquia_tutor")
    parroquias = devolver_tupla_codigo_territorio(parroquias_codigos, PARROQUIAS)
    if filtros["parroquia"]:
        lista_registros = lista_registros.filter(parroquia_tutor=filtros["parroquia"])

    barrios_codigos = obtener_valores_selector(lista_registros, "barrio_tutor")
    barrios = [(cod, cod) for cod in barrios_codigos]
    if filtros["barrio"]:
        lista_registros = lista_registros.filter(barrio_tutor=filtros["barrio"])
    origen = [("0", "Doméstico"), ("1", "Vulnerable")]
    if filtros["origen"]:
        lista_registros = lista_registros.filter(vulnerable=filtros["origen"])

    # Estadísticas
    mascotas_locaciones = (
        lista_registros.values_list("canton_tutor", "parroquia_tutor", "barrio_tutor")
        .annotate(count=Count("barrio_tutor"))
        .order_by("barrio_tutor")
    )
    estadisticas_genero = list(contar_datos_por_key(lista_registros, "sexo"))
    estadisticas_especie = list(contar_datos_por_key(lista_registros, "especie"))
    estadisticas_raza = list(contar_datos_por_key(lista_registros, "raza_mascota"))
    estadisticas_parroquia = list(contar_datos_por_key(lista_registros, "parroquia_tutor"))
    estadisticas_barrio = list(contar_datos_por_key(lista_registros, "barrio_tutor"))

    # Estadísticas de hogar
    queryset_limpio = lista_registros.exclude(n_animales_hogar__lte=0).order_by("inscripcion__id").distinct()
    n_hogar = queryset_limpio.aggregate(total=Sum("n_animales_hogar"))["total"] or 0
    n_hogar_esterilizadas = queryset_limpio.aggregate(total=Sum("n_animales_hogar_esterilizadas"))["total"] or 0
    promedio_hogar = round(queryset_limpio.aggregate(avg=Avg("n_animales_hogar"))["avg"] or 0, 2)
    n_muestras = queryset_limpio.count()
    porcentaje_esterilizacion = round(100 * n_hogar_esterilizadas / n_hogar, 2) if n_hogar else 0

    datos_mascotas_hogar = {
        "hogar": n_hogar,
        "hogar_esterilizadas": n_hogar_esterilizadas,
        "promedio_hogar": promedio_hogar,
        "n_muestras": n_muestras,
        "porcentaje_esterilizacion": porcentaje_esterilizacion,
    }

    # Paginación
    paginator = Paginator(lista_registros, 25)
    registros = paginator.get_page(page_number)

    # Mantener la URL sin el número de página
    query_dict = request.GET.copy()
    query_dict.pop("page", None)
    query_string = query_dict.urlencode()

    context = {
        "registros": registros,
        "campanas": campanas,
        "cantones": cantones,
        "parroquias": parroquias,
        "barrios": barrios,
        "especies": especies,
        "generos": generos,
        "razas": razas,
        "origen": origen,
        "nombre_actual": filtros["nombre"],
        "campana_actual": filtros["campana"],
        "especie_actual": filtros["especie"],
        "genero_actual": filtros["genero"],
        "raza_actual": filtros["raza"],
        "canton_actual": filtros["canton"],
        "parroquia_actual": filtros["parroquia"],
        "barrio_actual": filtros["barrio"],
        "origen_actual": filtros["origen"],
        "query_string": query_string,
        "mascotas_ubicacion": json.dumps(list(mascotas_locaciones)),
        "estadisticas_genero": estadisticas_genero,
        "estadisticas_especie": estadisticas_especie,
        "estadisticas_raza": estadisticas_raza,
        "estadisticas_parroquia": estadisticas_parroquia,
        "estadisticas_barrio": estadisticas_barrio,
        "datos_mascotas_hogar": datos_mascotas_hogar,
    }
    return render(request, "index.html", context)
