import argparse
import logging
import pathlib
import shutil
import subprocess

from watchfiles import Change, watch

# Configuración del logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", handlers=[logging.StreamHandler()]
)


def obtener_impresoras():
    try:
        resultado = subprocess.run(["lpstat", "-p"], capture_output=True, text=True, check=True)
        impresoras = [line.split()[1] for line in resultado.stdout.splitlines() if line.startswith("printer")]
        return impresoras
    except Exception as e:
        logging.error(f"Error al consultar impresoras: {e}")
        return []


def build_parser():
    descripcion_str = (
        "Herramienta sencilla para inspeccionar un directorio por nuevos PDFs para imprimirlos automáticamente."
    )
    parser = argparse.ArgumentParser(description=descripcion_str)
    parser.add_argument(
        "--directorio", "-d", type=pathlib.Path, help="Directorio para buscar por PDFs para imprimir", required=True
    )
    parser.add_argument("--procesados", "-p", type=str, help="Nombre directorio donde ", default="procesados")
    parser.add_argument("--impresora", "-i", type=str, help="Nombre de la impresora a usar")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    ruta_directorio = args.directorio
    ruta_procesados = ruta_directorio / args.procesados

    impresoras = obtener_impresoras()
    if not impresoras:
        logging.error("No se detectó ninguna impresora disponible en el sistema.")
        return

    impresora_seleccionada = args.impresora
    if impresora_seleccionada and impresora_seleccionada not in impresoras:
        logging.warning(
            f"La impresora '{impresora_seleccionada}' no está disponible. Se usará '{impresoras[0]}' en su lugar."
        )
        impresora_seleccionada = impresoras[0]
    elif not impresora_seleccionada:
        impresora_seleccionada = impresoras[0]
        logging.info(f"No se especificó impresora. Usando la primera disponible: '{impresora_seleccionada}'.")

    if ruta_directorio is None or not ruta_directorio.exists():
        logging.error("Por favor, proporciona la carpeta válida a observar.")
        return

    if not ruta_procesados.exists():
        logging.info(f"Creando directorio de procesados: {ruta_procesados}")
        ruta_procesados.mkdir(parents=True, exist_ok=True)

    logging.info(f"Observando el directorio: {ruta_directorio}")

    for changes in watch(args.directorio, recursive=False):
        for change_type, filepath in changes:
            filepath = pathlib.Path(filepath)
            if not filepath.is_file():
                continue

            if change_type == Change.added and filepath.suffix.lower() == ".pdf":
                pdf_path = filepath
                logging.info(f"Nuevo PDF detectado: {pdf_path}")

                # Imprimir el PDF usando el comando lpr con la impresora seleccionada
                try:
                    logging.info(f"PDF enviado a la impresora '{impresora_seleccionada}': {pdf_path}")
                    subprocess.run(["lpr", "-P", impresora_seleccionada, str(pdf_path)], check=True)
                    logging.info("PDF impreso exitosamente")
                except Exception as e:
                    logging.error(f"Error al imprimir {pdf_path}: {e}")
                # Mover el archivo a la carpeta de procesados
                shutil.move(str(pdf_path), str(ruta_procesados / pdf_path.name))
                logging.info(f"PDF movido a procesados: {ruta_procesados / pdf_path.name}")
            else:
                logging.info(f"Otro tipo de cambio detectado: {change_type} en {filepath}")


if __name__ == "__main__":
    main()
