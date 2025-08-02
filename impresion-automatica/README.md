# Impresion Automática de fichas de esterilizaya

## Instalación

*Nota:* Estas instrucciones están pensadas a correrlas en la carpeta por defecto de esterilizaya

1. Por favor,  crea un nuevo `venv` en Python con el siguiente commando: `python -m venv .venv`
2. Activa ese nuevo ambiente con `source .venv/bin/activate`
3. Instale los requisitos de software con `pip install -r impresion-automatica/requirements.txt`

## Uso

Monitoriza el directorio donde `esterilizaya` guarda las fichas registradas, con el siguiente comando: `python3 impresion-automatica/__main__.py -d=pdfs/`
Mayor información sobre los comandos:

```bash
usage: __main__.py [-h] --directorio DIRECTORIO [--procesados PROCESADOS] [--impresora IMPRESORA]

Herramienta sencilla para inspeccionar un directorio por nuevos PDFs para imprimirlos automáticamente.

options:
  -h, --help            show this help message and exit
  --directorio DIRECTORIO, -d DIRECTORIO
                        Directorio para buscar por PDFs para imprimir
  --procesados PROCESADOS, -p PROCESADOS
                        Nombre directorio donde
  --impresora IMPRESORA, -i IMPRESORA
                        Nombre de la impresora a usar
```
