import pandas as pd
import pyodbc
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def createRelationAccounts()->None:
    """
    creating all relations related to Account data
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    1. Set up Connection
    2. SQL queries
    3. read data from dremio in dataframe
    4. cypher queries
    5. execute cypher queries with data from dataframes using pyneoinstance
    """

    start_time = time.time()

    # Set up connections

    config = load_yaml_file('C:/Users/lschloemer/Nextcloud/MOBDA 2.0/VSCodeMOBDARepository/Python/a.yaml')
    db_info = config['db_infoneo']
    graph = Neo4jInstance(db_info['uri'],db_info['database'],db_info['password'])

    DSN = "Arrow Flight SQL ODBC DSN"
    cnxn = pyodbc.connect(DSN=DSN ,autocommit=True)

    #SQL Queries
    sqlRelationAccountBlogPost_account_created_item = """
    SELECT id as blogid, prof_guid, extid 
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_BlogPost_account_created_item"
    """

    sqlRelationAccountBoardPost_account_created_item = """
    SELECT nodeuuid, prof_guid, exid
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_BoardPost_account_created_item"
    """

    sqlRelationAccountFile_account_created_item = """
    SELECT id, prof_guid, directory_id
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_File_account_created_item"
    """

    sqlRelationAccountFolder_account_created_item = """
    SELECT id, prof_guid, directory_id
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_Folder_account_created_item"
    """

    sqlRelationAccountMicroblogPost_account_created_item = """
    SELECT entry_id, prof_guid, exid
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_MicroblogPost_account_created_item"
    """

    sqlRelationAccountTask_account_created_item = """
    SELECT nodeuuid, prof_guid, exid 
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_Task_account_created_item"
    """

    sqlRelationAccountWikiPage_account_created_item = """
    SELECT id, prof_guid, directory_id
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_WikiPage_account_created_item"
    """

    sqlRelationAccountSocialProfile_account_has_social_profile = """
    SELECT person_id, prof_guid, exid
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_SocialProfile_account_has_soical_profile"
    """

    sqlRelationAccountEvent_account_performed_event = """
    SELECT event_id, prof_guid
    FROM MOBDA_Datastore.Relations.Account.Uniconnect_Relation_Account_Event_account_performed_event
    """

    sqlRelationAccountPerson_account_of_agent = """
    SELECT accountid, personid, accountmail, personmail 
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_Person_account_of_agent"
    """
    sqlRelationAccountAttachmentBoardPost_account_created_item = """
    SELECT id, accountid
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_AttachmentBoardPost_account_created_item"
    """

    sqlRelationAccountAttachmentWikiPage_account_created_item = """
    SELECT accountid, id 
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_AttachmentWikiPage_account_created_item"
    """

    sqlRelationAccountAttachmentTask_account_created_item = """
    SELECT accountid, id 
    FROM "MOBDA_Datastore".Relations.Account.Uniconnect_Relation_Account_AttachmentTask_account_created_item
    """
    sqlRelationAccountAttachmentSocialProfileComment_account_created_item = """
    SELECT accountid, id 
    FROM MOBDA_Datastore.Relations.Account.Uniconnect_Relation_Account_AttachmentSocialProfileComment_account_created_item
    """
    sqlRelationAccountCommentBlogPost_account_created_item = """
    SELECT accountid, id FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_CommentBlogPost_account_created_item"
    """
    sqlRelationAccountCommentBoardPost_account_created_item = """
    SELECT accountid, id FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_CommentBoardPost_account_created_item"
    """
    sqlRelationAccountCommentFiles_account_created_item ="""
    SELECT accountid, id FROM "MOBDA_Datastore".Relations.Account.Uniconnect_Relation_Account_CommentFiles_account_created_item
    """
    sqlRelationAccountCommentMicroblogPost_account_created_item ="""
    SELECT accountid, id 
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_CommentMicroblogPost_account_created_item"
    """

    sqlRelationAccountCommentSocialProfile_account_created_item ="""
    SELECT accountid, id 
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_CommentSocialProfileComment_account_created_item"
    """

    sqlRelationAccountCommentTask_account_created_item ="""
    SELECT accountid, id
    FROM MOBDA_Datastore.Relations.Account.Uniconnect_Relation_Account_CommentTask_account_created_item
    """
    sqlRelationAccountCommentWikiPage_account_created_item ="""
    SELECT accountid, id
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_CommentWikiPage_account_created_item"
    """
    
    sqlRelationAccountFollowBoardPost_account_created_item ="""
    SELECT id, accountid
    FROM MOBDA_Datastore.Relations.Account.Uniconnect_Relation_Account_FollowBoardPost_account_created_item
    """

    sqlRelationAccountFollowFile_account_created_item = """
    SELECT id, accountid
    FROM MOBDA_Datastore.Relations.Account.Uniconnect_Relation_Account_FollowFile_account_created_item
    """
    sqlRelationAccountFollowFolder_account_created_item ="""
    SELECT id, accountid
    FROM MOBDA_Datastore.Relations.Account.Uniconnect_Relation_Account_FollowFolder_account_created_item
    """
    sqlRelationAccountFollowSocialProfile_account_created_item ="""
    SELECT id, accountid
    FROM MOBDA_Datastore.Relations.Account.Uniconnect_Relation_Account_FollowSocialProfile_account_created_item
    """
    sqlRelationAccountFollowTask_account_created_item ="""
    SELECT id, accountid
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_FollowTask_account_created_item"
    """
    sqlRelationAccountFollowWikiPage_account_created_item ="""
    SELECT id, accountid
    FROM MOBDA_Datastore.Relations.Account.Uniconnect_Relation_Account_FollowWikiPage_account_created_item
    """
    sqlRelationAccountLikeBlogPost_account_created_item ="""
    SELECT id, accountid
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_LikeBlogPost_account_created_item"
    """
    sqlRelationAccountLikeBlogPostComment_account_created_item ="""
    SELECT id, accountid
    FROM MOBDA_Datastore.Relations.Account.Uniconnect_Relation_Account_LikeBlogPostComment_account_created_item
    """
    sqlRelationAccountLikeBoardPost_account_created_item ="""
    SELECT id, accountid
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_LikeBoardPost_account_creatded_item"
    """
    sqlRelationAccountLikeBoardPostComment_account_created_item ="""
    SELECT id, accountid
    FROM MOBDA_Datastore.Relations.Account.Uniconnect_Relation_Account_LikeBoardPostComment_account_created_item
    """
    sqlRelationAccountLikeMicroblogPost_account_created_item ="""
    SELECT id, accountid
    FROM MOBDA_Datastore.Relations.Account.Uniconnect_Relation_Account_LikeMicroblogPost_account_created_item
    """
    sqlRelationAccountLikeMicroblogPostComment_account_created_item ="""
    SELECT id, accountid
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_LikeMircoblogPostComment_account_created_item"
    """
    sqlRelationAccountLikeFile_account_created_item ="""
    SELECT id, accountid
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_LikeFile_account_created_item"
    """
    sqlRelationAccountLikeSocialProfileComment_account_created_item ="""
    SELECT id, accountid 
    FROM MOBDA_Datastore.Relations.Account.Uniconnect_Relation_Account_LikeSocialProfileComment_account_created_item
    """
    sqlRelationAccountLikeSocialProfileCommentAttachment_account_created_item ="""
    SELECT id, accountid
    FROM MOBDA_Datastore.Relations.Account.Uniconnect_Relation_Account_LikeSocialProifileCommentAttachment_account_created_item
    """
    sqlRelationAccountLikeWikiPage_account_created_item ="""
    SELECT id, accountid
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_LikeWikiPage_account_created_item"
    """
    sqlRelationAccountTagBlogPost_account_created_item ="""
    SELECT id, accountid
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_TagBlogPost_account_created_item"
    """
    sqlRelationAccountTagBoardPost_account_created_item ="""
    SELECT id, accountid
    FROM MOBDA_Datastore.Relations.Account.Uniconnect_Relation_Account_TagBoardPost_account_created_item
    """
    sqlRelationAccountTagFile_account_created_item ="""
    SELECT id, accountid
    FROM MOBDA_Datastore.Relations.Account.Uniconnect_Relation_Account_TagFile_account_created_item
    """

    sqlRelationAccountTagSocialProfile_account_created_item ="""
    SELECT id, accountid
    FROM MOBDA_Datastore.Relations.Account.Uniconnect_Relation_Account_TagSocialProfile_account_created_item
    """

    sqlRelationAccountTagTask_account_created_item ="""
    SELECT id, accountid
    FROM MOBDA_Datastore.Relations.Account.Uniconnect_Relation_Account_TagTask_account_created_item
    """
    sqlRelationAccountTagWikiPage_account_created_item ="""
    SELECT id, accountid
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_TagWikiPage_account_created_item"
    """
    sqlRelationAccountGroupWorkspace_account_is_member_of_space ="""
    SELECT id, accountid 
    FROM "MOBDA_Datastore".Relations.Account."Uniconnect_Relation_Account_GroupWorkspace_account_is_member_of_space"
    """

    #Load Dataframes
    #Intellectual Entities
    dfRelationAccountBlogPost_account_created_item = pd.read_sql(sqlRelationAccountBlogPost_account_created_item,cnxn)
    print (dfRelationAccountBlogPost_account_created_item)
    dfRelationAccountBoardPost_account_created_item = pd.read_sql(sqlRelationAccountBoardPost_account_created_item, cnxn)
    print (dfRelationAccountBoardPost_account_created_item)
    dfRelationAccountFile_account_created_item = pd.read_sql(sqlRelationAccountFile_account_created_item, cnxn)
    print (dfRelationAccountFile_account_created_item)
    dfRelationAccountFolder_account_created_item = pd.read_sql(sqlRelationAccountFolder_account_created_item, cnxn)
    print (dfRelationAccountFolder_account_created_item)
    dfRelationAccountMicroblogPost_account_created_item = pd.read_sql(sqlRelationAccountMicroblogPost_account_created_item, cnxn)
    print (dfRelationAccountMicroblogPost_account_created_item)
    dfRelationAccountTask_account_created_item = pd.read_sql(sqlRelationAccountTask_account_created_item, cnxn)
    print (dfRelationAccountTask_account_created_item)
    dfRelationAccountWikiPage_account_created_item = pd.read_sql(sqlRelationAccountWikiPage_account_created_item, cnxn)
    print (dfRelationAccountWikiPage_account_created_item)
    dfRelationAccountSocialProfile_account_has_social_profile = pd.read_sql(sqlRelationAccountSocialProfile_account_has_social_profile, cnxn) # used for both SocialProfile <-> Account relations
    print (dfRelationAccountSocialProfile_account_has_social_profile)

    #Event
    dfRelationAccountEvent_account_performed_event = pd.read_sql(sqlRelationAccountEvent_account_performed_event, cnxn) 
    print (dfRelationAccountEvent_account_performed_event)

    #Agent
    dfRelationAccountPerson_account_of_agent = pd.read_sql(sqlRelationAccountPerson_account_of_agent, cnxn) 
    print (dfRelationAccountPerson_account_of_agent)

    #Attachments
    dfRelationAccountAttachmentBoardPost_account_created_item = pd.read_sql(sqlRelationAccountAttachmentBoardPost_account_created_item, cnxn) 
    print (dfRelationAccountAttachmentBoardPost_account_created_item)
    dfRelationAccountAttachmentWikiPage_account_created_item = pd.read_sql(sqlRelationAccountAttachmentWikiPage_account_created_item, cnxn) 
    print (dfRelationAccountAttachmentWikiPage_account_created_item)
    dfRelationAccountAttachmentTask_account_created_item = pd.read_sql(sqlRelationAccountAttachmentTask_account_created_item, cnxn) 
    print (dfRelationAccountAttachmentTask_account_created_item)
    dfRelationAccountAttachmentSocialProfileComment_account_created_item = pd.read_sql(sqlRelationAccountAttachmentSocialProfileComment_account_created_item, cnxn) 
    print (dfRelationAccountAttachmentSocialProfileComment_account_created_item)

    #Comments
    dfRelationAccountCommentBlogPost_account_created_item = pd.read_sql(sqlRelationAccountCommentBlogPost_account_created_item, cnxn) 
    print (dfRelationAccountCommentBlogPost_account_created_item)
    dfRelationAccountCommentBoardPost_account_created_item = pd.read_sql(sqlRelationAccountCommentBoardPost_account_created_item, cnxn) 
    print (dfRelationAccountCommentBoardPost_account_created_item)
    dfRelationAccountCommentFiles_account_created_item = pd.read_sql(sqlRelationAccountCommentFiles_account_created_item, cnxn) 
    print (dfRelationAccountCommentFiles_account_created_item)
    dfRelationAccountCommentMicroblogPost_account_created_item = pd.read_sql(sqlRelationAccountCommentMicroblogPost_account_created_item, cnxn) 
    print (dfRelationAccountCommentMicroblogPost_account_created_item)
    dfRelationAccountCommentSocialProfile_account_created_item = pd.read_sql(sqlRelationAccountCommentSocialProfile_account_created_item, cnxn) 
    print (dfRelationAccountCommentSocialProfile_account_created_item)
    dfRelationAccountCommentTask_account_created_item = pd.read_sql(sqlRelationAccountCommentTask_account_created_item, cnxn) 
    print (dfRelationAccountCommentTask_account_created_item)
    dfRelationAccountCommentWikiPage_account_created_item = pd.read_sql(sqlRelationAccountCommentWikiPage_account_created_item, cnxn) # ToDo
    print (dfRelationAccountCommentWikiPage_account_created_item)

    #Follow
    dfRelationAccountFollowBoardPost_account_created_item = pd.read_sql(sqlRelationAccountFollowBoardPost_account_created_item, cnxn) 
    print (dfRelationAccountFollowBoardPost_account_created_item)
    dfRelationAccountFollowFile_account_created_item = pd.read_sql(sqlRelationAccountFollowFile_account_created_item, cnxn) 
    print (dfRelationAccountFollowFile_account_created_item)
    dfRelationAccountFollowFolder_account_created_item = pd.read_sql(sqlRelationAccountFollowFolder_account_created_item, cnxn) 
    print (dfRelationAccountFollowFolder_account_created_item)
    dfRelationAccountFollowSocialProfile_account_created_item = pd.read_sql(sqlRelationAccountFollowSocialProfile_account_created_item, cnxn) 
    print (dfRelationAccountFollowSocialProfile_account_created_item)
    dfRelationAccountFollowTask_account_created_item = pd.read_sql(sqlRelationAccountFollowTask_account_created_item, cnxn) 
    print (dfRelationAccountFollowTask_account_created_item)
    dfRelationAccountFollowWikiPage_account_created_item = pd.read_sql(sqlRelationAccountFollowWikiPage_account_created_item, cnxn) 
    print (dfRelationAccountFollowWikiPage_account_created_item)

    #Like
    dfRelationAccountLikeBlogPost_account_created_item = pd.read_sql(sqlRelationAccountLikeBlogPost_account_created_item, cnxn) 
    print (dfRelationAccountLikeBlogPost_account_created_item)
    dfRelationAccountLikeBlogPostComment_account_created_item = pd.read_sql(sqlRelationAccountLikeBlogPostComment_account_created_item, cnxn) 
    print (dfRelationAccountLikeBlogPostComment_account_created_item)
    dfRelationAccountLikeBoardPost_account_created_item = pd.read_sql(sqlRelationAccountLikeBoardPost_account_created_item, cnxn) 
    print (dfRelationAccountLikeBoardPost_account_created_item)
    dfRelationAccountLikeBoardPostComment_account_created_item = pd.read_sql(sqlRelationAccountLikeBoardPostComment_account_created_item, cnxn) 
    print (dfRelationAccountLikeBoardPostComment_account_created_item)
    dfRelationAccountLikeMicroblogPost_account_created_item = pd.read_sql(sqlRelationAccountLikeMicroblogPost_account_created_item, cnxn) 
    print (dfRelationAccountLikeMicroblogPost_account_created_item)
    dfRelationAccountLikeMicroblogPostComment_account_created_item = pd.read_sql(sqlRelationAccountLikeMicroblogPostComment_account_created_item, cnxn) 
    print (dfRelationAccountLikeMicroblogPostComment_account_created_item)
    dfRelationAccountLikeFile_account_created_item = pd.read_sql(sqlRelationAccountLikeFile_account_created_item, cnxn) 
    print (dfRelationAccountLikeFile_account_created_item)
    dfRelationAccountLikeSocialProfileComment_account_created_item = pd.read_sql(sqlRelationAccountLikeSocialProfileComment_account_created_item, cnxn) 
    print (dfRelationAccountLikeSocialProfileComment_account_created_item)
    dfRelationAccountLikeSocialProfileCommentAttachment_account_created_item = pd.read_sql(sqlRelationAccountLikeSocialProfileCommentAttachment_account_created_item, cnxn) 
    print (dfRelationAccountLikeSocialProfileCommentAttachment_account_created_item)
    dfRelationAccountLikeWikiPage_account_created_item = pd.read_sql(sqlRelationAccountLikeWikiPage_account_created_item, cnxn) 
    print (dfRelationAccountLikeWikiPage_account_created_item)

    #Tag
    dfRelationAccountTagBlogPost_account_created_item = pd.read_sql(sqlRelationAccountTagBlogPost_account_created_item, cnxn) 
    print (dfRelationAccountTagBlogPost_account_created_item)
    dfRelationAccountTagBoardPost_account_created_item = pd.read_sql(sqlRelationAccountTagBoardPost_account_created_item, cnxn) 
    print (dfRelationAccountTagBoardPost_account_created_item)
    dfRelationAccountTagFile_account_created_item = pd.read_sql(sqlRelationAccountTagFile_account_created_item, cnxn) 
    print (dfRelationAccountTagFile_account_created_item)
    dfRelationAccountTagSocialProfile_account_created_item = pd.read_sql(sqlRelationAccountTagSocialProfile_account_created_item, cnxn) 
    print (dfRelationAccountTagSocialProfile_account_created_item)
    dfRelationAccountTagTask_account_created_item = pd.read_sql(sqlRelationAccountTagTask_account_created_item, cnxn) 
    print (dfRelationAccountTagTask_account_created_item)
    dfRelationAccountTagWikiPage_account_created_item = pd.read_sql(sqlRelationAccountTagWikiPage_account_created_item, cnxn) 
    print (dfRelationAccountTagWikiPage_account_created_item)

    #GroupWorkspace
    dfRelationAccountGroupWorkspace_account_is_member_of_space = pd.read_sql(sqlRelationAccountGroupWorkspace_account_is_member_of_space, cnxn) 
    print (dfRelationAccountGroupWorkspace_account_is_member_of_space)

    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Cypher Queries
    RelationAccountBlogPost_account_created_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (b:BlogPost{id:row.blogid})
    MATCH (acc:Account{id:row.prof_guid})
    CREATE (b)-[ricby:item_created_by_account]->(acc)
    CREATE (acc)-[raci:account_created_item]->(b)
    """

    RelationAccountBoardPost_account_created_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (bo:BoardPost{id:row.nodeuuid})
    MATCH (acc:Account{id:row.prof_guid})
    CREATE (bo)-[ricby:item_created_by_account]->(acc)
    CREATE (acc)-[raci:account_created_item]->(bo)
    """

    RelationAccountFile_account_created_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (f:File{id:row.id})
    MATCH (acc:Account{id:row.prof_guid})
    CREATE (f)-[ricby:item_created_by_account]->(acc)
    CREATE (acc)-[raci:account_created_item]->(f)
    """
    RelationAccountFolder_account_created_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (fo:Folder{id:row.id})
    MATCH (acc:Account{id:row.prof_guid})
    CREATE (fo)-[ricby:item_created_by_account]->(acc)
    CREATE (acc)-[raci:account_created_item]->(fo)
    """
    RelationAccountMicroblogPost_account_created_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (mp:MicroblogPost{id:row.entry_id})
    MATCH (acc:Account{id:row.prof_guid})
    CREATE (mp)-[ricby:item_created_by_account]->(acc)
    CREATE (acc)-[raci:account_created_item]->(mp)
    """

    RelationAccountTask_account_created_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (t:Task{id:row.nodeuuid})
    MATCH (acc:Account{id:row.prof_guid})
    CREATE (t)-[ricby:item_created_by_account]->(acc)
    CREATE (acc)-[raci:account_created_item]->(t)
    """

    RelationAccountWikiPage_account_created_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (wp:WikiPage{id:row.id})
    MATCH (acc:Account{id:row.prof_guid})
    CREATE (wp)-[ricby:item_created_by_account]->(acc)
    CREATE (acc)-[raci:account_created_item]->(wp)
    """
    RelationAccountSocialProfile_account_has_social_profile= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (sp:SocialProfile{id:row.person_id})
    MATCH (acc:Account{id:row.prof_guid})
    CREATE (sp)-[rahsp:account_has_social_profile {cardinality: "maximal 1" }]->(acc)
    CREATE (acc)-[rspoc:social_profile_of_account]->(sp)
    """

    RelationAccountSocialProfile_account_created_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (sp:SocialProfile{id:row.person_id})
    MATCH (acc:Account{id:row.prof_guid})
    CREATE (sp)-[ricby:item_created_by_account]->(acc)
    CREATE (acc)-[raci:account_created_item]->(sp)
    """

    RelationAccountEvent_account_performed_event= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (acc:Account{id:row.prof_guid})
    MATCH (ev:Event{id:row.event_id})
    CREATE (ev)-[repby:event_performed_by_account {cardinality: "exactly 1"}]->(acc)
    CREATE (acc)-[raha:account_performed_event]->(ev)
    """

    RelationAccountPerson_account_of_agent = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (acc:Account{id:row.accountid})
    MATCH (pe:Person{id:row.personid})
    CREATE (acc)-[racoa:account_of_agent {cardinality: "exactly 1"}]->(pe)
    CREATE (pe)-[raoa:agent_of_account]->(acc)
    """
    RelationAccountAttachement_account_created_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (at:Attachment{id:row.id})
    MATCH (acc:Account{id:row.accountid})
    CREATE (at)-[ricby:item_created_by_account]->(acc)
    CREATE (acc)-[raci:account_created_item]->(at)
    """
    
    RelationAccountComment_account_created_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (com:Comment{id:row.id})
    MATCH (acc:Account{id:row.accountid})
    CREATE (com)-[ricby:item_created_by_account]->(acc)
    CREATE (acc)-[raci:account_created_item]->(com)
    """
    RelationAccountFollow_account_created_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (fol:Follow{id:row.id})
    MATCH (acc:Account{id:row.accountid})
    CREATE (fol)-[ricby:item_created_by_account]->(acc)
    CREATE (acc)-[raci:account_created_item]->(fol)
    """
    RelationAccountLike_account_created_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (li:Like{id:row.id})
    MATCH (acc:Account{id:row.accountid})
    CREATE (li)-[ricby:item_created_by_account]->(acc)
    CREATE (acc)-[raci:account_created_item]->(li)
    """

    RelationAccountTag_account_created_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (ta:Tag{id:row.id})
    MATCH (acc:Account{id:row.accountid})
    CREATE (ta)-[ricby:item_created_by_account]->(acc)
    CREATE (acc)-[raci:account_created_item]->(ta)
    """
    RelationAccountSystem_account_contained_in_system = """
    MATCH (acc:Account)
    MATCH (sy:System)
    CREATE (acc)-[racis:account_contained_in_system {cardinality: "exactly 1"}]->(sy)
    CREATE (sy)-[rsca:system_contains_account]->(acc)
    """

    RelationAccountOrganisation_account_of_agent = """
    MATCH (acc:Account)
    MATCH (org:Organisation)
    CREATE (acc)-[racis:account_of_agent {cardinality: "exactly 1"}]->(org)
    CREATE (org)-[rsca:agent_has_account]->(acc)
    """
     #Organsiation to Person
    RelationOrganisationPerson_organisation_related_to_agent = """
    MATCH (org:Organisation)
    MATCH (per:Person)
    CREATE (org)-[rorta:organisation_related_to_agent]->(per)
    CREATE (per)-[raha:agent_related_to_organisation]->(org)
    """

    RelationAccountGroupWorkspace_account_is_member_of_space= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (gws:GroupWorkspace{id:row.id})
    MATCH (acc:Account{id:row.accountid})
    CREATE (gws)-[ricby:space_has_member_account]->(acc)
    CREATE (acc)-[raci:account_is_member_of_space]->(gws)
    """

    #Execute Import
    #Intellectual Entity
    graph.execute_write_query_with_data(RelationAccountBlogPost_account_created_item, dfRelationAccountBlogPost_account_created_item, "neo4j", partitions = 8, parallel=True, workers = 8)
    graph.execute_write_query_with_data(RelationAccountBoardPost_account_created_item, dfRelationAccountBoardPost_account_created_item, "neo4j", partitions = 8, parallel=True, workers = 8)
    graph.execute_write_query_with_data(RelationAccountFile_account_created_item, dfRelationAccountFile_account_created_item, "neo4j", partitions = 8, parallel=True, workers = 8)
    graph.execute_write_query_with_data(RelationAccountFolder_account_created_item, dfRelationAccountFolder_account_created_item, "neo4j", partitions = 8, parallel=True, workers = 8)
    graph.execute_write_query_with_data(RelationAccountMicroblogPost_account_created_item, dfRelationAccountMicroblogPost_account_created_item, "neo4j", partitions = 8, parallel=True, workers = 8)
    graph.execute_write_query_with_data(RelationAccountTask_account_created_item, dfRelationAccountTask_account_created_item, "neo4j", partitions = 8, parallel=True, workers = 8)
    graph.execute_write_query_with_data(RelationAccountWikiPage_account_created_item, dfRelationAccountWikiPage_account_created_item, "neo4j", partitions = 8, parallel=True, workers = 8)
    graph.execute_write_query_with_data(RelationAccountSocialProfile_account_has_social_profile, dfRelationAccountSocialProfile_account_has_social_profile, "neo4j", partitions = 8, parallel=True, workers = 8)
    graph.execute_write_query_with_data(RelationAccountSocialProfile_account_created_item, dfRelationAccountSocialProfile_account_has_social_profile, "neo4j", partitions = 8, parallel=True, workers = 8)
    graph.execute_write_query_with_data(RelationAccountEvent_account_performed_event, dfRelationAccountEvent_account_performed_event, "neo4j", partitions = 8, parallel=True, workers = 8)
    graph.execute_write_query_with_data(RelationAccountPerson_account_of_agent, dfRelationAccountPerson_account_of_agent, "neo4j", partitions = 8, parallel=True, workers = 8)
    
    #Attachment
    graph.execute_write_query_with_data(RelationAccountAttachement_account_created_item, dfRelationAccountAttachmentBoardPost_account_created_item, "neo4j", partitions = 10, parallel=True, workers = 10)
    graph.execute_write_query_with_data(RelationAccountAttachement_account_created_item, dfRelationAccountAttachmentWikiPage_account_created_item, "neo4j", partitions = 10, parallel=True, workers = 10)
    graph.execute_write_query_with_data(RelationAccountAttachement_account_created_item, dfRelationAccountAttachmentTask_account_created_item, "neo4j", partitions = 10, parallel=True, workers = 10)
    graph.execute_write_query_with_data(RelationAccountAttachement_account_created_item, dfRelationAccountAttachmentSocialProfileComment_account_created_item, "neo4j", partitions = 10, parallel=True, workers = 10)
    
    #Comment
    graph.execute_write_query_with_data(RelationAccountComment_account_created_item, dfRelationAccountCommentBlogPost_account_created_item, "neo4j", partitions = 10, parallel=True, workers = 10)
    graph.execute_write_query_with_data(RelationAccountComment_account_created_item, dfRelationAccountCommentBoardPost_account_created_item, "neo4j", partitions = 10, parallel=True, workers = 10)
    graph.execute_write_query_with_data(RelationAccountComment_account_created_item, dfRelationAccountCommentFiles_account_created_item, "neo4j", partitions = 10, parallel=True, workers = 10)
    graph.execute_write_query_with_data(RelationAccountComment_account_created_item, dfRelationAccountCommentMicroblogPost_account_created_item, "neo4j", partitions = 10, parallel=True, workers = 10)
    graph.execute_write_query_with_data(RelationAccountComment_account_created_item, dfRelationAccountCommentSocialProfile_account_created_item, "neo4j", partitions = 10, parallel=True, workers = 10)
    graph.execute_write_query_with_data(RelationAccountComment_account_created_item, dfRelationAccountCommentTask_account_created_item, "neo4j", partitions = 10, parallel=True, workers = 10)
    graph.execute_write_query_with_data(RelationAccountComment_account_created_item, dfRelationAccountCommentWikiPage_account_created_item, "neo4j", partitions = 10, parallel=True, workers = 10) # ToDo
   
    #Follow
    graph.execute_write_query_with_data(RelationAccountFollow_account_created_item, dfRelationAccountFollowBoardPost_account_created_item, "neo4j", partitions = 10, parallel=True, workers = 10)
    graph.execute_write_query_with_data(RelationAccountFollow_account_created_item, dfRelationAccountFollowFile_account_created_item, "neo4j", partitions = 12, parallel=True, workers = 12)
    graph.execute_write_query_with_data(RelationAccountFollow_account_created_item, dfRelationAccountFollowFolder_account_created_item, "neo4j", partitions = 12, parallel=True, workers = 12)
    graph.execute_write_query_with_data(RelationAccountFollow_account_created_item, dfRelationAccountFollowSocialProfile_account_created_item, "neo4j", partitions = 12, parallel=True, workers = 12)
    graph.execute_write_query_with_data(RelationAccountFollow_account_created_item, dfRelationAccountFollowTask_account_created_item, "neo4j", partitions = 12, parallel=True, workers = 12)
    graph.execute_write_query_with_data(RelationAccountFollow_account_created_item, dfRelationAccountFollowWikiPage_account_created_item, "neo4j", partitions = 12, parallel=True, workers = 12)
    
    #Like
    graph.execute_write_query_with_data(RelationAccountLike_account_created_item, dfRelationAccountLikeBlogPost_account_created_item, "neo4j", partitions = 16, parallel=True, workers = 16)
    graph.execute_write_query_with_data(RelationAccountLike_account_created_item, dfRelationAccountLikeBlogPostComment_account_created_item, "neo4j", partitions = 16, parallel=True, workers = 16)
    graph.execute_write_query_with_data(RelationAccountLike_account_created_item, dfRelationAccountLikeBoardPost_account_created_item, "neo4j", partitions = 16, parallel=True, workers = 16)
    graph.execute_write_query_with_data(RelationAccountLike_account_created_item, dfRelationAccountLikeBoardPostComment_account_created_item, "neo4j", partitions = 16, parallel=True, workers = 16)
    graph.execute_write_query_with_data(RelationAccountLike_account_created_item, dfRelationAccountLikeMicroblogPost_account_created_item, "neo4j", partitions = 16, parallel=True, workers = 16)
    graph.execute_write_query_with_data(RelationAccountLike_account_created_item, dfRelationAccountLikeMicroblogPostComment_account_created_item, "neo4j", partitions = 16, parallel=True, workers = 16)
    graph.execute_write_query_with_data(RelationAccountLike_account_created_item, dfRelationAccountLikeFile_account_created_item, "neo4j", partitions = 16, parallel=True, workers = 16)
    graph.execute_write_query_with_data(RelationAccountLike_account_created_item, dfRelationAccountLikeSocialProfileComment_account_created_item, "neo4j", partitions = 16, parallel=True, workers = 16)
    graph.execute_write_query_with_data(RelationAccountLike_account_created_item, dfRelationAccountLikeSocialProfileCommentAttachment_account_created_item, "neo4j", partitions = 16, parallel=True, workers = 16)
    graph.execute_write_query_with_data(RelationAccountLike_account_created_item, dfRelationAccountLikeWikiPage_account_created_item, "neo4j", partitions = 16, parallel=True, workers = 16)

    #Tag
    graph.execute_write_query_with_data(RelationAccountTag_account_created_item, dfRelationAccountTagBlogPost_account_created_item, "neo4j", partitions = 16, parallel=True, workers = 16)
    graph.execute_write_query_with_data(RelationAccountTag_account_created_item, dfRelationAccountTagBoardPost_account_created_item, "neo4j", partitions = 16, parallel=True, workers = 16)
    graph.execute_write_query_with_data(RelationAccountTag_account_created_item, dfRelationAccountTagFile_account_created_item, "neo4j", partitions = 16, parallel=True, workers = 16)
    graph.execute_write_query_with_data(RelationAccountTag_account_created_item, dfRelationAccountTagSocialProfile_account_created_item, "neo4j", partitions = 16, parallel=True, workers = 16)
    graph.execute_write_query_with_data(RelationAccountTag_account_created_item, dfRelationAccountTagTask_account_created_item, "neo4j", partitions = 16, parallel=True, workers = 16)
    graph.execute_write_query_with_data(RelationAccountTag_account_created_item, dfRelationAccountTagWikiPage_account_created_item, "neo4j", partitions = 16, parallel=True, workers = 16)

    #Other
    graph.execute_write_query(RelationAccountSystem_account_contained_in_system, "neo4j")
    graph.execute_write_query(RelationAccountOrganisation_account_of_agent, "neo4j")
    graph.execute_write_query(RelationOrganisationPerson_organisation_related_to_agent, "neo4j")

    #GroupWorkspace
    graph.execute_write_query_with_data(RelationAccountGroupWorkspace_account_is_member_of_space, dfRelationAccountGroupWorkspace_account_is_member_of_space, "neo4j", partitions = 12, parallel=True, workers = 12)

    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    createRelationAccounts()
