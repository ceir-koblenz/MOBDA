from ibm_db import connect
import pandas as pd
import ibm_db_dbi
from bs4 import BeautifulSoup
import neointerface

#Aufbau der Datenbankverbindung zur UniConnect Datenbank blogs
cnxnblogs = connect('DATABASE=blogs;'
                 'HOSTNAME=db2.uniconnect.de;'  # localhost would work 
                 'PORT=50000;'
                 'PROTOCOL=TCPIP;'
                 'UID=reader19;'
                 'PWD=b2BwaRHN;', '', '')

connblogs = ibm_db_dbi.Connection(cnxnblogs)

#SQL Queries

sqlBlogPost = """SELECT blogposts.id AS id, blogposts.hitcount AS Views, blogposts.pubtime AS created, BLOGPOSTS.title AS title, 
blogposts.updatetime AS last_updated, BLOGPOSTS.userid, BLOGPOSTS.TEXT AS content, blogposts.WEBSITEID, r.EXTID 
FROM  blogs.weblogentry AS blogposts JOIN blogs.ROLLERUSER r ON BLOGPOSTS.USERID = r.ID  
"""

sqlWeblog = """SELECT weblog.id AS id, weblog.NAME AS title, ASSOC.ASSOCID 
FROM BLOGS.WEBSITE AS weblog
JOIN BLOGS.WEBSITEASSOC AS Assoc ON WEBLOG.ID = ASSOC.WEBSITEID
"""

sqlBlogPostComment = """SELECT COMMENT.id AS id, COMMENT.lastUpdated AS last_updated, COMMENT.name AS title , COMMENT.posttime AS created,
 COMMENT.content AS content, COMMENT.entryid, USERS.EXTID 
FROM BLOGS.ROLLER_COMMENT AS comment
JOIN blogs.ROLLERUSER AS users ON (users.id = comment.userid)
 """

sqlBlogPostLike = """ SELECT CONCAT(entryid, CONCAT (' - ', userid)) AS Id, WEBRATING.RATETIME AS created, WEBRATING.ENTRYID, USER.extid
FROM BLOGS.ROLLER_WEBLOGENTRY_RATING AS webrating
JOIN BLOGS.ROLLERUSER USER ON USER.id = WEBRATING.USERID 
"""

sqlBlogPostCommentLike = """SELECT CONCAT(commentid, CONCAT(' - ', userid)) AS id, BCOMMENTLIKE.RATETIME AS created, 
BCOMMENTLIKE.COMMENTID, USER.extid
FROM BLOGS.ROLLER_COMMENT_RATING AS bcommentlike
JOIN BLOGS.ROLLERUSER USER ON USER.id = BCOMMENTLIKE.USERID 
 """

sqlBlogPostTag = """SELECT  tags.id AS id, tags.name AS label, tags.time AS created, tags.entryid, USERS.extid
FROM blogs.ROLLER_WEBLOGENTRYTAG  AS tags
JOIN blogs.ROLLERUSER AS users ON (users.id = tags.userid) 
"""

#Einlesen der Daten aus den SQL Queries in die Dataframes
dfBlogPost = pd.read_sql(sqlBlogPost, connblogs)
dfWeblog = pd.read_sql(sqlWeblog, connblogs)
dfBlogPostComment = pd.read_sql(sqlBlogPostComment, connblogs)
dfBlogPostCommentLike = pd.read_sql(sqlBlogPostCommentLike, connblogs)
dfBlogPostLike = pd.read_sql(sqlBlogPostLike, connblogs)
dfBlogPostTag = pd.read_sql(sqlBlogPostTag, connblogs)

