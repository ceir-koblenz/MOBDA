//Purge von Mapping Properties von BlogPost
MATCH (bp:BlogPost)
SET bp.WEBSITEID = null
SET bp.USERID = null
SET bp.EXTID = null