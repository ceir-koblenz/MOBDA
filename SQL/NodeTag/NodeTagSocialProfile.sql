SELECT prof_tag_id AS id, prof_tag as label, people.prof_guid, 
FROM EMPINST.PEOPLE_TAG AS tags
JOIN EMPINST.employee As people ON (people.prof_key = tags.prof_source_key)