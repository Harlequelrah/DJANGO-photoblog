import requests
import json
server='http://localhost:8080/taches'
def get_tasks():
    reponse=requests.get(server+'/taches/read-tasks')
    if reponse.status_code==200:
        tasks=reponse.json()
        return tasks
        # return json.loads(tasks)
    else:
        return {}

