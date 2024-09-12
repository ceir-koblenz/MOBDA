from ibm_db import connect
import pandas as pd
import ibm_db_dbi
from bs4 import BeautifulSoup
import neointerface

#Aufbau der Datenbankverbindung zur UniConnect Datenbank opnact/activities
cnxnactivites = connect('DATABASE=opnact;'
                 'HOSTNAME=db2.uniconnect.de;'  # localhost would work 
                 'PORT=50000;'
                 'PROTOCOL=TCPIP;'
                 'UID=reader19;'
                 'PWD=b2BwaRHN;', '', '')
connactivites = ibm_db_dbi.Connection(cnxnactivites)

#SQL Queries

sqlTask = """SELECT Task.nodeuuid AS id, Task.created AS created, Task.description AS content, Task.lastmod AS last_updated, Task.name AS title, PROFILE.EXID, PARENTTASK.PARENTUUID 
FROM ACTIVITIES.OA_NODE AS Task
JOIN ACTIVITIES.OA_MEMBERPROFILE AS profile ON PROFILE.MEMBERID = TASK.CREATEDBY 
JOIN ACTIVITIES.OA_NODE AS parenttask ON PARENTTASK.NODEUUID = TASK.PARENTUUID 
WHERE TASK.nodetype = 'activities/task'
"""

sqlTaskContainer = """SELECT DISTINCT node.activityuuid AS id, PROFILE.EXID 
FROM ACTIVITIES.OA_NODE AS node
JOIN ACTIVITIES.OA_MEMBERPROFILE profile ON PROFILE.MEMBERID = node.CREATEDBY 
WHERE nodetype = 'activities/task' 
"""

sqlTaskAttachment = """SELECT tasks.nodeuuid AS id, tasks.name AS title, tasks.description AS content, tasks.created AS created, tasks.lastmod AS last_updated, users.exid, users.membertype
FROM ACTIVITIES.oa_node AS tasks
JOIN ACTIVITIES.oa_memberprofile AS users ON (users.memberid = tasks.createdby) 
WHERE nodetype = 'application/activityfield' 
"""

sqlTaskComment = """SELECT taskComs.created AS created, taskComs.description AS content, taskComs.lastmod AS last_updated, taskComs.name AS title, taskComs.nodeuuid AS id, users.EXID 
FROM ACTIVITIES.OA_NODE AS taskComs
JOIN ACTIVITIES.OA_MEMBERPROFILE AS users ON (users.memberid = taskComs.createdby)
WHERE nodetype = 'activities/reply' 
"""

sqlTaskFollow= """SELECT CONCAT(taskFollow.nmemberuuid, CONCAT(' - ', task.nodeuuid)) AS id, taskFollow.created AS CREATED, users.EXID, task.PARENTUUID, TASKFOLLOW.NODEUUID 
FROM ACTIVITIES.OA_NODE AS task
JOIN ACTIVITIES.OA_NODEMEMBER  AS taskFollow ON taskFollow.nodeuuid = task.activityuuid
JOIN ACTIVITIES.OA_MEMBERPROFILE AS users ON (users.memberid = taskFollow.memberid)
WHERE TASKFOLLOW.following = 1 AND task.NODETYPE ='activities/task' 
"""

sqlTaskTag = """ SELECT  taguuid AS id, TAGS.name AS label, USERS.exid, tags.nodeuuid
FROM ACTIVITIES.OA_TAG AS tags
JOIN ACTIVITIES.OA_MEMBERPROFILE AS users ON (users.memberid = tags.owner)
"""

#Einlesen der Daten aus den SQL Queries in die Dataframes
dfTask = pd.read_sql(sqlTask, connactivites)
dfTaskContainer = pd.read_sql(sqlTaskContainer, connactivites)
dfTaskAttachment = pd.read_sql(sqlTaskAttachment, connactivites)
dfTaskComment = pd.read_sql(sqlTaskComment, connactivites)
dfTaskFollow = pd.read_sql(sqlTaskFollow, connactivites)
dfTaskTag = pd.read_sql(sqlTaskTag, connactivites)

#Datacleaning:

