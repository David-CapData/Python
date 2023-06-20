# Configuration du erveur jira utilisé
Set-JiraConfigServer 'https://testdavidcapdata.atlassian.net'

# Récupération et Affichage du serveur jira utilisé
$server_used = Get-JiraConfigServer
Write-Output "Le serveur jira used est: $server_used"

# Récupération et connection sur le serveur jira utilisé avec des identifiants 
# Après plusieurs tests, mettre le mot de passe du compte ne fonctionne pas mais le token si
$jira_cred = Get-Credential 'kegoceh284@bodeem.com'
New-JiraSession -Credential $jira_cred

# Récupération du ticket avec les customfields
$jira_issue = Get-JiraIssue -Key T1-4 | Select-Object @{Name="CustomField1"; Expression={$_.customfield_10034}}, @{Name="CustomField2"; Expression={$_.customfield_10036.value}}, @{Name="CustomField3"; Expression={$_.customfield_10037.value}} | Format-List

# Affichage des Custom fields
Write-Output $jira_issue

