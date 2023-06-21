# Importation des librairies utilisées
# Import of the used libraries
import requests
import json

# Récupération des identifiants
# Recuperation of the IDs
creds_jira = ("ID_for_JIRA","Token-API")

# Appel de L'API via "requests" avec les identifiants
# Call of the api via "requests" with the IDs
r = requests.get("https://testdavidcapdata.atlassian.net/rest/api/3/issue/T1-4/editmeta", auth=creds_jira)

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

    # Récupération des valeurs possible d'un custom field
    # Fetch of all possible values of a custom field
    Possible_value1 = r.json()['fields']['customfield_10036']['allowedValues'][0]['value'] # fields.customfield_10036.allowedValues[0].value
    Possible_value2 = r.json()['fields']['customfield_10036']['allowedValues'][1]['value'] # fields.customfield_10036.allowedValues[1].value

    # Affichage en Json formaté
    # Display of the formatted Json
    print("Les valeurs possible du Customfiel2 sont: " + Possible_value1 + " & " + Possible_value2)

else:
    # Affichage du statut de l'appel de l'api
    # Display of API call status 
    print("the status of the get command is : " + str(r.status_code))
