SELECT likes.uuid AS id, likes.created AS created, likes.nodeid, USERS.EXID 
FROM FORUM.DF_NODE AS boardP
JOIN FORUM.DF_RECOMMENDATION AS likes ON boardP.nodeuuid = likes.nodeid
JOIN FORUM.DF_MEMBERPROFILE AS users ON (users.memberid = likes.createdby)
WHERE boardP.nodetype = 'forum/topic'