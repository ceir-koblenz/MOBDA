//"MOBDA_Datastore".Relations.Blogs."Uniconnect_Relation_BlogPostsComment_Like_intellectual_component_has_simple_component"
SELECT CONCAT(likes.USERID, CONCAT('-', likes.COMMENTID)) as likeid, comment.id as commentid
FROM Uniconnect_blogs.BLOGS.ROLLER_COMMENT_RATING as likes
JOIN Uniconnect_blogs.BLOGS.ROLLER_COMMENT as comment ON likes.COMMENTID = comment.ID

//"MOBDA_Datastore".Relations.Blogs."Uniconnect_Relation_Blogs_blog_post_contained_in_weblog"
SELECT blog.id as blogid, blog.WEBSITEID, weblog.id as weblogid
FROM "Uniconnect_blogs".BLOGS.WEBLOGENTRY as blog
JOIN "Uniconnect_blogs".BLOGS.WEBSITE as weblog ON blog.WEBSITEID = weblog.ID

//"MOBDA_Datastore".Relations.Blogs."Uniconnect_Relation_Blogs_Comment_intellectual_entity_has_component"
SELECT  blog.id as blogid, com.entryid, com.ID as comid
FROM "Uniconnect_blogs".BLOGS."ROLLER_COMMENT" as com
JOIN "Uniconnect_blogs".BLOGS.WEBLOGENTRY as blog ON blog.ID = com.ENTRYID

//"MOBDA_Datastore".Relations.Blogs."Uniconnect_Relation_Blogs_Like_intellectual_entity_has_component"
SELECT CONCAT(likes.userid, CONCAT ('-', likes.entryid)) AS likeid, likes.ENTRYID, blog.id as blogid
FROM "Uniconnect_blogs".BLOGS.ROLLER_WEBLOGENTRY_RATING as likes
JOIN Uniconnect_blogs.BLOGS.WEBLOGENTRY as blog ON blog.id = likes.ENTRYID

//"MOBDA_Datastore".Relations.Blogs."Uniconnect_Relation_Blogs_Tag_intellectual_entity_has_component"
SELECT tag.id as tagid, blog.id as blogid, tag.entryid
FROM Uniconnect_blogs.BLOGS.ROLLER_WEBLOGENTRYTAG as tag
JOIN Uniconnect_blogs.BLOGS.WEBLOGENTRY as blog ON blog.id = tag.ENTRYID

