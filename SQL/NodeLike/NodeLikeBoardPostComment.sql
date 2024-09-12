SELECT likes.created AS created, likes.uuid AS id, likes.nodeid, USERS.exid
FROM FORUM.DF_NODE AS boardP
JOIN FORUM.DF_RECOMMENDATION AS likes ON boardP.nodeuuid = likes.nodeid
JOIN FORUM.DF_MEMBERPROFILE AS users ON (users.memberid = likes.createdby)
WHERE boardP.nodetype = 'forum/reply'