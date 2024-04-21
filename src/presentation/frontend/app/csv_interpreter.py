import csv

remove_first_columns = 6
remove_last_columns = 4
delimiter = ";"
file_path = "./app/dataset_openqasm_qiskit.csv"
path_position = 5

def getTableHeader():
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        line_count = 0

        for row in csv_reader:
            if remove_first_columns > 0:
                del row[:remove_first_columns]
            
            if remove_last_columns > 0:
                del row[-remove_last_columns:]
            
            for i in range(0, len(row)):
                if row[i].startswith("m."):
                    row[i] = row[i].replace("m.", "")

            if line_count == 0:
                return row

def getTableContent(path):
    rows = []
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        line_count = 0
        
        for row in csv_reader:
            if row[path_position] != path:
                continue

            if remove_first_columns > 0:
                del row[:remove_first_columns]
            
            if remove_last_columns > 0:
                del row[-remove_last_columns:]
            
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