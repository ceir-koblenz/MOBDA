//"MOBDA_Datastore".Relations.Tasks."Uniconnect_Relation_Task_TaskContainer"
SELECT DISTINCT task.NODEUUID as taskid, task.ACTIVITYUUID as containerid
FROM Uniconnect_opnact.ACTIVITIES.OA_NODE as task
WHERE task.NODETYPE = 'activities/task'
ORDER BY task.NODEUUID

//"MOBDA_Datastore".Relations.Tasks."Uniconnect_Relation_Tasks_Attachment_intellectual_entity_has_component"
SELECT task.NODEUUID as taskid, attachment.NODEUUID as attachmentid
FROM Uniconnect_opnact.ACTIVITIES.OA_NODE as task
JOIN Uniconnect_opnact.ACTIVITIES.OA_NODE as attachment ON task.NODEUUID = attachment.PARENTUUID
WHERE task.NODETYPE = 'activities/task'AND attachment.nodetype = 'application/activityfield'

//"MOBDA_Datastore".Relations.Tasks."Uniconnect_Relation_Tasks_Comment_intellectual_entity_has_component"
SELECT task.NODEUUID as taskid, comment.NODEUUID as commentid
FROM Uniconnect_opnact.ACTIVITIES.OA_NODE as task
JOIN Uniconnect_opnact.ACTIVITIES.OA_NODE as comment ON task.NODEUUID = comment.PARENTUUID
WHERE task.NODETYPE = 'activities/task'AND comment.nodetype = 'activities/reply'

//"MOBDA_Datastore".Relations.Tasks."Uniconnect_Relation_Tasks_Follow_intellectual_entity_has_component"
SELECT follow.NODEUUID as taskid , follow.NMEMBERUUID as followid
FROM Uniconnect_opnact.ACTIVITIES.OA_NODEMEMBER as follow
WHERE follow.FOLLOWING = 1

//"MOBDA_Datastore".Relations.Tasks."Uniconnect_Relation_Tasks_Tag_intellectual_entitiy_has_component"
SELECT tag.TAGUUID as tagid, task.NODEUUID as taskid
FROM Uniconnect_opnact.ACTIVITIES.OA_TAG as tag
JOIN Uniconnect_opnact.ACTIVITIES.OA_NODE as task ON tag.NODEUUID = task.NODEUUID

//"MOBDA_Datastore".Relations.Tasks."Uniconnect_Relation_Tasks_task_has_parent"
SELECT tasks.PARENTUUID as parentid, tasks.NODEUUID as childid
FROM (SELECT nodeuuid, parentuuid
    FROM Uniconnect_opnact.ACTIVITIES.OA_NODE
    WHERE NODETYPE = 'activities/task' ) as tasks
    JOIN "Uniconnect_opnact".ACTIVITIES."OA_NODE" as parent ON tasks.PARENTUUID = parent.NODEUUID
    WHERE parent.NODETYPE = 'activities/task'

