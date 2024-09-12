SELECT tags.taguuid AS id, tags.created AS created, tags.name AS label, tags.nodeuuid, users.exid
FROM FORUM.DF_NODE AS boardposts
JOIN FORUM.DF_TAG AS tags ON boardposts.nodeuuid = tags.nodeuuid
JOIN FORUM.DF_MEMBERPROFILE AS users ON (users.memberid = tags.createdby)
WHERE boardposts.nodetype = 'forum/topic'