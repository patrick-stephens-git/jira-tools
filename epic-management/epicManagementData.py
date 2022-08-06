## Import JIRA Module Requirements:
from jira import JIRA # Documentation: https://jira.readthedocs.io/examples.html
from jira.client import ResultList
from jira.resources import Issue

## Import Module Requirements:
from datetime import date
import pandas as pd
import time
import re

## Import Variables via Files from Directory:
from jiraConfigurationVariables import jira_server, jira_username, jira_apitoken, jql_query, jira_project_label, jira_status_toDo, jira_status_inProgress, jira_status_inTesting, jira_status_inProduction

## Jira Authenticate:
options = {'server': jira_server}
jira = JIRA(options, basic_auth=(jira_username, jira_apitoken))

def pull_jql(jql_query):
    for attempt in range(5):
        try:
            jql_query = re.sub('\s+', ' ', jql_query)
            # print('JQL Query:' + jql_query) ## Use for troubleshooting
            return jira.search_issues(jql_query, maxResults = False)
        except Exception as e:
            # print(str(e) + '\nAttempt {0} out of 5'.format(attempt + 1))
            if attempt == 4: ## Attempt is '4' because it starts at '0'
                log_errors(e) ## Log Error on final attempt
                time.sleep(2)
            else:
                time.sleep(2)

def log_errors(error):
    with open('error-log.csv','ab') as export_file:
        writer = csv.writer(export_file)
        writer.writerow([error])

def create_issueKey_info_df(df):
    issueKey_info_dict = {'issueType':[],
                          'issueSummary':[],
                          'issueReporter':[],
                          'issueAssignee':[],
                          'issueStatus':[],
                          'jiraLink':[]}

    for index, row in df.iterrows(): 
        issueType, issueSummary, issueReporter, issueAssignee, issueStatus, jiraLink = pull_issueKey_info(row[0])
        issueKey_info_dict['issueType'].append(issueType)
        issueKey_info_dict['issueSummary'].append(issueSummary)
        issueKey_info_dict['issueReporter'].append(issueReporter)
        issueKey_info_dict['issueAssignee'].append(issueAssignee)
        issueKey_info_dict['issueStatus'].append(issueStatus)
        issueKey_info_dict['jiraLink'].append(jiraLink)
        
        df = pd.DataFrame.from_dict(issueKey_info_dict)
    return df

def pull_issueKey_info(issueKey):
    issue = jira.issue(issueKey)
    for attempt in range(5):
        try:
            projectKey = issue.fields.project.key
            projectName = issue.fields.project.name
            issueKey = issue.key
            issueReporter = issue.fields.reporter.displayName
            try:
                epicKey = issue.fields.parent.key
            except Exception as e:
                epicKey = 'None'
            issueType = issue.fields.issuetype.name
            try:
                issueAssignee = issue.fields.assignee.displayName
            except Exception as e:
                issueAssignee = 'Unassigned'
            issueSummary = issue.fields.summary
            issueStatus = issue.fields.status.name
            jiraLink = '{0}/browse/{1}'.format(jira_server, issueKey)
           
            return issueType, issueSummary, issueReporter, issueAssignee, issueStatus, jiraLink
        except Exception as e:
            if attempt == 4: ## Attempt is '4' because it starts at '0'
                log_errors(e) ## Log Error on final attempt
                time.sleep(2)
            else:
                time.sleep(2)

def generate_epic_df(jira_username, jira_status, jira_project_label):
  df = pd.DataFrame()
  data = pull_jql(jql_query.format(jira_username, jira_status, jira_project_label))
  df = df.append(data)
  df = create_issueKey_info_df(df)
  if df.empty == True:
    df = 'None'
  else:
    df = df.sort_values(by='jiraLink', ascending=False).reset_index(drop=True)
  return df

##################
## Date Variables:
today_date = date.today()

#########################
## Create Epic DataFrames
jira_status_toDo_df = generate_epic_df(jira_username, jira_status_toDo, jira_project_label) ## Pull Epics in To Do
jira_status_inProgress_df = generate_epic_df(jira_username, jira_status_inProgress, jira_project_label) ## Pull Epics in Progress
jira_status_inTesting_df = generate_epic_df(jira_username, jira_status_inTesting, jira_project_label) ## Pull Epics in Testing
jira_status_inProduction_df = generate_epic_df(jira_username, jira_status_inProduction, jira_project_label) ## Pull Epics in Production

import emailer