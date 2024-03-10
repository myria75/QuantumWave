ANTES:
| Language      | Ingested | Acepted | Parsed ANTLR4 | Circuit RQCR  | Metrics & Patterns |
| ------------- | -------- | ------- | ------------- | ------------- |--------------------|
|Python - Qiskit| 13462    | 5004    | 1616          | 806           | 30                 |
|OpenQASM       | 75800    |  15320  | 101           | 101           | 50                 |


DESPUÉS:
| Language      | Ingested | Acepted | Parsed AST | Circuit RQCR     | Metrics & Patterns |
| ------------- | -------- | ------- | ---------- | ---------------- |--------------------|
|Python - Qiskit| 6963     | 5451    | 5416       | 2752 ANTES 1971* |   1263*            |

2082 files