from src.presentation.frontend import run
from src.presentation.frontend import metricsPrueba
from table_information import generateCSV

if __name__ == "__main__":
    run.runFrontend(host='0.0.0.0', port=5000, debug=True)
