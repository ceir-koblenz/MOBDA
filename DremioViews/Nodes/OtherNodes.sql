//"MOBDA_Datastore".Nodes."Uniconnect_Node_Account"
SELECT PROF_GUID, PROF_MAIL_LOWER, PROF_UID, PROF_DISPLAY_NAME, PROF_KEY
FROM "Uniconnect_peopledb".EMPINST.EMPLOYEE

//"MOBDA_Datastore".Nodes."Uniconnect_Node_Event"
SELECT "Event ID", Activity, "Event Local Timestamp", "Event Action" 
FROM CLog.public.clogTest 
WHERE "System Instance" = 'UniConnect'

//"MOBDA_Datastore".Nodes."Uniconnect_Node_GroupWorkspace"
SELECT COMMUNITY_UUID, NAME FROM "Uniconnect_sncomm".SNCOMM.COMMUNITY

//"MOBDA_Datastore".Nodes."Uniconnect_Node_Person"
SELECT PROF_MAIL_LOWER, PROF_SURNAME, PROF_GIVEN_NAME, PROF_GUID, PROF_TELEPHONE_NUMBER
FROM "Uniconnect_peopledb".EMPINST.EMPLOYEE
