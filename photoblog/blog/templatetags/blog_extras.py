from django.utils.timezone import now
from django import template
register=template.Library()

@register.filter
def model_type(instance):
    return type(instance).__name__


@register.simple_tag(takes_context=True)
def get_poster_display(context,user):
    if user == context['user']:return 'Vous'
    return user.username

@register.simple_tag(takes_context=True)
def get_posted_at_display(context,time):
    time_now=now()
    delta=time_now-time
    if delta.total_seconds()<3600:
        minutes=int(delta.total_seconds()/60)
        return f"Posté il y a {minutes} minutes"
    elif delta.total_seconds()<3600*24:
        heures=int(delta.total_seconds()/3600)
        return f"Posté il y a {minutes} minutes"
    else:
        return time.strftime('Posté à %H:%M:%S %Y-%m-%d ')


