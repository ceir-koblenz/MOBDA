SELECT e.prof_mail_lower AS email, e.prof_guid AS id, CONCAT(e.prof_given_name, CONCAT(' ', e.prof_surname)) AS publicName, e.PROF_UID AS privateName, e.Prof_GUID
FROM EMPINST.EMPLOYEE e