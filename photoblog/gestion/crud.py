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

def get_task(id):
    reponse=requests.get(server+'/taches/read-task-by-id/'+id)
    if reponse.status_code==200:
        task=reponse.json()
        return task
    else:
        return {}

def ordered(tasks):
    key= [i for i  in tasks[0].keys() ]if tasks else []
    if key:
        element_to_move = key.pop(-1)
        key.insert(0, element_to_move)
        return key


