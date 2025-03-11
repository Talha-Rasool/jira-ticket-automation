
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask,request,jsonify

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJIRA', methods=['POST'])
def createJIRA():

    github_payload=request.json
    comment=github_payload['comment']

    issue_title=github_payload["issue"]["title"]
    user_login=github_payload["user"]["login"]

    print(f"Github Webhook-Payload : {github_payload}")

    print(f"User Login: {user_login}")


    url =  "Jira API URL"

    API_TOKEN="your Jira API TOKEN"

    auth = HTTPBasicAuth("email address", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "Order entry fails when selecting supplier.",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "TR"
        },
        "issuetype": {
            "id": "10009"
        },
        "summary": issue_title,
    },
    "update": {}
    } )

    for key, value in comment.items():
        if value == '/jira':
          response = requests.request(
           "POST",
           url,
           data=payload,
           headers=headers,
           auth=auth
           )
        else:
         print('please provide /jira in comment to create ticket')  

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)








