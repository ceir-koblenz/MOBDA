//"MOBDA_Datastore".Relations.BoardPosts."Uniconnect_Relation_BoardPosts_Attachment_intellectual_entity_has_component"
SELECT forum.NODEUUID as forumid, attachment.NODEUUID as attachmentid, attachment.TOPICID
FROM Uniconnect_forum.FORUM.DF_NODE as forum
JOIN Uniconnect_forum.FORUM.DF_Node as attachment ON forum.nodeuuid = attachment.TOPICID
WHERE attachment.NODETYPE = 'application/field' AND forum.NODETYPE =  'forum/topic'

//"MOBDA_Datastore".Relations.BoardPosts."Uniconnect_Relation_BoardPosts_Comment_intellectual_entity_has_component"
SELECT comment.nodeuuid as commentid, forum.nodeuuid as forumid, comment.TOPICID
FROM Uniconnect_forum.FORUM.DF_NODE as comment 
JOIN Uniconnect_forum.FORUM.df_node as forum ON comment.TOPICID = forum.NODEUUID
WHERE comment.NODETYPE =  'forum/reply' AND forum.NODETYPE =  'forum/topic'

//"MOBDA_Datastore".Relations.BoardPosts."Uniconnect_Relation_BoardPosts_Follow_intellectual_entity_has_component"
SELECT follow.uuid as followid, forum.NODEUUID as forumid, follow.TOPICID
FROM Uniconnect_forum.FORUM.DF_SUBSCRIPTION as follow
JOIN Uniconnect_forum.FORUM.DF_NODE as forum ON follow.TOPICID = forum.TOPICID
WHERE forum.NODETYPE =  'forum/topic'

//"MOBDA_Datastore".Relations.BoardPosts."Uniconnect_Relation_BoardPosts_Like_intellectual_entity_has_component"
SELECT likes.uuid as likeid, forum.NODEUUID as forumid, likes.nodeid
FROM Uniconnect_forum.FORUM.DF_RECOMMENDATION as likes
JOIN Uniconnect_forum.FORUM.DF_NODE as forum ON likes.NODEID = forum.NODEUUID
WHERE forum.NODETYPE = 'forum/topic'

//"MOBDA_Datastore".Relations.BoardPosts."Uniconnect_Relation_BoardPosts_MessageBoard_board_post_contained_in_message_board"
SELECT forum.NODEUUID as forumid, board.FORUMUUID as mboardid, forum.FORUMUUID
FROM Uniconnect_forum.FORUM.DF_NODE as forum
JOIN Uniconnect_forum.FORUM.DF_NODECOMMMAP as board ON board.FORUMUUID = forum.FORUMUUID
WHERE forum.NODETYPE = 'forum/topic'

//"MOBDA_Datastore".Relations.BoardPosts."Uniconnect_Relation_BoardPosts_Tag_intellectual_entity_has_component"
SELECT tag.TAGUUID as tagid, forum.NODEUUID as forumid, tag.NODEUUID
FROM "Uniconnect_forum".FORUM."DF_TAG" as tag
JOIN Uniconnect_forum.FORUM.DF_NODE as forum on forum.NODEUUID = tag.NODEUUID
WHERE forum.NODETYPE = 'forum/topic'

//"MOBDA_Datastore".Relations.BoardPosts."Uniconnect_Relation_BoardPostsComment_Like_intellectual_component_has_simple_component"
SELECT comment.NODEUUID as commentid, likes.UUID as likeid
FROM Uniconnect_forum.FORUM.DF_RECOMMENDATION as likes
JOIN Uniconnect_forum.FORUM.DF_NODE as comment ON likes.NODEID = comment.NODEUUID
WHERE comment.NODETYPE =  'forum/reply'