#Datacleaning BlogPost
#Content
#Füllen von Null/None Werten
dfBlogPost['CONTENT'] = dfBlogPost['CONTENT'].fillna('NaN')
#print(dfBlogPost['CONTENT'])
dfBlogPost['CONTENT'] = dfBlogPost['CONTENT'].str.replace('\n', '')
dfBlogPost['CONTENT'] = dfBlogPost['CONTENT'].str.replace('\t', '')
dfBlogPost['CONTENT'] = dfBlogPost['CONTENT'].str.replace('\r', '')
dfBlogPost['CONTENT'] = dfBlogPost['CONTENT'].str.replace('\v', '')
dfBlogPost['CONTENT'] = dfBlogPost['CONTENT'].str.replace(';', ',')
dfBlogPost['CONTENT'] = dfBlogPost[['CONTENT']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
#print(dfBlogPost['CONTENT'])
#Timestamp
#print(dfBlogPost['CREATED'])
dfBlogPost['CREATED'] = pd.to_datetime(dfBlogPost['CREATED'])
# Set timezone (replace 'YOUR_TIMEZONE' with the desired timezone)
dfBlogPost['CREATED'] = dfBlogPost['CREATED'].dt.tz_localize('CET')
#print(dfBlogPost['CREATED'])
#print(dfBlogPost['LAST_UPDATED'])
dfBlogPost['LAST_UPDATED'] = pd.to_datetime(dfBlogPost['LAST_UPDATED'])
# Set timezone (replace 'YOUR_TIMEZONE' with the desired timezone)
dfBlogPost['LAST_UPDATED'] = dfBlogPost['LAST_UPDATED'].dt.tz_localize('CET')
#print(dfBlogPost['LAST_UPDATED'])

#Datacleaning BlogPostComment
#Content
#Füllen von Null/None Werten
dfBlogPostComment['CONTENT'] = dfBlogPostComment['CONTENT'].fillna('NaN')
#print(dfBlogPostComment['CONTENT'])
dfBlogPostComment['CONTENT'] = dfBlogPostComment['CONTENT'].str.replace('\n', '')
dfBlogPostComment['CONTENT'] = dfBlogPostComment['CONTENT'].str.replace('\t', '')
dfBlogPostComment['CONTENT'] = dfBlogPostComment['CONTENT'].str.replace('\r', '')
dfBlogPostComment['CONTENT'] = dfBlogPostComment['CONTENT'].str.replace('\v', '')
dfBlogPostComment['CONTENT'] = dfBlogPostComment['CONTENT'].str.replace(';', ',')
dfBlogPostComment['CONTENT'] = dfBlogPostComment[['CONTENT']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
#print(dfBlogPostComment['CONTENT'])
#Timestamp
#print(dfBlogPostComment['CREATED'])
dfBlogPostComment['CREATED'] = pd.to_datetime(dfBlogPostComment['CREATED'])
# Set timezone (replace 'YOUR_TIMEZONE' with the desired timezone)
dfBlogPostComment['CREATED'] = dfBlogPostComment['CREATED'].dt.tz_localize('CET')
#print(dfBlogPostComment['CREATED'])
#print(dfBlogPostComment['LAST_UPDATED'])
dfBlogPostComment['LAST_UPDATED'] = pd.to_datetime(dfBlogPostComment['LAST_UPDATED'])
# Set timezone (replace 'YOUR_TIMEZONE' with the desired timezone)
dfBlogPostComment['LAST_UPDATED'] = dfBlogPostComment['LAST_UPDATED'].dt.tz_localize('CET')
#print(dfBlogPostComment['LAST_UPDATED'])

#Datacleaning BlogPostLike
#Timestamp
#print(dfBlogPostLike['CREATED'])
dfBlogPostLike['CREATED'] = pd.to_datetime(dfBlogPostLike['CREATED'])
# Set timezone (replace 'YOUR_TIMEZONE' with the desired timezone)
dfBlogPostLike['CREATED'] = dfBlogPostLike['CREATED'].dt.tz_localize('CET')
#print(dfBlogPostLike['CREATED'])

#Datacleaning BlogPostCommentLike
#Timestamp
#print(dfBlogPostCommentLike['CREATED'])
dfBlogPostCommentLike['CREATED'] = pd.to_datetime(dfBlogPostCommentLike['CREATED'])
# Set timezone (replace 'YOUR_TIMEZONE' with the desired timezone)
dfBlogPostCommentLike['CREATED'] = dfBlogPostCommentLike['CREATED'].dt.tz_localize('CET')
#print(dfBlogPostLike['CREATED'])

#Datacleaning BlogPostTag
#Timestamp
#print(dfBlogPostTag['CREATED'])
dfBlogPostTag['CREATED'] = pd.to_datetime(dfBlogPostTag['CREATED'])
# Set timezone (replace 'YOUR_TIMEZONE' with the desired timezone)
dfBlogPostTag['CREATED'] = dfBlogPostTag['CREATED'].dt.tz_localize('CET')
#print(dfBlogPostTag['CREATED'])

#Aufbau Verbindung zu Neo4j
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Ingestion with NeoIntefrace to Neo4j
#(Name Dataframe, Name Label, Aktivieren der Mergefunktion statt Create)
neodb.load_df(dfBlogPost, "BlogPost", merge=True)
neodb.load_df(dfWeblog, "Weblog", merge=True)
neodb.load_df(dfBlogPostComment, "Comment", merge=True)
neodb.load_df(dfBlogPostCommentLike, "Like", merge=True)
neodb.load_df(dfBlogPostLike, "Like", merge=True)
neodb.load_df(dfBlogPostTag, "Tag", merge=True)
