SELECT COMMENT.id AS id, COMMENT.lastUpdated AS last_updated, COMMENT.name AS title , COMMENT.posttime AS created, COMMENT.content AS content, COMMENT.entryid, USERS.EXTID 
FROM BLOGS.ROLLER_COMMENT AS comment
JOIN blogs.ROLLERUSER AS users ON (users.id = comment.userid)