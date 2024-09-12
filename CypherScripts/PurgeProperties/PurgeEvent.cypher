//Purge von Mapping Properties von Event
MATCH (ev:Event)
SET ev.UUID = null
SET ev.ITEM_UUID = null
SET ev.SOURCE_ID = null
SET ev.MATCH_ITEM_UUID = null