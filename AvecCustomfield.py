import requests
import json

# Récupération des credentials
creds_jira = ("dpierre@capdata-osmozium.com","ATATT3xFfGF0OHIGHRBDzwFMiRF5uvY5mlUfglXruzOzCHNqfC14LryPt2-cN1urk8ZLATpZUXO3-NlXhJKbW-hgx7c4cWL3RGqohCo64tcYC9FFeHZtVGFQ85bjuMbyy3XnCGQQTc6uHmiv8plucT7GEVT4OlnsAIO6N6E55HF-V3Lqv54_LOE=7CA8ABE7")

# Ligne pour call l'api du ticket avec les creds en option
r = requests.get("https://testdavidcapdata.atlassian.net/rest/api/3/issue/T1-4", auth=creds_jira)

# Boucle If pour vérifier la possibilité de "GET" l'api
if r.status_code == 200:
    # Si ça fontionne, print 200
    print("the status of the get command is : " + str(r.status_code))

    # Les données de l'api dans la variable data
    data = r.json()

    # Formatage du Json
    Human_readable_data = json.dumps(data, indent=4)

    # Récupération d'un champs en particulier
    CustomTest1 = r.json()['fields']['customfield_10034']['content'][0]['content'][0]['text'] # fields.customfield_10034.content[0].content[0].text
    CustomTest2a = r.json()['fields']['customfield_10036'][0]['value'] # fields.customfield_10036[0].value
    CustomTest2b = r.json()['fields']['customfield_10036'][1]['value'] # fields.customfield_10036[1].value
    CustomTest3 = r.json()['fields']['customfield_10037']['value'] # fields.customfield_10037.value

    # Affichage du Json formaté
    print("Voici le contenu du Customfiel1: " + CustomTest1)
    print("Voici le contenu du Customfiel2: " + CustomTest2a + " & " + CustomTest2b)
    print("Voici le contenu du Customfiel3: " + CustomTest3)
else:
    # Print en cas de non possibilité d'appel de L'api
    print("the status of the get command is : " + str(r.status_code))
