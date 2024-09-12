SELECT CONCAT(taskFollow.nmemberuuid, CONCAT(' - ', task.nodeuuid)) AS id, taskFollow.created AS CREATED, users.EXID, task.PARENTUUID, TASKFOLLOW.NODEUUID 
FROM ACTIVITIES.OA_NODE AS task
JOIN ACTIVITIES.OA_NODEMEMBER  AS taskFollow ON taskFollow.nodeuuid = task.activityuuid
JOIN ACTIVITIES.OA_MEMBERPROFILE AS users ON (users.memberid = taskFollow.memberid)
WHERE TASKFOLLOW.following = 1 AND task.NODETYPE ='activities/task'
