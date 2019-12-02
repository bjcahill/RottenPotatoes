from django import template

from users.models import Usermodel

register = template.Library()

@register.filter(name='to_int')
def to_int(value):
    return int(value)

@register.filter(name='get_user_name')
def get_user_name(user):
    usermodel = Usermodel.objects.get(user_id=user.id)

    if usermodel != None:
        return usermodel.user_name
    else:
        return "Unknown User"

@register.filter(name='round_movie_score')
def round_movie_score(value):
    return str(round(value, 1))
    
