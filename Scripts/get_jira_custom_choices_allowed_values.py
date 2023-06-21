import requests
import json

# Récupération des credentials
creds_jira = ("ID_for_JIRA","Token-API")

# Ligne pour call l'api du ticket avec les creds en option
r = requests.get("https://testdavidcapdata.atlassian.net/rest/api/3/issue/T1-4/editmeta", auth=creds_jira)

# Boucle If pour vérifier la possibilité de "GET" l'api
if r.status_code == 200:
    # Si ça fontionne, print 200
    print("the status of the get command is : " + str(r.status_code))

    # Les données de l'api dans la variable data
    data = r.json()

    # Formatage du Json
    Human_readable_data = json.dumps(data, indent=4)

    # Récupération des valeurs possible d'un custom field
    Possible_value1 = r.json()['fields']['customfield_10036']['allowedValues'][0]['value'] # fields.customfield_10036.allowedValues[0].value
    Possible_value2 = r.json()['fields']['customfield_10036']['allowedValues'][1]['value'] # fields.customfield_10036.allowedValues[1].value

    # Affichage en Json formaté
    print("Les valeurs possible du Customfiel2 sont: " + Possible_value1 + " & " + Possible_value2)

else:
    # Print en cas de non possibilité d'appel de L'api
    print("the status of the get command is : " + str(r.status_code))
