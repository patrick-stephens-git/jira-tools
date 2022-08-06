## Import Variables via Files from Directory:
from epicManagementData import today_date, jira_status_toDo_df, jira_status_inProgress_df, jira_status_inTesting_df, jira_status_inProduction_df

########################
## Email Authentication: 
## Email Sender / Receiver Variables:
list_of_receiver_email_addresses = ['receiver_email_address']

## Authentication for Email Sender:
email_username = 'your_email_address'
email_password = 'your_email_app_password' # The App Password needed after the Google update for Less Secure Apps: https://support.google.com/accounts/answer/6010255?hl=en&p=less-secure-apps&rd=1#zippy=%2Cif-less-secure-app-access-is-on-for-your-account%2Cupdate-your-app-or-operating-system%2Cuse-more-secure-apps%2Cuse-an-app-password

## Email Subject:
email_subject = 'Epic Management for {0}'.format(today_date)

## Email Body:
email_body = """
<b>Epic Management:</b><br>
<br>
<b>In Testing:</b><br>
{0}<br>
<br>
<b>In Progress:</b><br>
{1}<br>
<br>
<b>In Production:</b><br>
{2}<br>
<b>To Do:</b><br>
{3}<br>
<br>
""".format(jira_status_inTesting_df.to_html(),
           jira_status_inProgress_df.to_html(),
           jira_status_inProduction_df.to_html(),
           jira_status_toDo_df.to_html())
