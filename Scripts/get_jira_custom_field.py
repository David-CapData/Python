# Importation des librairies utilisées
# Import of the used libraries
import requests
import json

# Récupération des identifiants
# Recuperation of the ID
creds_jira = ("ID_for_JIRA","Token-API")

# Appel de L'API via "requests" avec les identifiants
# Call of the api via "requests" with the IDs
r = requests.get("https://testdavidcapdata.atlassian.net/rest/api/3/issue/T1-4", auth=creds_jira)

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
    CustomTest1 = r.json()['fields']['customfield_10034']['content'][0]['content'][0]['text'] # fields.customfield_10034.content[0].content[0].text
    CustomTest2a = r.json()['fields']['customfield_10036'][0]['value'] # fields.customfield_10036[0].value
    CustomTest2b = r.json()['fields']['customfield_10036'][1]['value'] # fields.customfield_10036[1].value
    CustomTest3 = r.json()['fields']['customfield_10037']['value'] # fields.customfield_10037.value

    # Affichage des valeurs récupérées
    # Display of retrieved values
    print("Voici le contenu du Customfiel1: " + CustomTest1)
    print("Voici le contenu du Customfiel2: " + CustomTest2a + " & " + CustomTest2b)
    print("Voici le contenu du Customfiel3: " + CustomTest3)
else:
    # Affichage du statut de l'appel de l'api
    # Display of API call status 
    print("the status of the get command is : " + str(r.status_code))
