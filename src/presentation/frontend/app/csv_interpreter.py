import csv

remove_first_columns_Metrics = 6
remove_last_columns_Metrics = 4
remove_first_columns_Patterns = 41
delimiter = ";"
file_path = "./app/dataset_openqasm_qiskit.csv"
path_position = 5

def getTableHeaderMetrics():
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        line_count = 0

        for row in csv_reader:
            if remove_first_columns_Metrics > 0:
                del row[:remove_first_columns_Metrics]
            
            if remove_last_columns_Metrics > 0:
                del row[-remove_last_columns_Metrics:]
            
            for i in range(0, len(row)):
                if row[i].startswith("m."):
                    row[i] = row[i].replace("m.", "", 1)

            if line_count == 0:
                return row

def getTableHeaderPatterns():
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        line_count = 0

        for row in csv_reader:
            if remove_first_columns_Patterns > 0:
                del row[:remove_first_columns_Patterns]
            
            for i in range(0, len(row)):
                if row[i].startswith("p."):
                    row[i] = row[i].replace("p.", "", 1)

            if line_count == 0:
                return row
            
def getTableContentMetrics(path):
    rows = []
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        line_count = 0
        
        for row in csv_reader:
            if row[path_position] != path:
                continue

            if remove_first_columns_Metrics > 0:
                del row[:remove_first_columns_Metrics]
            
            if remove_last_columns_Metrics > 0:
                del row[-remove_last_columns_Metrics:]
            
            rows.append(row)
            line_count += 1
    return rows

def getTableContentPatterns(path):
    rows = []
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        line_count = 0
        
        for row in csv_reader:
            if row[path_position] != path:
                continue

            if remove_first_columns_Patterns > 0:
                del row[:remove_first_columns_Patterns]
            
            rows.append(row)
            line_count += 1
    return rows

def getAllPaths():
    all_paths = []

    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        line_count = 0
        
        for row in csv_reader:
            all_paths.append(row[path_position])
    
    return list(set(all_paths))

#print(getTableContent("Python_qiskit_qiskit-community_qiskit-algorithms_test.test_grover.py"))