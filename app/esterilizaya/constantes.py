import pathlib

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


PARROQUIAS = [
    # Rurales
    ("BM", "Baquerizo Moreno"),
    ("EMT", "Emilio Maria Terán"),
    ("ME", "Marcos Espinel"),
    ("PU", "Presidente Urbina"),
    ("SA", "San Andrés"),
    ("SJP", "San José de Poaló"),
    ("SM", "San Miguelito"),
    # Urbanas
    ("LM", "La Matriz"),
    ("CN", "Ciudad Nueva"),
]

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
