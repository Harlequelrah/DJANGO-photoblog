from django.shortcuts import render
from . import crud
def display_tasks(request):
    tasks=crud.get_tasks()
    key= [i for i  in tasks[0].keys() ]if tasks else []
    element_to_move = key.pop(-1)
    key.insert(0, element_to_move)
    return render(request,'gestion/affichage_taches.html',context={'tasks':tasks,'key':key})

