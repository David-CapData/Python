import requests
import json

# Récupération des credentials
creds_jira = ("ID_for_JIRA","Token-API")

# Ligne pour call l'api du ticket avec les creds en option
r = requests.get("https://testdavidcapdata.atlassian.net/rest/api/3/issue/T1-3", auth=creds_jira)

# Boucle If pour vérifier la possibilité de "GET" l'api
if r.status_code == 200:
    # Si ça fontionne, print 200
    print("the status of the get command is : " + str(r.status_code))

    # Les données de l'api dans la variable data
    data = r.json()

    # Formatage du Json
    Human_readable_data = json.dumps(data, indent=4)

    # Récupération d'un champs en particulier
    champ1 = r.json()['fields']['statuscategorychangedate']
    descprt1 = r.json()['fields']['description']['content'][0]['content'][0]['text']
    comment1 = r.json()['fields']['comment']['comments'][0]['body']['content'][0]['content'][0]['text']

    # Affichage du Json formaté
    print("statuscategorychangedate : " + champ1)
    print("Descritpion" + descprt1)
    print(comment1)
else:
    # Print en cas de non possibilité d'appel de L'api
    print("the status of the get command is : " + str(r.status_code))
