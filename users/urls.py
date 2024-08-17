from django.urls import path

from users.views import logout_user, user_login, user_register


urlpatterns = [
    path('register/', user_register, name='user_register'),
    path('login/', user_login, name='user_login'),
    path('logout/', logout_user, name='logout_user'),
]