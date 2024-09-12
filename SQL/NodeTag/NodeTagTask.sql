SELECT taguuid AS id, TAGS.name AS label, USERS.exid, tags.nodeuuid
FROM ACTIVITIES.OA_TAG AS tags
JOIN ACTIVITIES.OA_MEMBERPROFILE AS users ON (users.memberid = tags.owner)