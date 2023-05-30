from django.urls import path
from hospital.views import Home, About, Contact, Login,Logout,Register
urlpatterns = [
    path('', Home ,name ='home'),
    path('about/', About, name = 'about'),
    path('contact/', Contact, name = 'contact'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('register/',Register, name='register')
]