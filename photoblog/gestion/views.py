from django.shortcuts import render,redirect
import httpx
from django.contrib import messages
from . import crud,forms
from django.contrib.auth.decorators import login_required,permission_required
server='http://localhost:8080/taches'

@login_required
@permission_required('auth.view_gestion',raise_exception=True)
def display_tasks(request):
    tasks=crud.get_tasks()
    key= [i for i  in tasks[0].keys() ]if tasks else []
    element_to_move = key.pop(-1)
    key.insert(0, element_to_move)

    return render(request,'gestion/affichage_taches.html',context={'tasks':tasks,'key':key})

@login_required
@permission_required('auth.add_gestion',raise_exception=True)
def post_task(request):
    form = forms.CreateTask()
    if request.method == 'POST':
        form = forms.CreateTask(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['auteur'] = request.user.username
            data['date_echeance'] = data['date_echeance'].isoformat()
            data['date_debut'] = data['date_debut'].isoformat()
            if data.get('date_fin'):
                data['date_fin'] = data['date_fin'].isoformat()
            api_url = server + '/taches/create-task'
            try:
                # Utilisation de httpx.Client().post pour envoyer une requête POST
                with httpx.Client() as client:
                    response = client.post(api_url, json=data)
                if response.status_code == 200:
                    messages.success(request, 'Tache créée avec succès')
                    return redirect('get_tasks')
                else:
                    messages.error(request, 'Echec lors de la création de la tache')
                    return redirect('post_task')
            except httpx.HTTPError as e:
                error_message = "Echec, Quelque chose s'est mal passé : " + str(e)
                messages.error(request, error_message)
                return redirect('post_task')
    return render(request, 'gestion/creation_tache.html', {'form': form})









