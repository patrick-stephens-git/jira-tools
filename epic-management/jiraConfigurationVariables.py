#######################
## JIRA Authentication:
## Authentication Variables:
jira_server = 'https://xxx.atlassian.net'
jira_username = 'your_username'
jira_apitoken = 'your_api_token' # Generate API Token: https://id.atlassian.com/manage-profile/security/api-tokens

## JIRA Query Variables:
jql_query = """
            assignee = '{0}' AND issuetype = Epic AND status = '{1}' AND labels = '{2}'
            """

## JIRA Project Variables:
jira_project_label = 'your_label'

## JIRA Status Variables:
jira_status_toDo = 'To Do' # Change to fit status
jira_status_inProgress = 'In Progress' # Change to fit status
jira_status_inTesting = 'In Testing' # Change to fit status
jira_status_inProduction = 'In Production' # Change to fit status

