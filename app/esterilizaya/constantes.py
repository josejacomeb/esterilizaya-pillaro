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
MAX_LONG_PARROQUIAS = 40

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


PARROQUIAS = {
    "PI": [
        # Rurales
        "Baquerizo Moreno",
        "Emilio Maria Terán",
        "Marcos Espinel",
        "Presidente Urbina",
        "San Andrés",
        "San José de Poaló",
        "San Miguelito",
        # Urbanas
        "La Matriz",
        "Ciudad Nueva",
    ],
    "AM": [
        # Rurales
        "Ambatillo",
        "Atahualpa",
        "Augusto Nicolás Martínez",
        "Constantino Fernández",
        "Cunchibamba",
        "Huachi Grande",
        "Izamba",
        "Juan Benigno Vela",
        "Montalvo",
        "Pasa",
        "Picaihua",
        "Pilahuín",
        "Quisapincha",
        "San Bartolomé de Pinllo",
        "San Fernando",
        "Santa Rosa",
        "Totoras",
        "Unamuncho",
        # Urbanas
        "Ambato",
    ],
    "PE": [
        # Rurales
        "Benítez",
        "Bolívar",
        "Cotaló",
        "Chiquicha",
        "El Rosario",
        "García Moreno",
        "Huambaló",
        "Salasaca",
        # Urbanas
        "Pelileo",
    ],
    "PA": [
        # Rurales
        "El Triunfo",
        "Los Andes",
        "Sucre",
        # Urbanas
        "Patate",
    ],
    "SA": [
        # Rurales
        "Antonio José Holguín",
        "Cusubamba",
        "Mulalillo",
        "Mulliquindil",
        "Panzaleo",
        # Urbanas
        "San Miguel",
    ],
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
