from django import template
from users.forms import LoginForm

register = template.Library()


@register.simple_tag()
def get_login_form():
    return LoginForm()