SELECT DISTINCT tag.ID AS id, tag.CREATE_DATE AS created, tag.TAG AS LABEL, MREVISION.ID AS MEDIA_ID, USER.id AS userid
FROM FILES.TAG tag 
JOIN FILES.MEDIA_TO_TAG AS mediatag ON tag.id = mediatag.TAG_ID
JOIN FILES.MEDIA_REVISION AS mrevision ON MREVISION.MEDIA_ID = MEDIATAG.MEDIA_ID 
JOIN files.MEDIA media ON mediatag.MEDIA_ID = media.id
JOIN FILES.USER AS USER ON media.OWNER_USER_ID  = USER.ID 