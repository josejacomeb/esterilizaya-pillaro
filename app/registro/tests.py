from django.test import TestCase
from django.contrib.auth import get_user_model
from inscripcion.models import Inscripcion
from campana.models import Campana
from registro.models import Registro
from esterilizaya.constantes import COLORES, ESPECIE, SEXO, AFIRMATIVO_NEGATIVO, PARROQUIAS, RAZON_TENENCIA, N_MASCOTAS, EDADES_ANOS, EDADES_MESES

class RegistroModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username="testuser")
        self.campana = Campana.objects.create(nombre="Campaña Test", barrio="Centro", parroquia="Pillaro", fecha="2025-08-07")
        self.inscripcion = Inscripcion.objects.create(
            campana=self.campana,
            nombres_tutor="Juan Perez",
            cupos_totales=5,
            cupos_registrados=0,
            barrio_tutor="Centro",
            parroquia_tutor=PARROQUIAS[0][0],
            numero_telefono_tutor=1234567890,
            cedula_identidad=1234567890,
            razon_tenencia=RAZON_TENENCIA[0][0],
            usuario=self.user,
        )

    def test_create_registro(self):
        registro = Registro.objects.create(
            inscripcion=self.inscripcion,
            peso=12.5,
            numero_turno=1,
            nombre="Firulais",
            color_principal=COLORES[0][0],
            color_secundario=COLORES[1][0],
            observaciones="Sin observaciones",
            especie=ESPECIE[0][0],
            sexo=SEXO[0][0],
            edad_anos=EDADES_ANOS[0][0],
            edad_meses=EDADES_MESES[0][0],
            raza_mascota="Mestizo",
            carnet=AFIRMATIVO_NEGATIVO[0][0],
            vulnerable=False,
            nombres_tutor="Juan Perez",
            numero_telefono_tutor=1234567890,
            cedula_identidad=1234567890,
            razon_tenencia=RAZON_TENENCIA[0][0],
            parroquia_tutor=PARROQUIAS[0][0],
            barrio_tutor="Centro",
            n_animales_hogar=N_MASCOTAS[0][0],
            n_animales_hogar_esterilizadas=N_MASCOTAS[0][0],
            usuario=self.user,
        )
        self.assertEqual(str(registro), "Firulais de Juan Perez")
        self.assertEqual(registro.inscripcion, self.inscripcion)
        self.assertEqual(registro.usuario, self.user)
        self.assertEqual(registro.peso, 12.5)
        self.assertEqual(registro.numero_turno, 1)
        self.assertEqual(registro.nombre, "Firulais")

class RegistroViewsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpass")
        self.campana = Campana.objects.create(nombre="Campaña Test", barrio="Centro", parroquia="Pillaro", fecha="2025-08-07")
        self.inscripcion = Inscripcion.objects.create(
            campana=self.campana,
            nombres_tutor="Juan Perez",
            cupos_totales=5,
            cupos_registrados=0,
            barrio_tutor="Centro",
            parroquia_tutor=PARROQUIAS[0][0],
            numero_telefono_tutor=1234567890,
            cedula_identidad=1234567890,
            razon_tenencia=RAZON_TENENCIA[0][0],
            usuario=self.user,
        )
        self.registro = Registro.objects.create(
            inscripcion=self.inscripcion,
            peso=12.5,
            numero_turno=1,
            nombre="Firulais",
            color_principal=COLORES[0][0],
            color_secundario=COLORES[1][0],
            observaciones="Sin observaciones",
            especie=ESPECIE[0][0],
            sexo=SEXO[0][0],
            edad_anos=EDADES_ANOS[0][0],
            edad_meses=EDADES_MESES[0][0],
            raza_mascota="Mestizo",
            carnet=AFIRMATIVO_NEGATIVO[0][0],
            vulnerable=False,
            nombres_tutor="Juan Perez",
            numero_telefono_tutor=1234567890,
            cedula_identidad=1234567890,
            razon_tenencia=RAZON_TENENCIA[0][0],
            parroquia_tutor=PARROQUIAS[0][0],
            barrio_tutor="Centro",
            n_animales_hogar=N_MASCOTAS[0][0],
            n_animales_hogar_esterilizadas=N_MASCOTAS[0][0],
            usuario=self.user,
        )

    def test_lista_view(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(f"/registro/lista/{self.campana.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Firulais")

    def test_ver_ficha_view(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(f"/registro/{self.campana.id}/ficha/{self.registro.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Firulais")

    def test_registrar_view_no_cupos(self):
        self.inscripcion.cupos_registrados = self.inscripcion.cupos_totales
        self.inscripcion.save()
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(f"/registro/{self.campana.id}/registrar/{self.inscripcion.id}/", {})
        self.assertEqual(response.status_code, 302)  # Redirect due to no cupos

    def test_registrar_view_get(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(f"/registro/{self.campana.id}/registrar/{self.inscripcion.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Registrar")

    def test_generar_pdf_view(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(f"/registro/generar_pdf/{self.registro.id}/")
        self.assertIn(response.status_code, [200, 302])  # Puede redirigir tras generar
