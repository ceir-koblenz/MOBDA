//"MOBDA_Datastore".Relations.WikiPages."Uniconnect_Relation_WikiPages_Attachment_intellectual_entity_has_component"
SELECT hexedToID(LOWER(HEX(attachment.id))) as attachmentid, hexedToID(LOWER(HEX(wikipage.id))) as wikipageid, hexedToID(LOWER(HEX(wikipage.media_id))) as mediaid
FROM Uniconnect_wikis.WIKIS.MEDIA_ADDITIONAL_FILE as attachment
JOIN Uniconnect_wikis.WIKIS.MEDIA_REVISION as wikipage ON attachment.MEDIA_ID = wikipage.media_id

//"MOBDA_Datastore".Relations.WikiPages."Uniconnect_Relation_WikiPages_Comment_intellectual_entity_has_component"
SELECT hexedToID(LOWER(HEX(wikipage.id))) as wikipageid, hexedToID(LOWER(HEX(comment.id))) as commentid, hexedToID(LOWER(HEX(wikipage.media_id))) as mediaid
FROM Uniconnect_wikis.WIKIS.MEDIA_COMMENT as comment
JOIN Uniconnect_wikis.WIKIS.MEDIA_REVISION as wikipage ON wikipage.MEDIA_ID = comment.MEDIA_ID

//"MOBDA_Datastore".Relations.WikiPages."Uniconnect_Relation_WikiPages_Follow_intellectual_entity_has_component"
SELECT CONCAT(hexedToID(LOWER(HEX(follow.USER_ID))), CONCAT('-', hexedToID(LOWER(HEX(follow.MEDIA_ID))))) as followid, hexedToID(LOWER(HEX(wikipage.id))) as wikipageid
FROM "Uniconnect_wikis".WIKIS."MEDIA_NOTIFICATION" as follow
JOIN Uniconnect_wikis.WIKIS.MEDIA_REVISION as wikipage ON wikipage.media_id = follow.MEDIA_ID

//"MOBDA_Datastore".Relations.WikiPages."Uniconnect_Relation_WikiPages_intellectual_entity_has_previous_version"
SELECT hexedToID(LOWER(HEX(subselect.id))) AS wikiid, hexedToID(LOWER(HEX(cofiMR.id))) AS previousid
                FROM (SELECT id, media_id, (SELECT MAX(revision_number)
                                            FROM Uniconnect_wikis."WIKIS".media_revision AS sub
                                            WHERE sub.media_id = main.media_id AND sub.revision_number < main.revision_number
                                            ) AS previous_revision_number
                      FROM Uniconnect_wikis."WIKIS".MEDIA_REVISION AS main) AS subselect
                  JOIN Uniconnect_wikis."WIKIS".MEDIA_REVISION AS cofiMR ON cofiMR.media_id = subselect.media_id AND revision_number = previous_revision_number

//"MOBDA_Datastore".Relations.WikiPages."Uniconnect_Relation_WikiPages_intellecutal_entity_has_recent_version"
SELECT hexedToID(LOWER(HEX(allWikis.id))) as wikiid, hexedToID(LOWER(HEX(wikiGroups.current_revision_id))) as recentid
    FROM Uniconnect_wikis."WIKIS".MEDIA_REVISION AS allWikis
        LEFT JOIN Uniconnect_wikis."WIKIS".MEDIA AS wikiGroups ON allWikis.media_id = wikiGroups.id

//"MOBDA_Datastore".Relations.WikiPages."Uniconnect_Relation_WikiPages_Like_intellectual_entity_has_component"
SELECT CONCAT(hexedToID(LOWER(HEX(likes.USER_ID))), CONCAT('-', hexedToID(LOWER(HEX(likes.MEDIA_ID))))) as likeid, hexedToID(LOWER(HEX(wikipage.id))) as wikipageid, hexedToID(LOWER(HEX(wikipage.media_id))) as media_id
FROM Uniconnect_wikis.WIKIS.MEDIA_RECOMMEND as likes
JOIN Uniconnect_wikis.WIKIS.MEDIA_REVISION as wikipage ON likes.MEDIA_ID = wikipage.MEDIA_ID

//"MOBDA_Datastore".Relations.WikiPages."Uniconnect_Relation_WikiPages_Tag_intellectuial_entity_has_component"
SELECT DISTINCT CONCAT((hexedToID(LOWER(HEX(mediatag.OWNER_user_id)))),CONCAT('-', (hexedToID(LOWER(HEX(mediatag.tag_id)))))) as tagid, hexedToID(LOWER(HEX(wikipage.id))) as wikipageid
FROM Uniconnect_wikis."WIKIS".MEDIA_TO_TAG as mediatag
JOIN Uniconnect_wikis."WIKIS".MEDIA_REVISION as wikipage ON wikipage.MEDIA_ID = mediatag.MEDIA_ID

//"MOBDA_Datastore".Relations.WikiPages."Uniconnect_Relation_WikiPages_Wiki"
SELECT hexedToID(LOWER(HEX(wiki.id))) as wikiid, hexedToID(LOWER(HEX(wikipage.id))) as wikipageid
FROM "Uniconnect_wikis".WIKIS."MEDIA_REVISION" as wikipage
JOIN Uniconnect_wikis.WIKIS.library as wiki ON wiki.id = wikipage.LIBRARY_ID

//"MOBDA_Datastore".Relations.WikiPages."Uniconnect_Relation_WikiPages_wiki_page_has_child"
SELECT hexedToID(LOWER(HEX(allWikis.id))) as wikiid, hexedToID(LOWER(HEX(Wikis.current_revision_id))) AS childid
    FROM Uniconnect_wikis.WIKIS.media_revision as allWikis
        JOIN Uniconnect_wikis.WIKIS.NAVIGATION as nav ON allWikis.media_id = nav.MEDIA_PARENT_ID
        JOIN Uniconnect_wikis.WIKIS.MEDIA as Wikis ON Wikis.id = nav.media_id

//"MOBDA_Datastore".Relations.WikiPages."Uniconnect_Relation_WikiPages_wiki_page_has_parent"
SELECT hexedToID(LOWER(HEX(allWikis.id))) as wikiid, hexedToID(LOWER(HEX(Wikis.current_revision_id))) AS parentId
    FROM Uniconnect_wikis.WIKIS.media_revision as allWikis
        JOIN Uniconnect_wikis.WIKIS.NAVIGATION as nav ON allWikis.media_id = nav.media_id
        JOIN Uniconnect_wikis.WIKIS.MEDIA as Wikis ON Wikis.id = nav.media_parent_id
        