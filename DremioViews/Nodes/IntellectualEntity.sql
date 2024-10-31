//"MOBDA_Datastore".Nodes."Uniconnect_Node_BlogPost"
SELECT ID, PUBTIME, HITCOUNT, TITLE, UPDATETIME, LEFT(TEXT, 32000) as TEXT, USERID, WEBSITEID, ATOMID, LASTEDITEDBY, LASTSUBMITTEDBY 
FROM "Uniconnect_blogs".BLOGS.WEBLOGENTRY

//"MOBDA_Datastore".Nodes."Uniconnect_Node_BoardPost"
SELECT NODEUUID, CREATED, NAME, LEFT(DESCRIPTION, 32000) as DESCRIPTION, LASTMOD, CONTAINERID, FORUMUUID, TOPICID, NODEFAMILY, PARENTUUID, NODETYPE, CCREFUUID, DESCCREFUUID, DESCMIMETYPE, NODEFIELDUUID, CREATEDBY, LASTMODBY, NODEALIAS, LASTACCESSED, CONTENTMOD, CONTENTMODBY, STATECHANGE, STATECHANGEBY 
FROM "Uniconnect_forum".FORUM."DF_NODE"
WHERE NODETYPE = 'forum/topic'

//"MOBDA_Datastore".Nodes."Uniconnect_Node_File"
SELECT hexedToID(LOWER(HEX(ID))) as ID, CREATE_DATE, LAST_UPDATE, MEDIA_LABEL,  hexedToID(LOWER(HEX(MEDIA_ID))) as MEDIA_ID,  hexedToID(LOWER(HEX(LIBRARY_ID))) as LIBRARY_ID 
FROM "Uniconnect_files"."FILES"."MEDIA_REVISION"

//"MOBDA_Datastore".Nodes."Uniconnect_Node_Folder"
SELECT hexedToID(LOWER(HEX(ID))) as ID, CREATE_DATE, LAST_UPDATE, TITLE, type
FROM "Uniconnect_files"."FILES".COLLECTION

//"MOBDA_Datastore".Nodes."Uniconnect_Node_MicroblogPost"
SELECT ENTRY_ID, CREATION_DATE, UPDATE_DATE, LEFT(CONTENT, 32000) as CONTENT, CATEGORY_TYPE, SOURCE, ITEM_ID, CONTAINER_ID,  ACTOR_UUID  
FROM "Uniconnect_homepage".HOMEPAGE."BOARD_ENTRIES" WHERE CATEGORY_TYPE = 3

//"MOBDA_Datastore".Nodes."Uniconnect_Node_SocialProfile"
SELECT PERSON_ID, CREATION_DATE, LAST_UPDATE, DISPLAYNAME
FROM "Uniconnect_homepage".HOMEPAGE.PERSON
WHERE MEMBER_TYPE = 0

//"MOBDA_Datastore".Nodes."Uniconnect_Node_Task"
SELECT NODEUUID, CREATED, LASTMOD, DESCRIPTION, NAME, NODETYPE FROM "Uniconnect_opnact".ACTIVITIES."OA_NODE"
WHERE NODETYPE = 'activities/task'

//"MOBDA_Datastore".Nodes."Uniconnect_Node_Weblog"
SELECT * FROM "Uniconnect_blogs".BLOGS.WEBSITE

//"MOBDA_Datastore".Nodes."Uniconnect_Node_WikiPage"
SELECT hexedToID(LOWER(HEX(mr.ID))) as ID, mr.CREATE_DATE , mr.LAST_UPDATE,  mr.MEDIA_LABEL, m.SUMMARY,m.DOWNLOAD_CNT, hexedToID(LOWER(HEX(mr.MEDIA_ID))) as MEDIA_ID, hexedToID(LOWER(HEX(mr.LIBRARY_ID))) as LIBRARY_ID 
FROM "Uniconnect_wikis".WIKIS."MEDIA_REVISION" mr JOIN "Uniconnect_wikis".WIKIS."MEDIA" m ON m.ID = mr.MEDIA_ID