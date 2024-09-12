SELECT mr.ID AS id ,mr.CREATE_DATE AS created, mr.LAST_UPDATE AS last_updated, m.SUMMARY AS content, m.TITLE AS title, m.DOWNLOAD_CNT AS views, mr.MEDIA_ID, USER.directory_id, 
REPLACE(mr.media_id, ' ', '') AS match_media_id, previous.sub_id, previous.previous_id, m.CURRENT_REVISION_ID 
FROM WIKIS.MEDIA m 
JOIN WIKIS.MEDIA_REVISION mr ON m.id = mr.MEDIA_ID 
JOIN WIKIS.USER AS USER ON USER.id = m.OWNER_USER_ID 
JOIN (
SELECT subselect.id AS sub_id, cofiMR.id AS previous_id
                FROM (SELECT id, media_id, (SELECT MAX(revision_number)
                                            FROM WIKIS.MEDIA_REVISION AS sub
                                            WHERE sub.media_id = main.media_id AND sub.revision_number < main.revision_number
                                            ) AS previous_revision_number
                      FROM WIKIS.media_revision AS main) AS subselect
                  JOIN WIKIS.media_revision AS cofiMR ON cofiMR.media_id = subselect.media_id AND revision_number = previous_revision_number
                  )AS previous ON previous.sub_id = mr.ID
