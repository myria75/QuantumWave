import logging
import configparser
import io
import os

configuration_file = os.path.join("resources", "config", "properties.ini")
config = configparser.ConfigParser()
config.read(configuration_file)

# Crear un objeto StringIO para capturar los logs
log_capture_string = io.StringIO()

# Crear un handler para StringIO
varLogger = logging.StreamHandler(log_capture_string)
varLogger.setLevel(logging.DEBUG)

# Crear el formato del log
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
varLogger.setFormatter(formatter)

# Resetear los handlers
logging.root.handlers = []

# Configurar el logging básico
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(eval(config.get('log', 'file'))),
        varLogger  # Añadir el handler de StringIO
    ],
    encoding="UTF-8"
)

# Ahora, los logs también se capturan en log_capture_string
# Puedes obtener los logs como una cadena con log_capture_string.getvalue()

# Ejemplo de uso
logging.debug("Este es un mensaje de depuración")
logging.info("Este es un mensaje informativo")
logging.warning("Este es un mensaje de advertencia")

# Obtener los logs capturados
log_contents = log_capture_string.getvalue()
print(log_contents)
