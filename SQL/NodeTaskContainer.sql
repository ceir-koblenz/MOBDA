SELECT DISTINCT node.activityuuid AS id, PROFILE.EXID 
FROM ACTIVITIES.OA_NODE AS node
JOIN ACTIVITIES.OA_MEMBERPROFILE profile ON PROFILE.MEMBERID = node.CREATEDBY 
WHERE nodetype = 'activities/task'