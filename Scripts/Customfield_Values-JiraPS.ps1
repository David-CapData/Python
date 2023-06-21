# Configuration du erveur jira utilisé
Set-JiraConfigServer 'https://testdavidcapdata.atlassian.net'

# Récupération et Affichage du serveur jira utilisé
$server_used = Get-JiraConfigServer
Write-Output "Le serveur jira used est: $server_used"

# Récupération d'indentifiants, Mettez le un token API pour le mot de passe pour me bon fonctionnement de cette méthode
$jira_cred = Get-Credential 'email_de_votre_compte'

# Création d'une sesion Jira avec les identifiants récupérés
New-JiraSession -Credential $jira_cred

# Création d'une liste contenant les customfileds à analyser
$Customefield = @("customfield_10036","customfield_10037")

#Récupération des valeurs autorisées pour chaques customfields
$jira_issue = Get-JiraIssueEditMetadata -Issue T1-4 | Where-Object {$_.Id -in $Customefield} | Select-Object {$_.AllowedValues.value} | Format-List	

# Affichage des Custom fields
Write-Output $jira_issue

