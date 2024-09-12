# MOBDA 1.0

This repo contains a list of [**MOBDA - Materialised Ontology-Based Data Access Systems**](https://github.com/ceir-koblenz/MOBDA) developed by the [CEIR - Center for Enterprise Information Research](https://ceir.de/).

MOBDA builds on several components: 
- [**Neo4j**](https://neo4j.com/) as a target database
- The **DB2 database** of a HCL Connections instance used as a source system
- **MOBDA Application** importing the data into the target database which is documented in this repository. The application uses:
    - [pandas dataframe](https://pypi.org/project/pandas/) for data preprocessing 
    - [Neointerface](https://github.com/GSK-Biostatistics/neointerface/issues) for the data import into neo4j

MOBDA is dependend on all three components.

The repository has three main folder:
 - CypherScripts contains all cypher scripte used for MOBDA
 - FinalImportScrips contains several folder with python files to build/delete the graph in neo4j
    - DeleteDatabase contains a script to delete the graph
    - FinalNodesIngetion contains python scripts to ingest all data layer nodes into neo4j
    - FinalRelations contains python scripts to create all relations between data layer nodes
    - OntologyRelation contains a python script to create the relations between the data and ontology layer
    - OntologyLayer contains a python script to create the ontology layer
    - Purge contains python scripts to delete mapping ids only needed for the import
 - SQL conatins all SQL queries used to get the data from the source system

\
Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg