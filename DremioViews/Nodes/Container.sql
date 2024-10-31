//"MOBDA_Datastore".Nodes."Uniconnect_Node_FileLibrary"
SELECT hexedToID(LOWER(HEX(lib.id))) as libid, lib.TITLE 
FROM Uniconnect_files."FILES".LIBRARY as lib
WHERE lib.TYPE = 2 

//"MOBDA_Datastore".Nodes."Uniconnect_Node_MessageBoard"
SELECT * FROM "Uniconnect_forum".FORUM."DF_NODECOMMMAP"

//"MOBDA_Datastore".Nodes."Uniconnect_Node_Microblog"
SELECT * FROM "Uniconnect_homepage".HOMEPAGE.BOARD
WHERE BOARD_OWNER_ASSOC_TYPE = 'community'

//"MOBDA_Datastore".Nodes."Uniconnect_Node_TaskContainer"
SELECT DISTINCT ACTIVITYUUID
FROM "Uniconnect_opnact".ACTIVITIES."OA_NODE"
WHERE NODETYPE = 'activities/task'

//"MOBDA_Datastore".Nodes."Unniconnect_Node_Wiki"
SELECT hexedToID(LOWER(HEX(ID))) as ID, TITLE, CREATE_DATE, LAST_UPDATE, EXTERNAL_CONTAINER_ID FROM "Uniconnect_wikis".WIKIS.LIBRARY

//"MOBDA_Datastore".Nodes."Uniconnect_Node_Weblog"
SELECT * FROM "Uniconnect_blogs".BLOGS.WEBSITE