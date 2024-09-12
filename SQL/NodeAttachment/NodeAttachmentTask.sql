SELECT tasks.nodeuuid AS id, tasks.name AS title, tasks.description AS content, tasks.created AS created, tasks.lastmod AS last_updated, users.exid, users.membertype, tasks.parentuuid
FROM ACTIVITIES.oa_node AS tasks
JOIN ACTIVITIES.oa_memberprofile AS users ON (users.memberid = tasks.createdby) 
WHERE nodetype = 'application/activityfield'
