from django import forms

STATUT = (
    ('EN_COURS', 'En cours'),
    ('FINI', 'Fini'),
    ('STOPE', 'Stopé'),
    ('EN_ATTENTE', 'En attente'),
)

PRIORITE = (
    ('HAUTE', 'Haute'),
    ('MOYENNE', 'Moyenne'),
    ('FAIBLE', 'Faible'),
)


class CreateTask(forms.Form):
    # auteur=forms.CharField(max_length=30)
    titre=forms.CharField(max_length=30)
    description=forms.CharField(max_length=100)
    statut=forms.ChoiceField(choices=STATUT,widget=forms.Select(attrs={'class': 'form-control'}))
    priorite=forms.ChoiceField(choices=PRIORITE,widget=forms.Select(attrs={'class': 'form-control'}))
    commentaire=forms.CharField(max_length=100,required=False)
    date_echeance=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_debut=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_fin=forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date'}))


