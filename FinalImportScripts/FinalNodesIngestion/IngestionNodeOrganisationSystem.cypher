//Beide Classes/Nodes sind aktuell noch hardcoded und basieren nicht auf Datebankdatan
//Deswegen werdden sie mit Cypher hardcoded

MERGE (o:Organisation {ID: 1})
    SET
    o.TITLE = 'Universität Koblenz-Landau',
    o.PHONE = '0261 2871667',
    o.EMAIL =  'asta.uni-koblenz.de'

MERGE (s:System {INSTANCETITLE: 'UniConnect'})
    SET
    s.SOFTWAREPRODUCT = 'HCL Connections',
    s.SOFTWARETYPE = 'ECS',
    s.SOFTWAREVENDOR = 'HCL Technologies',
    s.SOFTWAREVERSION = '6.0.0.0'