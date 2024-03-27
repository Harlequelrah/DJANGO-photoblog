from django.shortcuts import render,redirect
import httpx
from django.contrib import messages
from . import crud,forms
from django.contrib.auth.decorators import login_required,permission_required
server='http://localhost:8080/taches'

@login_required

@permission_required('auth.view_gestion',raise_exception=True)
def display_tasks(request,id):
    numberform=forms.NumberForm()
    if request.method=='POST' and 'search' in request.POST:
            numberform=forms.NumberForm(request.POST)
            if numberform.is_valid():
                id=numberform.cleaned_data['identifiant']
                return redirect('get_tasks',id)
    if request.method=='POST' and   'supp' in request.POST:
                api_url = server + '/taches/delete-task/'+id
                try:
                    with httpx.Client() as client:
                        response=client.delete(api_url)
                    if response.status_code==200:
                        messages.success(request, 'Tache supprimée avec succès')
                    else:
                        messages.error(request, 'Echec lors de la suppression de la tache')
                    return redirect('get_tasks','0')
                except httpx.HTTPError as e:
                        error_message = "Echec, Quelque chose s'est mal passé : " + str(e)
                        messages.error(request, error_message)
                        return redirect('get_tasks','0')
    if id=='0':
        tasks=crud.get_tasks()
    if id!='0':
        task=crud.get_task(id)
        tasks=[]
        tasks.append(task)
    if tasks[0] :
        if len(tasks)!=1:
            tasks.sort(key=lambda x: x['id'])
    else:
        messages.error(request,'La tâche n \' a pas été trouvée')
        return redirect('get_tasks','0')
    key=crud.ordered(tasks)
    current_url=request.path
    # new_id=current_url[-2]
    # if request.method=='GET':
    #     print(current_url,new_id,id)
    #     if id!=new_id: return redirect('get_tasks',id)
    return render(request,'gestion/affichage_taches.html',context={'tasks':tasks,'key':key,'form':numberform,'id':id})



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
                    return redirect('get_tasks','0')
                else:
                    messages.error(request, 'Echec lors de la création de la tache')
                    return redirect('post_task')
            except httpx.HTTPError as e:
                error_message = "Echec, Quelque chose s'est mal passé : " + str(e)
                messages.error(request, error_message)
                return redirect('post_task')
    return render(request, 'gestion/creation_tache.html', {'form': form})


@login_required
@permission_required('auth.change_gestion', raise_exception=True)
def change_task(request,id):
    initial_data=crud.get_task(id)
    # print(initial_data['auteur'])
    form = forms.UpdateTask(initial=initial_data)
    if request.method == 'POST':
        form = forms.UpdateTask(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['date_echeance']:
                data['date_echeance'] = data['date_echeance'].isoformat()
            if data['date_debut']:
                data['date_debut'] = data['date_debut'].isoformat()
            if data.get('date_fin'):
                data['date_fin'] = data['date_fin'].isoformat()
            api_url=server+"/taches/update-task/"+id
            try:
                # Utilisation de httpx pour envoyer une requête PUT
                response = httpx.put(api_url, json=data)
                if response.status_code == 200:
                    messages.success(request, 'La tâche a été mise à jour avec succès')
                    return redirect('get_tasks',id)
                else:
                    messages.error(request, 'Échec lors de la mise a jour de la tâche')
                    return redirect('get_tasks','0')
            except httpx.HTTPError as e:
                error_message = "Échec, Quelque chose s'est mal passé : " + str(e)
                messages.error(request, error_message)
                return redirect('get_tasks',id)
    return render(request, 'gestion/creation_tache.html', {'form': form,'id':id})








