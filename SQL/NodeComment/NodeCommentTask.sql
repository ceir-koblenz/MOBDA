SELECT taskComs.created AS created, taskComs.description AS content, taskComs.lastmod AS last_updated, taskComs.name AS title, taskComs.nodeuuid AS id, users.EXID, TASKCOMS.PARENTUUID 
FROM ACTIVITIES.OA_NODE AS taskComs
JOIN ACTIVITIES.OA_MEMBERPROFILE AS users ON (users.memberid = taskComs.createdby)
WHERE nodetype = 'activities/reply'