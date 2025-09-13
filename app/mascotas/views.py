import json
import logging
from typing import List

from django.core.paginator import Paginator
from django.db.models import Avg, Count, QuerySet, Sum
from django.shortcuts import render
from esterilizaya.constantes import CANTONES, ESPECIE, PARROQUIAS, SEXO
from registro.models import Registro

logger = logging.getLogger(__name__)


def devolver_tupla_codigo_territorio(lista_codigo_territorio: list, lista_valores_tupla: List):
    valor_dict = dict(lista_valores_tupla)
    return [(codigo, valor_dict.get(codigo, codigo)) for codigo in lista_codigo_territorio]


def contar_datos_por_key(lista_registros: QuerySet, key: str):
    return lista_registros.values(key).order_by(key).annotate(total=Count(key))


def index(request):
    lista_registros = Registro.objects.all().order_by("id")
    campana_actual = request.GET.get("campana", "")
    especie_actual = request.GET.get("especie", "")
    genero_actual = request.GET.get("genero", "")
    nombre_actual = request.GET.get("nombre", "")
    canton_actual = request.GET.get("canton", "")
    parroquia_actual = request.GET.get("parroquia", "")
    barrio_actual = request.GET.get("barrio", "")
    page_number = request.GET.get("page", 1)
    campanas = (
        lista_registros.order_by("inscripcion__campana")
        .distinct()
        .values_list("inscripcion__campana", "inscripcion__campana__nombre")
    )
    # Comparar solo strings en los selectores
    campanas = [(str(id), nombre) for id, nombre in campanas]
    if nombre_actual:
        if nombre_actual.isnumeric():
            lista_registros = lista_registros.filter(id__startswith=nombre_actual)
        else:
            lista_registros = lista_registros.filter(nombre__iregex=nombre_actual)
    if campana_actual:
        lista_registros = lista_registros.filter(inscripcion__campana=campana_actual)
    especies_codigos = lista_registros.order_by("especie").distinct().values_list("especie", flat=True)
    especies = devolver_tupla_codigo_territorio(especies_codigos, ESPECIE)
    if especie_actual:
        lista_registros = lista_registros.filter(especie=especie_actual)
    genero_codigos = lista_registros.order_by("sexo").distinct().values_list("sexo", flat=True)
    generos = devolver_tupla_codigo_territorio(genero_codigos, SEXO)
    if genero_actual:
        lista_registros = lista_registros.filter(sexo=genero_actual)
    cantones_codigos = lista_registros.order_by("canton_tutor").distinct().values_list("canton_tutor", flat=True)
    cantones = devolver_tupla_codigo_territorio(cantones_codigos, CANTONES)
    if canton_actual:
        lista_registros = lista_registros.filter(canton_tutor=canton_actual)
    parroquias_codigos = (
        lista_registros.order_by("parroquia_tutor").distinct().values_list("parroquia_tutor", flat=True)
    )
    parroquias = devolver_tupla_codigo_territorio(parroquias_codigos, PARROQUIAS)
    if parroquia_actual:
        lista_registros = lista_registros.filter(parroquia_tutor=parroquia_actual)
    barrios_codigos = lista_registros.order_by("barrio_tutor").distinct().values_list("barrio_tutor", flat=True)
    barrios = [(cod, cod) for cod in barrios_codigos]
    if barrio_actual:
        lista_registros = lista_registros.filter(barrio_tutor=barrio_actual)
    # Estadísticas
    mascotas_locaciones = (
        lista_registros.values_list("canton_tutor", "parroquia_tutor", "barrio_tutor")
        .annotate(count=Count("barrio_tutor"))
        .order_by("barrio_tutor")
    )
    estadisticas_genero = contar_datos_por_key(lista_registros, "sexo")
    estadisticas_especie = contar_datos_por_key(lista_registros, "especie")
    estadisticas_raza = contar_datos_por_key(lista_registros, "raza_mascota")
    estadisticas_parroquia = contar_datos_por_key(lista_registros, "parroquia_tutor")
    estadisticas_barrio = contar_datos_por_key(lista_registros, "barrio_tutor")
    queryset_limpio = lista_registros.exclude(n_animales_hogar__lte=0)
    datos_mascotas_hogar = {
        "hogar": queryset_limpio.aggregate(total_value=Sum("n_animales_hogar"))["total_value"],
        "hogar_esterilizadas": queryset_limpio.aggregate(total_value=Sum("n_animales_hogar_esterilizadas"))[
            "total_value"
        ],
        "promedio_hogar": round(queryset_limpio.aggregate(Avg("n_animales_hogar"))["n_animales_hogar__avg"], 2),
    }
    datos_mascotas_hogar["porcentaje_esterilizacion"] = round(
        100 * datos_mascotas_hogar["hogar_esterilizadas"] / datos_mascotas_hogar["hogar"], 2
    )
    # Paginación
    paginator = Paginator(lista_registros, 25)
    registros = paginator.page(page_number)
    # Mantener la URL sin el número de página
    query_dict = request.GET.copy()
    if "page" in query_dict:
        query_dict.pop("page")
    query_string = query_dict.urlencode()
    context = {
        "registros": registros,
        "campanas": campanas,
        "cantones": cantones,
        "parroquias": parroquias,
        "barrios": barrios,
        "especies": especies,
        "generos": generos,
        "nombre_actual": nombre_actual,
        "campana_actual": campana_actual,
        "especie_actual": especie_actual,
        "genero_actual": genero_actual,
        "canton_actual": canton_actual,
        "parroquia_actual": parroquia_actual,
        "barrio_actual": barrio_actual,
        "query_string": query_string,
        "mascotas_ubicacion": json.dumps(list(mascotas_locaciones)),
        "estadisticas_genero": list(estadisticas_genero),
        "estadisticas_especie": list(estadisticas_especie),
        "estadisticas_raza": list(estadisticas_raza),
        "estadisticas_parroquia": list(estadisticas_parroquia),
        "estadisticas_barrio": list(estadisticas_barrio),
        "datos_mascotas_hogar": datos_mascotas_hogar,
    }
    return render(
        request,
        "index.html",
        context,
    )