#Datacleaning Task:
#Content
#Füllen von Null/None Werten
dfTask['CONTENT'] = dfTask['CONTENT'].fillna('NaN')
#print(dfTask['CONTENT'])
dfTask['CONTENT'] = dfTask['CONTENT'].str.replace('\n', '')
dfTask['CONTENT'] = dfTask['CONTENT'].str.replace('\t', '')
dfTask['CONTENT'] = dfTask['CONTENT'].str.replace('\r', '')
dfTask['CONTENT'] = dfTask['CONTENT'].str.replace('\v', '')
dfTask['CONTENT'] = dfTask['CONTENT'].str.replace(';', ',')
dfTask['CONTENT'] = dfTask[['CONTENT']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
#print(dfTask['CONTENT'])
#Timestamp
#print(dfTask['CREATED'])
dfTask['CREATED'] = pd.to_datetime(dfTask['CREATED'])
# Set timezone (replace 'YOUR_TIMEZONE' with the desired timezone)
dfTask['CREATED'] = dfTask['CREATED'].dt.tz_localize('CET')
#print(dfTask['CREATED'])
#print(dfTask['LAST_UPDATED'])
dfTask['LAST_UPDATED'] = pd.to_datetime(dfTask['LAST_UPDATED'])
# Set timezone (replace 'YOUR_TIMEZONE' with the desired timezone)
dfTask['LAST_UPDATED'] = dfTask['LAST_UPDATED'].dt.tz_localize('CET')
#print(dfTask['LAST_UPDATED'])

#Datacleaning TaskAttachment
#Content
#Füllen von Null/None Werten
dfTaskAttachment['CONTENT'] = dfTaskAttachment['CONTENT'].fillna('NaN')
#print(dfTaskAttachment['CONTENT'])
dfTaskAttachment['CONTENT'] = dfTaskAttachment['CONTENT'].str.replace('\n', '')
dfTaskAttachment['CONTENT'] = dfTaskAttachment['CONTENT'].str.replace('\t', '')
dfTaskAttachment['CONTENT'] = dfTaskAttachment['CONTENT'].str.replace('\r', '')
dfTaskAttachment['CONTENT'] = dfTaskAttachment['CONTENT'].str.replace('\v', '')
dfTaskAttachment['CONTENT'] = dfTaskAttachment['CONTENT'].str.replace(';', ',')
dfTaskAttachment['CONTENT'] = dfTaskAttachment[['CONTENT']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
#print(dfTaskAttachment['CONTENT'])
#Timestamp
#print(dfTaskAttachment['CREATED'])
dfTaskAttachment['CREATED'] = pd.to_datetime(dfTaskAttachment['CREATED'])
# Set timezone (replace 'YOUR_TIMEZONE' with the desired timezone)
dfTaskAttachment['CREATED'] = dfTaskAttachment['CREATED'].dt.tz_localize('CET')
#print(dfTaskAttachment['CREATED'])
#print(dfTaskAttachment['LAST_UPDATED'])
dfTaskAttachment['LAST_UPDATED'] = pd.to_datetime(dfTaskAttachment['LAST_UPDATED'])
# Set timezone (replace 'YOUR_TIMEZONE' with the desired timezone)
dfTaskAttachment['LAST_UPDATED'] = dfTaskAttachment['LAST_UPDATED'].dt.tz_localize('CET')
#print(dfTaskAttachment['LAST_UPDATED'])

#Datacleaning TaskComment
#Content
#Füllen von Null/None Werten
dfTaskComment['CONTENT'] = dfTaskComment['CONTENT'].fillna('NaN')
#print(dfTaskComment['CONTENT'])
dfTaskComment['CONTENT'] = dfTaskComment['CONTENT'].str.replace('\n', '')
dfTaskComment['CONTENT'] = dfTaskComment['CONTENT'].str.replace('\t', '')
dfTaskComment['CONTENT'] = dfTaskComment['CONTENT'].str.replace('\r', '')
dfTaskComment['CONTENT'] = dfTaskComment['CONTENT'].str.replace('\v', '')
dfTaskComment['CONTENT'] = dfTaskComment['CONTENT'].str.replace(';', ',')
dfTaskComment['CONTENT'] = dfTaskComment[['CONTENT']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
#print(dfTaskComment['CONTENT'])
#Timestamp
#print(dfTaskComment['CREATED'])
dfTaskComment['CREATED'] = pd.to_datetime(dfTaskComment['CREATED'])
# Set timezone (replace 'YOUR_TIMEZONE' with the desired timezone)
dfTaskComment['CREATED'] = dfTaskComment['CREATED'].dt.tz_localize('CET')
#print(dfTaskComment['CREATED'])
#print(dfTaskComment['LAST_UPDATED'])
dfTaskComment['LAST_UPDATED'] = pd.to_datetime(dfTaskComment['LAST_UPDATED'])
# Set timezone (replace 'YOUR_TIMEZONE' with the desired timezone)
dfTaskComment['LAST_UPDATED'] = dfTaskComment['LAST_UPDATED'].dt.tz_localize('CET')
#print(dfTaskComment['LAST_UPDATED'])

#Datacleaning TaskFollow
#Timestamp
#print(dfTaskFollow['CREATED'])
dfTaskFollow['CREATED'] = pd.to_datetime(dfTaskFollow['CREATED'])
# Set timezone (replace 'YOUR_TIMEZONE' with the desired timezone)
dfTaskFollow['CREATED'] = dfTaskFollow['CREATED'].dt.tz_localize('CET')
#print(dfTaskFollow['CREATED'])

#Connection from NeoInterface to Neo4j
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Ingestion with NeoIntefrace to Neo4j
#(Name Dataframe, Name Label, Aktivieren der Mergefunktion statt Create)
neodb.load_df(dfTask, "Task", merge=True)
neodb.load_df(dfTaskContainer, "TaskContainer", merge=True)
neodb.load_df(dfTaskAttachment, "Attachment", merge=True)
neodb.load_df(dfTaskComment, "Comment", merge=True)
neodb.load_df(dfTaskFollow, "Follow", merge=True)
neodb.load_df(dfTaskTag, "Tag", merge=True)
