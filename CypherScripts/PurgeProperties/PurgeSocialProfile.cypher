//Purge von Mapping Properties von SocialProfile
MATCH (sopo:SocialProfile)
SET sopo.ENTRY_ID = null
SET sopo.EXID = null
