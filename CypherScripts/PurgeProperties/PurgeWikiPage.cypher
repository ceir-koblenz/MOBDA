//Purge von Mapping Properties von WikiPage
MATCH (wipa:WikiPage)
SET wipa.MEDIA_ID = null
SET wipa.DIRECTORY_ID = null
SET wipa.MATCH_MEDIA_ID = null
SET wipa.CHILD_ID = null
SET wipa.PARENT_ID = null
SET wipa.CURRENT_REVISION_ID = null
SET wipa.SUB_ID = null
SET wipa.PREVIOUS_ID = null
