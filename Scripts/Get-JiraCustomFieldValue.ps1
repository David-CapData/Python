# Configuration du serveur jira utilisé
# Configuration of the jira server used
Set-JiraConfigServer 'https://testdavidcapdata.atlassian.net'

# Récupération et Affichage du serveur jira utilisé
# Retrieving and displaying the jira server used
$server_used = Get-JiraConfigServer
Write-Output "Le serveur jira used est: $server_used"

# Récupération d'indentifiants, Mettez le un token API pour le mot de passe pour me bon fonctionnement de cette méthode
# Recovery of credentials, Use an API token for the password to ensure that this method works properly
$jira_cred = Get-Credential 'email_de_votre_compte'

# Création d'une sesion Jira avec les identifiants récupérés
# Creation of a Jira session with the recovered identifiers
New-JiraSession -Credential $jira_cred

# Récupération du ticket avec les customfields
# Ticket recovery with customfields
$jira_issue = Get-JiraIssue -Key T1-4 | Select-Object @{Name="CustomField1"; Expression={$_.customfield_10034}}, @{Name="CustomField2"; Expression={$_.customfield_10036.value}}, @{Name="CustomField3"; Expression={$_.customfield_10037.value}} | Format-List

# Affichage des Custom fields
# Display Custom fields
Write-Output $jira_issue

