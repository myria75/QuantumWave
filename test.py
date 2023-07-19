import re

content = "import qiskit.*\nafsafsadf\ndsafdsafadfs\noperation"

search_expression = r"import qiskit\.\*(\n)*operation"  
search_result = re.search(search_expression, content, re.MULTILINE)
print("resultados: ", search_result)