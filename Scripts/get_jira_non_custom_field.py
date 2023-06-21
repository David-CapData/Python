# Importation des librairies utilisées
# Import of the used libraries
import requests
import json

# Récupération des identifiants
# Recuperation of the ID
creds_jira = ("ID_for_JIRA","Token-API")

# Appel de L'API via "requests" avec les identifiants
# Call of the api via "requests" with the IDs
r = requests.get("https://testdavidcapdata.atlassian.net/rest/api/3/issue/T1-3", auth=creds_jira)

# IF pour vérifier si l'appel de l'api fonctionne
# IF to verify if the call of the API works
if r.status_code == 200:
    # Affichage du statut de l'appel de l'api
    # Display of API call status 
    print("the status of the get command is : " + str(r.status_code))

    # Création d'une variable contenant toue les données de l'API
    # Creation of variable containing all the data of the API
    data = r.json()

    # Formatage du Json
    # Formatting of Json
    Human_readable_data = json.dumps(data, indent=4)

    # Récupération des valeurs d'un custom field
    # Retrieving the value of a custom field
    champ1 = r.json()['fields']['statuscategorychangedate']
    descprt1 = r.json()['fields']['description']['content'][0]['content'][0]['text']
    comment1 = r.json()['fields']['comment']['comments'][0]['body']['content'][0]['content'][0]['text']

    # Affichage des valeurs récupérées
    # Display of retrieved values
    print("statuscategorychangedate : " + champ1)
    print("Descritpion" + descprt1)
    print(comment1)
else:
    # Affichage du statut de l'appel de l'api
    # Display of API call status 
    print("the status of the get command is : " + str(r.status_code))
