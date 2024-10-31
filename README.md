# MOBDA 2.0

This repo contains a prototype for [**MOBDA - Materialised Ontology-Based Data Access**](https://github.com/ceir-koblenz/MOBDA) developed by the [CEIR - Center for Enterprise Information Research](https://ceir.de/).

The prototyp builds on the technology of (materialised) ontology-based data access((M)OBDA) (Cysneiros, 2016). OBDA uses a ontology as a semantic layer to harmonise data from different source systems to make them in one data base with the ontologies language accessable. Thereby, the user needs no knowledge of the source systems datastructure and only needs the language of the ontology.
For this MOBDA datastore the Collaborative Actions on Documents Ontology short [ColActDOnt](https://w3id.org/ColActDOnt) is used.

MOBDA datastore builds on several components: 
- [Neo4j](https://neo4j.com/) as a target database, running on a linux server
- A [Dremio](https://www.dremio.com/) instance used as a conferated database with data from a HCL Connections instance as a source system
- MOBDA Application importing the data into the target database which is documented in this repository The application uses:
    - [pandas dataframe](https://pypi.org/project/pandas/) for data preprocessing 
    - [pyneoinstance](https://pypi.org/project/pyneoinstance/) for the data import into neo4j

This figure gives a a overview of the architcture:
![Architcture](<Architecture MOBDAv2.png>)
MOBDA datastore is dependend on all three components.

The repository has five folder:
- DremioViews contains all dremio views and their SQL scripts
- Index contains a file to create Indexes for the Neo4j database
- Import contains all Import Scripts
    - SoloScripts contains import scripts for each element stand alone executable 
        - ImportNodes20 contains scripts for all data nodes
        - OntologyLayer20 contains scripts for the ontology layer
        - Relation20 contains all scripts for relations
    - Execution contains all scripts and allows the execution of all data at once
        -'ExecutionImport.py' is a scripts executing all other scripts for the import
        - The folder contains all subscripts although they are not executable on their own
- Cleanup contains a file 'Delete' that deletes all data from the database
- PowerBIScripts contains a blueprint for importing a queried dataset from Neo4j to PowerBI
- Additionally a yaml file ('exampleYaml.yaml') is used for credentials to Neo4j


Major changes from version 1.0 to 2.0
- Use of Dremio as data source for the import
- Implementing the majority of data logic in Dremio views
- Use of a new import library pyneoinstance which can execute cypher scripts with data from dataframes
- Relations are created from dataframes and cypher queries and no longer using mapping ids
- Mulitprocessing due to pyneoistance
- Single import script to exectue all scripts
- Use of indexes to speed import and querying up

More information can be found in:

- Working Paper (German): [Schlömer, L., Just, M., & Schubert, P. (2024). Integration eines ontologiebasierten Data­stores für Enterprise Collaboration Systems. In CEIR Report (Issue 01/2024, p. 27.)]
- Paper: [Schlömer, L., Just, M., & Schubert, P. (2024). Using Materialised Ontology-Based Data Access (MOBDA) for the Harmonisation of Trace Data from Enterprise Collaboration Systems. 1–16.]
- Just, M., & Schubert, P. (2023). Collaborative Actions on Documents Ontology (ColActDOnt). Procedia Computer Science, 219, 294–302. https://doi.org/10.1016/j.procs.2023.01.293
- [Importing Neo4j Graph Data with Power BI](https://medium.com/codex/importing-neo4j-graph-data-with-power-bi-d2686e9255bc)

\
Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg