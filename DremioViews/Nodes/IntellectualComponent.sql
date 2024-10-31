//"MOBDA_Datastore".Nodes.Attachment."Uniconnect_Node_Attachment_BoardPost"
SELECT node.NODEUUID, node.FIELDNAME, node.CREATED, node.LASTMOD, node.FORUMUUID, node.TOPICID, node.NODEFAMILY, node.NODETYPE
FROM "Uniconnect_forum".FORUM."DF_NODE" as node 
WHERE NODETYPE = 'application/field'

//"MOBDA_Datastore".Nodes.Attachment."Uniconnect_Node_Attachment_SocialProfile_Comment"
SELECT DISTINCT ATTACH.OBJECT_ID, ATTACH.CREATION_DATE, ATTACH.DISPLAY_NAME
FROM (SELECT be.item_id, be.ENTRY_ID FROM "Uniconnect_homepage".HOMEPAGE."BOARD_ENTRIES" as be 
	WHERE be.category_type = 5 /*eq: SOURCE = 'PROFILES' */
		UNION
	SELECT bCom.item_id, bCom.ENTRY_ID FROM "Uniconnect_homepage".HOMEPAGE."BOARD_COMMENTS" AS bCom) AS socPComments
JOIN "Uniconnect_homepage".HOMEPAGE."BOARD_OBJECT_REFERENCE" AS ATTACH ON ATTACH.ITEM_ID = socPComments.entry_id

//"MOBDA_Datastore".Nodes.Attachment."Uniconnect_Node_Attachment_Task"
SELECT NODEUUID, NAME, DESCRIPTION, CREATED, LASTMOD, NODETYPE, ACTIVITYUUID
FROM "Uniconnect_opnact".ACTIVITIES."OA_NODE"
WHERE NODETYPE = 'application/activityfield'

//"MOBDA_Datastore".Nodes.Attachment."Uniconnect_Node_Attachment_WikiPage"
SELECT DISTINCT hexedToID(LOWER(HEX(ID))) as ID, TITLE, CREATE_DATE, LAST_UPDATE FROM "Uniconnect_wikis".WIKIS."MEDIA_ADDITIONAL_FILE"

//"MOBDA_Datastore".Nodes.Comment."Uniconnect_Node_Comment_BlogPost"
SELECT ID, LASTUPDATED, NAME, POSTTIME, CONTENT
FROM "Uniconnect_blogs".BLOGS."ROLLER_COMMENT"

//"MOBDA_Datastore".Nodes.Comment."Uniconnect_Node_Comment_BoardPost"
SELECT NODEUUID, CREATED, LASTMOD, NAME, DESCRIPTION
FROM "Uniconnect_forum".FORUM."DF_NODE"
WHERE NODETYPE = 'forum/reply'

//"MOBDA_Datastore".Nodes.Comment."Uniconnect_Node_Comment_File"
SELECT hexedToID(LOWER(HEX(ID))) as ID, COMMENT,CREATE_DATE, LAST_UPDATE, TITLE
FROM "Uniconnect_files"."FILES"."MEDIA_COMMENT"

//"MOBDA_Datastore".Nodes.Comment."Uniconnect_Node_Comment_MicroblogPost"
SELECT com.COMMENT_ID, com.CONTENT, com.CREATION_DATE, com.UPDATE_DATE
FROM "Uniconnect_homepage".HOMEPAGE."BOARD_COMMENTS" as com JOIN "Uniconnect_homepage".HOMEPAGE."BOARD_ENTRIES" as entry ON entry.ENTRY_ID = com.ENTRY_ID
WHERE entry.CATEGORY_TYPE = 3

//"MOBDA_Datastore".Nodes.Comment."Uniconnect_Node_Comment_SocialProfile"
SELECT board.ENTRY_ID, board.CREATION_DATE, board.UPDATE_DATE, board.CONTENT FROM "Uniconnect_homepage".HOMEPAGE."BOARD_ENTRIES" as board
WHERE CATEGORY_TYPE = 5
UNION ALL
SELECT cboard.COMMENT_ID, cboard.CREATION_DATE, cboard.UPDATE_DATE, cboard.CONTENT FROM "Uniconnect_homepage".HOMEPAGE."BOARD_COMMENTS" as cboard JOIN "Uniconnect_homepage".HOMEPAGE."BOARD_ENTRIES" as entry ON cboard.ENTRY_ID = entry.ENTRY_ID WHERE entry.CATEGORY_TYPE = 5

//"MOBDA_Datastore".Nodes.Comment."Uniconnect_Node_Comment_Task"
SELECT NODEUUID, NAME, LASTMOD, CREATED, DESCRIPTION
FROM "Uniconnect_opnact".ACTIVITIES."OA_NODE"
WHERE NODETYPE = 'activities/reply'

//"MOBDA_Datastore".Nodes.Comment."Uniconnect_Node_Comment_WikiPage"
SELECT hexedToID(LOWER(HEX(wikicom.id))) as ID, COMMENT,CREATE_DATE, LAST_UPDATE, TITLE, MEDIA_ID
FROM "Uniconnect_wikis".WIKIS."MEDIA_COMMENT" as wikicom