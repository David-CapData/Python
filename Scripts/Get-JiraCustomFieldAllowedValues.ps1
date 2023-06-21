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

# Création d'une liste contenant les customfileds à analyser
# Creation of a list containing the customfileds to be analysed
$Customefield = @("customfield_10036","customfield_10037")

# Récupération des valeurs autorisées pour chaques customfields
# Recovery of authorised values for each customfield
$jira_issue = Get-JiraIssueEditMetadata -Issue T1-4 | Where-Object {$_.Id -in $Customefield} | Select-Object {$_.AllowedValues.value} | Format-List	

# Affichage des Custom fields
# Display Custom fields
Write-Output $jira_issue

