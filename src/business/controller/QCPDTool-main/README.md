# QCPDTool 🧪💻
## Quantum Circuit Pattern Detector Tool
### Sergio Jiménez Fernández - [SergioJF10](https://github.com/SergioJF10)

Welcome to the repository of my web tool for quantum pattern detection in quantum circuits. This tool has been developed to assist quantum computing enthusiasts and professionals in identifying and analyzing quantum patterns within complex circuits. QCPDTool offers an efficient and user-friendly way to explore the structure and behavior of quantum circuits, providing invaluable insights for quantum research and development.

Characterized by an intuitive interface and powerful analysis capabilities, our web tool enables users to upload their own input quantum circuits and visually examine the quantum patterns present. Leveraging quantum information processing techniques, our tool identifies connections, symmetries, and characteristic behaviors in the circuits, helping users gain a better understanding of their structure and detect quantum phenomena of interest. Whether for academic research, industrial applications, or pure curiosity, our quantum pattern detection tool is designed to facilitate and expedite the analysis of quantum circuits, driving quantum computing forward into new frontiers.

## Contents 🗃️
The source code for QCPDTool in this repository is organized as follows:
- `Opt`: Directory for the development of the time comparison script between two different implementations for the automatic pattern detection.
- `QCPDTool`: Django project folder where the all the source code of the web tool is located. The content of this directory is organized following the [Django Project Structure](https://techvidvan.com/tutorials/django-project-structure-layout/).
- `doc`: Folder containing some documentation files: HTML organization diagram, user manual, ... .
- `node_modules`: Some dependencies applied the development of the web tool interface.

## Requirements📎
For this project to be implemented, the following software code dependencies and tools were used:
- [Python](https://www.python.org/downloads/): Python programming language for the source code for the development of the web tool. 
- [Django](https://docs.djangoproject.com/en/4.2/topics/install/): Django library for Python as web framework.
- [Qiskit](https://qiskit.org/documentation/getting_started.html): Qiskit IBM library for Python for Quantum Circuit and Quantum Software programming.

Those links lead to the official downloading and installation websites of each tool.

## References 📑
The theoretical knowledge and competences about the Gate-Based Quantum Computing model are detailed in the following sources:
- Sergio Jiménez-Fernández, José A. Cruz-Lemus, Mario Piattini:
**A Systematic Mapping Study on Quantum Circuits Design Patterns**. _ICEIS (2) 2023: 109-116_
    - Link: https://dblp.org/rec/conf/iceis/Jimenez-Fernandez23
- Frank Leymann: **Towards a Pattern Language for Quantum Algorithm**. _Lecture Notes in Computer Science: 11413_
    - Link: https://link.springer.com/chapter/10.1007/978-3-030-14082-3_19
- quantumcomputingpatterns.org: **Quantun Computing Patterns**
    - Link: https://quantumcomputingpatterns.org/#/
