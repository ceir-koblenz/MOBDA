SELECT Task.created AS created, Task.description AS content, Task.lastmod AS last_updated, Task.name AS title, Task.nodeuuid AS id, TASK.ACTIVITYUUID , PROFILE.EXID
FROM ACTIVITIES.OA_NODE AS Task
JOIN ACTIVITIES.OA_MEMBERPROFILE AS profile ON PROFILE.MEMBERID = TASK.CREATEDBY 
WHERE nodetype = 'activities/task'