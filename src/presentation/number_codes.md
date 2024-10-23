 
TABLE 1: Data collected using the ANTLR4 library
| Language       | Ingested | Accepted | Parsed ANTLR4 | RQCR Circuit  | Metrics & Patterns |
| -------------- | -------- | -------- | ------------- | ------------- |--------------------|
|Python - Qiskit | 13.462   | 5.004    | 1.616         | 806           | 30                 |
|OpenQASM        | 75.800   |  15.320  | 101           | 101           | 50                 |
(no valid, it has duplicated files)


TABLE 2: Data collected using the ast library:
| Language       | Ingested | Accepted | Parsed AST | RQCR Circuit          | Metrics & Patterns |
| -------------- | -------- | -------- | ---------- | --------------------- |--------------------|
|Python - Qiskit | 6.963    | 5.451    | 5.416      | 2.824 and 2.095 files |    1.945           |
(Ingestion used for TFG)

TABLE 3: Separate metrics and pattenrs:
| Language       | Ingested  | Acepted  | Parsed AST  | Circuit RQCR | Metrics | Patterns |
| -------------- | --------- | -------- | ----------- | ------------ |-------- |----------|
|Python - Qiskit | 6.963     | 5.451    | 5.416       | 2.824        | 1.860   |  537     |



TEST FILES:
|Number of gates | Number of gates with 1 gate | Circuit RQCR     | Metrics | Patterns |
|----------------| --------------------------- |------------------|---------|----------|
| 1              |  257                        |  2.567		      |   257   |	60	   |
| 2              |  287                        |  2.537		      |   287   |	69	   |
| 3              |  102                        |  2.722		      |   102   |	25	   |
| 4              |  56                         |  2.768		      |   56    |	12	   |
| TOTAL          |  600                        |        	      |         |   	   |



TABLE 3: DATA INGESTION SEPTEMBER 2024:
| Language       | Ingested | Accepted | Parsed AST | RQCR Circuit          | Metrics & Patterns |
| -------------- | -------- | -------- | ---------- | --------------------- |--------------------|
|Python - Qiskit | 13.555   | 11.295   | 11.230     | 5.973 and 4.146 files |   2.252            |
| OpenQASM       | 14.942   | 14.942   |  101       | 101                   |   63               |
| TOTAL          | 28.297   | 26.237   | 11.331     | 6.074                 |   2315             |
Duration of data ingestion: 3 días 20h 35 minutos



TABLE 4: Static analysis comparator
| Static analyzer | AST   | RQCR Circuit | Metrics & Patterns |
| --------------- | ----- | ------------ | ------------------ | 
| ANTLR4          | 1.717 | 907          | 80                 | 
| AST             | 5.416 |  2.824       | 612                | 

TABLE 5: DATA INGESTION OCTOBER 2024:
| Language       | Ingested | Accepted | Parsed AST | RQCR Circuit          | Metrics | Patterns |
| -------------- | -------- | -------- | ---------- | --------------------- |---------|----------|
|Python - Qiskit | 8.673    | 6.578    | 6.563      | 3.395 and 2.346 files |   2.373 |   924    |
Duration of data ingestion: 3 días 14h 30 minutos