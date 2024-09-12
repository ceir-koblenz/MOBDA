SELECT boardP.nodeuuid AS id, boardP.created AS created, boardP.description AS content, boardP.lastmod AS last_updated, boardP.name AS title, USERS.exid, BOARDP.TOPICID
FROM forum.df_node AS boardP
JOIN forum.df_memberprofile AS users ON (users.memberid = boardP.createdby)
WHERE nodetype = 'forum/reply'
