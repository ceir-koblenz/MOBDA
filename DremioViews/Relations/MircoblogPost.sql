//"MOBDA_Datastore".Relations.MicroblogPosts."Uniconnect_Relation_MicroblogPosts_Comment_intellectual_entity_has_component"
SELECT com.COMMENT_ID as comid, mblog.ENTRY_ID as mblogid
FROM "Uniconnect_homepage".HOMEPAGE."BOARD_COMMENTS" as com
JOIN Uniconnect_homepage.HOMEPAGE.BOARD_ENTRIES as mblog ON mblog.ENTRY_ID = com.ENTRY_ID
WHERE mblog.CATEGORY_TYPE = 3

//"MOBDA_Datastore".Relations.MicroblogPosts."Uniconnect_Relation_MicroblogPosts_Like_intellectual_entity_has_component"
SELECT mblog.ENTRY_ID as mblogid,  likes.ITEM_ID, likes.RECOMMENDATION_ID as likeid
FROM Uniconnect_homepage.HOMEPAGE.BOARD_RECOMMENDATIONS as likes
JOIN Uniconnect_homepage.HOMEPAGE.BOARD_ENTRIES as mblog ON likes.ITEM_ID = mblog.ENTRY_ID
WHERE mblog.CATEGORY_TYPE = 3

//"MOBDA_Datastore".Relations.MicroblogPosts."Uniconnect_Relation_MicroblogPosts_Microblog"
SELECT Mblog.BOARD_CONTAINER_ID as mblogid, mblogp.ENTRY_ID as mblogpostid, mblogp.CONTAINER_ID
FROM Uniconnect_homepage.HOMEPAGE.BOARD as Mblog
JOIN Uniconnect_homepage.HOMEPAGE.BOARD_ENTRIES as mblogp ON mblogp.CONTAINER_ID = Mblog.BOARD_CONTAINER_ID
WHERE Mblog.BOARD_OWNER_ASSOC_TYPE = 'community' AND mblogp.CATEGORY_TYPE = 3

//"MOBDA_Datastore".Relations.MicroblogPosts."Uniconnect_Relation_MicroblogPostsComment_Like_intellectual_component_has_simple_component"
SELECT comment.COMMENT_ID as commentid, likes.RECOMMENDATION_ID as likeid
FROM Uniconnect_homepage.HOMEPAGE.BOARD_COMMENTS as comment
JOIN Uniconnect_homepage.HOMEPAGE.BOARD_RECOMMENDATIONS as likes ON likes.ITEM_ID = comment.ITEM_ID
JOIN Uniconnect_homepage.HOMEPAGE.BOARD_ENTRIES as board ON board.ENTRY_ID = comment.ENTRY_ID
WHERE board.CATEGORY_TYPE = 3
