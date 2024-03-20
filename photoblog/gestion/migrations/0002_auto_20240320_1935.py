from django.contrib.contenttypes.models import ContentType
from django.db import migrations
from django.contrib.auth.models import Permission

def gestion(apps, schema_migration):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    taskteam = Group.objects.get(name='taskteam')
    content_type = ContentType.objects.get_for_model(Permission)

    add_gestion, _ = Permission.objects.get_or_create(
        codename='add_gestion',
        content_type=content_type,
        defaults={'name': 'Permission pour ajouter une tache'}
    )

    delete_gestion, _ = Permission.objects.get_or_create(
        codename='delete_gestion',
        content_type=content_type,
        defaults={'name': 'Permission pour supprimer une tache'}
    )

    change_gestion, _ = Permission.objects.get_or_create(
        codename='change_gestion',
        content_type=content_type,
        defaults={'name': 'Permission pour modifier une tache'}
    )

    view_gestion, _ = Permission.objects.get_or_create(
        codename='view_gestion',
        content_type=content_type,
        defaults={'name': 'Permission pour voir une tache'}
    )

    taskteam.permissions.add(add_gestion, delete_gestion, change_gestion, view_gestion)

class Migration(migrations.Migration):
    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(gestion),
    ]
