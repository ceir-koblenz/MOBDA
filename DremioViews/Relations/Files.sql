//"MOBDA_Datastore".Relations."Files"."Uniconnect_Relation_Files_Folder_file_contained_in_folder"
SELECT hexedToID(LOWER(HEX(file.id))) as fileid, hexedToID(LOWER(HEX(folder.id))) as folderid
FROM Uniconnect_files."FILES".MEDIA_REVISION as file
JOIN Uniconnect_files."FILES".COLLECTION_TO_MEDIA as cotmedia ON cotmedia.MEDIA_ID = file.MEDIA_ID
JOIN Uniconnect_files."FILES".COLLECTION as folder ON folder.id = cotmedia.COLLECTION_ID
WHERE folder.type = 3 or folder.type = 4

//"MOBDA_Datastore".Relations."Files"."Uniconnect_Relation_Files_Follow_intellectual_entity_has_component"
SELECT CONCAT(hexedToID(LOWER(HEX(follow.USER_ID))), CONCAT('-', hexedToID(LOWER(HEX(follow.MEDIA_ID))))) as followid, hexedToID(LOWER(HEX(file.id))) as fileid
FROM Uniconnect_files."FILES".MEDIA_NOTIFICATION as follow
JOIN Uniconnect_files."FILES".MEDIA_REVISION as file ON file.MEDIA_ID = follow.MEDIA_ID

//"MOBDA_Datastore".Relations."Files"."Uniconnect_Relation_Files_intellectual_entity_has_previous_version"
SELECT hexedToID(LOWER(HEX(subselect.id))) AS fileid, hexedToID(LOWER(HEX(cofiMR.id))) AS previousid
    FROM (SELECT id, media_id, (SELECT MAX(revision_number)
                                FROM Uniconnect_files."FILES".media_revision AS sub
                                WHERE sub.media_id = main.media_id AND sub.revision_number < main.revision_number
                                ) AS previous_revision_number
            FROM Uniconnect_files."FILES".MEDIA_REVISION AS main) AS subselect
        JOIN Uniconnect_files."FILES".MEDIA_REVISION AS cofiMR ON cofiMR.media_id = subselect.media_id AND revision_number = previous_revision_number

//"MOBDA_Datastore".Relations."Files"."Uniconnect_Relation_Files_intellectual_entity_has_recent_version"
SELECT hexedToID(LOWER(HEX(allFiles.id))) as fileid, hexedToID(LOWER(HEX(fileGroups.current_revision_id))) as recentid
    FROM Uniconnect_files."FILES".MEDIA_REVISION AS allFiles
        LEFT JOIN Uniconnect_files."FILES".MEDIA AS fileGroups ON allFiles.media_id = fileGroups.id

//"MOBDA_Datastore".Relations."Files"."Uniconnect_Relation_Files_Like_intellectual_entity_has_component"
SELECT CONCAT(hexedToID(LOWER(HEX(likes.USER_ID))), CONCAT('-', hexedToID(LOWER(HEX(likes.MEDIA_ID))))) as likeid, hexedToID(LOWER(HEX(file.id))) as fileid
FROM Uniconnect_files."FILES".MEDIA_RECOMMEND as likes
JOIN Uniconnect_files."FILES".MEDIA_REVISION as file ON file.MEDIA_ID = likes.MEDIA_ID

//"MOBDA_Datastore".Relations."Files"."Uniconnect_Relation_Files_Tag_intellectual_entity_has_component"
SELECT DISTINCT CONCAT((hexedToID(LOWER(HEX(mediatag.OWNER_user_id)))),CONCAT('-', (hexedToID(LOWER(HEX(mediatag.tag_id)))))) as tagid, hexedToID(LOWER(HEX(file.id))) as fileid
FROM Uniconnect_files."FILES".MEDIA_TO_TAG as mediatag
JOIN Uniconnect_files."FILES".MEDIA_REVISION as file ON file.MEDIA_ID = mediatag.MEDIA_ID

//"MOBDA_Datastore".Relations."Files"."Uniconnect_Relation_Folder_Follow_intellectual_entity_has_component"
SELECT CONCAT(hexedToID(LOWER(HEX(USER_ID))), CONCAT('-', hexedToID(LOWER(HEX(COLLECTION_ID))))) as followid, hexedToID(LOWER(HEX(folder.id))) as folderid
FROM Uniconnect_files."FILES".COLLECTION_NOTIFICATION as follow
JOIN Uniconnect_files."FILES".COLLECTION as folder ON folder.id = follow.COLLECTION_ID
WHERE folder.type = 3 OR folder.type = 4
ORDER BY followid

//"MOBDA_Datastore".Relations."Files"."Uniconnect_Relation_Folders_folder_has_parent"
SELECT  hexedToID(LOWER(HEX(child.id))) as childid, hexedToID(LOWER(HEX(child.parent_id))) as parentid
FROM "Uniconnect_files"."FILES".COLLECTION as child
JOIN Uniconnect_files."FILES".COLLECTION as parent ON parent.id = child.PARENT_ID
WHERE (parent.type = 3 OR parent.type = 4) AND (child.type = 3 OR child.type = 4)

//"MOBDA_Datastore".Relations."Files"."Uniconnect_Relation_FileLibrary_Folder_file_library_conatins_folder"
SELECT DISTINCT hexedToID(LOWER(HEX(lib.id))) as libid, hexedToID(LOWER(HEX(folder.id))) as folderid
FROM Uniconnect_files."FILES".LIBRARY as lib
JOIN Uniconnect_files."FILES".MEDIA_REVISION as file ON file.LIBRARY_ID = lib.id
JOIN Uniconnect_files."FILES".COLLECTION_TO_MEDIA as ctmedia ON ctmedia.MEDIA_ID = file.media_id
JOIN Uniconnect_files."FILES".COLLECTION as folder on folder.id = ctmedia.COLLECTION_ID
WHERE (folder.TYPE = 3 OR folder.TYPE = 4 or folder.TYPE = 1) AND lib.TYPE = 2 

//"MOBDA_Datastore".Relations."Files"."Uniconnect_Relation_Files_Comment_intellectual_entity_has_component"
SELECT hexedToID(LOWER(HEX(file.id))) as fileid, hexedToID(LOWER(HEX(comment.id))) as commentid
FROM Uniconnect_files."FILES".MEDIA_REVISION as file
JOIN Uniconnect_files."FILES".MEDIA_COMMENT as comment ON comment.MEDIA_ID = file.media_ID

//"MOBDA_Datastore".Relations.GroupWorkspaces."Uniconnect_Relation_GroupWorkspace_Filelibrary_space_contains_container"
SELECT gws.COMMUNITY_UUID as workspaceid, hexedToID(LOWER(HEX(filelib.id))) as libid
FROM Uniconnect_files."FILES".LIBRARY as filelib
JOIN Uniconnect_sncomm.SNCOMM.COMMUNITY as gws ON gws.COMMUNITY_UUID = filelib.EXTERNAL_CONTAINER_ID

