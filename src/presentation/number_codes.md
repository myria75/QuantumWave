ANTES:
| Language      | Ingested | Acepted | Parsed ANTLR4 | Circuit RQCR  | Metrics & Patterns |
| ------------- | -------- | ------- | ------------- | ------------- |--------------------|
|Python - Qiskit| 13462    | 5004    | 1616          | 806           | 30                 |
|OpenQASM       | 75800    |  15320  | 101           | 101           | 50                 |


DESPUÉS:
| Language      | Ingested | Acepted | Parsed AST | Circuit RQCR     | Metrics & Patterns |
| ------------- | -------- | ------- | ---------- | ---------------- |--------------------|
|Python - Qiskit| 6963     | 5451    | 5416       | 2824             |   1860 ANTES 1945  |

2095 files

















DESPUÉS CON MÉTRICAS Y PATRONES SEPARADOS:
| Language      | Ingested | Acepted | Parsed AST | Circuit RQCR     | Metrics | Patterns |
| ------------- | -------- | ------- | ---------- | ---------------- |-------- |----------|
|Python - Qiskit| 6963     | 5451    | 5416       | 2824             |   1860  |  537     |

















TEST FILES:
TOTAL: 600
CIRCUITOS CON 1 PUERTA: 257
| Circuit RQCR     | Metrics | Patterns |
| ---------------- |---------|----------|
| 2567			   |   257	 |	60	    |

CIRCUITOS CON 2 PUERTA: 287
| Circuit RQCR     | Metrics | Patterns |
| ---------------- |---------|----------|
| 2537			   |   287	 |	 69   	|

CIRCUITOS CON 3 PUERTA: 102
| Circuit RQCR     | Metrics | Patterns |
| ---------------- |---------|----------|
| 2722			   |   102	 |	 25 	|

CIRCUITOS CON 4 PUERTA: 56
| Circuit RQCR     | Metrics | Patterns |
| ---------------- |---------|----------|
| 2768			   |   56	 |	 12  	|