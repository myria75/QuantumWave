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

INGESTA AGOSTO 2024:
| Language      | Ingested | Acepted | Parsed AST | Circuit RQCR     | Metrics & Patterns |
| ------------- | -------- | ------- | ---------- | ---------------- |--------------------|
|Python - Qiskit| 13.555   | 11.295  | 11.230     | 5973             |   2.252            |

4146 files
Duración de la ingesta: 9 días 1h 39 minutos
Cantidad de ingestados TOTALES: 28.297

| Language  | Ingested files | Quantum Programs| Parsed ANTLR4|RQCR     |Number of files|
|-----------|----------------|-----------------|--------------|---------|---------------|
| OpenQASM  | 14.942         | 14.942          |  101         | 101     | 63            |



| Analizador sintáctico | Árboles sintácticos | Circuitos RQCR | Patrones de diseño y métricas |
| --------------------- | ------------------- | -------------- | ----------------------------- | 
| ANTLR4                | 1717                | 907            | 80                            | 
| AST                   | 5416                |  2824          | 612                           | 




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