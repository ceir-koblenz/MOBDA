SELECT BPOST.nodeuuid AS id, BPOST.FIELDNAME AS title, ATTACHMENT.content AS content, BPOST.CREATED AS created, BPOST.LASTMOD AS last_updated, PROFILE.exid, BPOST.TOPICID 
FROM (SELECT crefuuid, CASE WHEN Forum.DF_CONTENTREF.MIMETYPE = 'text/html' THEN forum.DF_CONTENTREF.DESCOFLOW ELSE forum.DF_CONTENTREF.CURI || '/' || 
forum.DF_CONTENTREF.FILENAME END AS content FROM FORUM.DF_CONTENTREF) AS attachment 
JOIN FORUM.DF_NODE AS BPOST ON attachment.CREFUUID  = BPOST.CCREFUUID  
JOIN FORUM.df_memberprofile AS profile ON PROFILE.memberid = BPOST.createdby
WHERE BPOST.NODETYPE = 'application/field'