# TokenAuth
Authentication Token

# Project Description
The Project is all about setting a GET and POST request that requires an authentication which will 
generated via the the Django RestFrameWork Token Authentication API

# Modules
pip install django, restframewok

# Project/settings.py
Installed Apps:

    'quickstart',   ##appname
    'rest_framework',
    'rest_framework.authtoken',

then:

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
               'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES':(
                'rest_framework.permissions.IsAuthenticated',
    ),



    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}


# __Models, Serializer and Views.py ... see django DRF for more.

a A model, A serializer that serializes the object to converted to an API to get an instance.

Then a 



# Project/urls.py

from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views

then;

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('quickstart.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth')
] 

# Project/app/url.py

from django.urls import path
from . import views

urlpatterns=[
    path('', views.home_list, name='home_list' ),
    path('login/', views.CustomAuthToken.as_view())

]
    

# Running the Apllication

make necessary migrations
-python manage.py migrate
-python manage.py makemigrations
-python manage.py migrate
-python manage.py runserver

# PostMan
Use a postman application, run your application 

- follow the appropraite links

- to get Authentication Token
  https://authen.pythonanywhere.com/login/ - URL to login for and get TOKEN

Test/Login Credentials
Username: presh,
Password: presh12345

watch video for hints on how to use POSTMAN - https://youtu.be/rjiHHDvs8mE?si=eZOeh8pAwmm6gNH9

https://authen.pythonanywhere.com - URLs for the hosted GET 
Authen.pythonanywhere.com/post/ - URL for a POST request
Authen.pythonanywhere.com/getdetail/2 - URL for details [GET]

