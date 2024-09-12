//Cypher Skript um die ganze Datenbank zu löschen
//Es muss wegen Event gestückelt werden
//Event.ID ist als einzige ID eine einfache Zahl, dadurch ist die Stücklung so möglich
//Diese Queries lassen sich nicht selbstständig in diesem File ausführen

//für erste 2500000 Nodes Event mit Relations
MATCH (ev:Event)
WHERE ev.ID <=2500000
DETACH DELETE ev

//für Nodes über 25000000 is 40000000 mit Relations
MATCH (ev:Event)
WHERE ev.ID > 2500000 AND ev.ID <=4000000
DETACH DELETE ev

//Für Nodes mit ID über 4000000 und unter 5000000 mit Relatoins
MATCH (ev:Event)
WHERE ev.ID > 4000000 AND ev.ID <=5000000
DETACH DELETE ev

//Für Nodes mit ID über 5000000 und unter 6000000 mit Relatoins
MATCH (ev:Event)
WHERE ev.ID > 5000000 AND ev.ID <=6000000
DETACH DELETE ev

//Für Nodes mit ID über 6000000 und unter 7000000 mit Relatoins
MATCH (ev:Event)
WHERE ev.ID > 6000000 AND ev.ID <= 7000000
DETACH DELETE ev

//Für Nodes mit ID über 7000000 und unter 8000000 mit Relatoins
MATCH (ev:Event)
WHERE ev.ID > 7000000 AND ev.ID <= 8000000
DETACH DELETE ev

//Für Nodes mit ID über 8000000 und unter 9000000 mit Relatoins
MATCH (ev:Event)
WHERE ev.ID > 8000000 AND ev.ID <= 9000000
DETACH DELETE ev 

// Für Nodes mit ID über 9000000 mit Relations
MATCH (ev:Event)
WHERE ev.ID > 9000000
DETACH DELETE ev

//Für den Rest der Nodes mit Relations
MATCH (n)
DETACH DELETE n