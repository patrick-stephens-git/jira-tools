README.txt

CONTENTS OF THIS FILE
---------------------
   
 * Introduction
 * Requirements
 * Configuration
 * Instructions


INTRODUCTION
------------

This script will send an email to recipients that provide status updates on all Epics assigned to you that contain a specified label.


REQUIREMENTS
------------

This module requires the following external modules:

 * smtplib
 * ssl
 * email
 * jira
 * datetime
 * time
 * pandas
 * re


CONFIGURATION
-------------

 * epicManagementData.py - script
 * emailer.py - script
 * jiraConfigurationVariables.py - jira configuration variables
 * emailConfigurationVariables.py - email configuration variables


INSTRUCTIONS
-------------

Command:
    $ python3 epicManagementData.py
Output: 
    Email: Epic Management for YYYY-MM-DD

    Epic Management:

	In Testing:
	issueType	issueSummary	issueReporter	issueAssignee	issueStatus	jiraLink
	0	Epic	Summary			Name			Name			Status 		https://xxx.atlassian.net/browse/ABC-123
	0	Epic	Summary			Name			Name			Status 		https://xxx.atlassian.net/browse/ABC-124

	In Progress:
	issueType	issueSummary	issueReporter	issueAssignee	issueStatus	jiraLink
	0	Epic	Summary			Name			Name			Status 		https://xxx.atlassian.net/browse/ABC-125
	0	Epic	Summary			Name			Name			Status 		https://xxx.atlassian.net/browse/ABC-126

	In Production:
	issueType	issueSummary	issueReporter	issueAssignee	issueStatus	jiraLink
	0	Epic	Summary			Name			Name			Status 		https://xxx.atlassian.net/browse/ABC-127
	0	Epic	Summary			Name			Name			Status 		https://xxx.atlassian.net/browse/ABC-128

	To Do:
	issueType	issueSummary	issueReporter	issueAssignee	issueStatus	jiraLink
	0	Epic	Summary			Name			Name			Status 		https://xxx.atlassian.net/browse/ABC-129
	0	Epic	Summary			Name			Name			Status 		https://xxx.atlassian.net/browse/ABC-130