SELECT mr.ID AS id, mr.create_date AS created,  mr.LAST_UPDATE AS last_updated, mr.media_label AS title, mr.MEDIA_ID, USER.DIRECTORY_ID, m.CURRENT_REVISION_ID, REPLACE(mr.MEDIA_ID, ' ', '') AS match_media_id, previous.sub_id, previous.previous_id 
FROM FILES.MEDIA_REVISION mr
JOIN FILES.MEDIA m ON mr.MEDIA_ID = m.ID  
JOIN FILES.USER USER ON USER.ID = m.OWNER_USER_ID 
JOIN (
SELECT subselect.id AS sub_id, cofiMR.id AS previous_id
                FROM (SELECT id, media_id, (SELECT MAX(revision_number)
                                            FROM FILES.MEDIA_REVISION AS sub
                                            WHERE sub.media_id = main.media_id AND sub.revision_number < main.revision_number
                                            ) AS previous_revision_number
                      FROM FILES.media_revision AS main) AS subselect
                  JOIN FILES.media_revision AS cofiMR ON cofiMR.media_id = subselect.media_id AND revision_number = previous_revision_number
                  )AS previous ON previous.sub_id = mr.ID 