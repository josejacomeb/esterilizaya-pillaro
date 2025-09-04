import pathlib

from django import forms


class SelectInput(forms.Select):
    input_type = "select"


ESPECIE = [("🐕", "Canino"), ("🐈", "Felino")]
SEXO = [("♂️", "Macho"), ("♀️", "Hembra")]
AFIRMATIVO_NEGATIVO = [("S", "Si"), ("N", "No")]

HORARIOS = [
    ("07", "07:00"),
    ("11", "11:00"),
]

EDADES_MESES = [(i, str(i)) for i in range(12)]
EDADES_ANOS = [(i, str(i)) for i in range(20)]
N_MASCOTAS = [(i, str(i)) for i in range(25)]
MAX_CUPOS = [(i, str(i)) for i in range(1, 5)]
# Máxima longitud de caracteres para la BD
MAX_LONG_CANTONES = 5
MAX_LONG_BARRIOS = 75
MAX_LONG_PARROQUIAS = 5

# Según https://simple.wikipedia.org/wiki/Dog_coat
# y https://www.catster.com/lifestyle/different-cat-colors/
COLORES = [
    ("AL", "Albaricoque"),
    ("AM", "Amarillo"),
    ("AZ", "Azul"),
    ("BE", "Beige"),
    ("BL", "Blanco"),
    ("CF", "Café"),
    ("CN", "Canela"),
    ("CR", "Crema"),
    ("DO", "Dorado"),
    ("GR", "Gris"),
    ("NA", "Naranja"),
    ("NE", "Negro"),
    ("RO", "Rojo"),
    ("TR", "Tricolor"),
]

# Cantones cercanos a las campañas de esterilización
CANTONES = [("PI", "Píllaro"), ("AM", "Ambato"), ("PE", "Pelileo"), ("PA", "Patate"), ("SA", "Salcedo")]

PARROQUIAS = [
    # Píllaro Rurales
    ("BM", "Baquerizo Moreno"),
    ("EMT", "Emilio Maria Terán"),
    ("ME", "Marcos Espinel"),
    ("PU", "Presidente Urbina"),
    ("SA", "San Andrés"),
    ("SJP", "San José de Poaló"),
    ("SM", "San Miguelito"),
    # Píllaro Urbanas
    ("LM", "La Matriz"),
    ("CN", "Ciudad Nueva"),
    # Ambato Rurales
    ("amb", "Ambatillo"),
    ("AT", "Atahualpa"),
    ("ANM", "Augusto Nicolás Martínez"),
    ("CF", "Constantino Fernández"),
    ("CUN", "Cunchibamba"),
    ("HG", "Huachi Grande"),
    ("IZA", "Izamba"),
    ("JBV", "Juan Benigno Vela"),
    ("MON", "Montalvo"),
    ("PAS", "Pasa"),
    ("PIC", "Picaihua"),
    ("PIL", "Pilahuín"),
    ("QUI", "Quisapincha"),
    ("SBP", "San Bartolomé de Pinllo"),
    ("SF", "San Fernando"),
    ("SR", "Santa Rosa"),
    ("TOT", "Totoras"),
    ("UNA", "Unamuncho"),
    # Ambato Urbanas
    ("AMB", "Ambato"),
    # Pelileo Rurales
    ("BEN", "Benítez"),
    ("BOL", "Bolívar"),
    ("COT", "Cotaló"),
    ("CHI", "Chiquicha"),
    ("ER", "El Rosario"),
    ("GM", "García Moreno"),
    ("HUA", "Huambaló"),
    ("SAL", "Salasaca"),
    # Pelileo Urbanas
    ("PEL", "Pelileo"),
    # Patate Rurales
    ("ET", "El Triunfo"),
    ("LA", "Los Andes"),
    ("SUC", "Sucre"),
    # Patate Urbanas
    ("PAT", "Patate"),
    # Salcedo Rurales
    ("AJH", "Antonio José Holguín"),
    ("CUS", "Cusubamba"),
    ("MUO", "Mulalillo"),
    ("MUL", "Mulliquindil"),
    ("PAN", "Panzaleo"),
    # Salcedo Urbanas
    ("SMl", "San Miguel"),
]

PARROQUIAS_CANTON = {
    "PI": PARROQUIAS[:9],
    "AM": PARROQUIAS[9:28],
    "PE": PARROQUIAS[28:37],
    "PA": PARROQUIAS[37:41],
    "SA": PARROQUIAS[41:],
}

RAZON_TENENCIA = [
    ("CO", "Compañia"),
    ("GU", "Guardián"),
    ("RE", "Reproductiva"),
    ("DE", "Deporte"),
    ("CA", "Caza"),
    ("SE", "Servicio"),
    ("MI", "Mixta"),
]

RUTA_PDFS = pathlib.Path("/tmp/pdfs")
