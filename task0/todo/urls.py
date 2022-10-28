from . import views
from django.urls import path

urlpatterns = [
    path('',views.loginpage, name='loginpage'),
    path('register/',views.registerpage, name='registerpage'),    
    path('func/',views.func ,name ='func'),
    path('func/<str:pk>', views.deletestuff, name='deletestuff'),
    path('func/update/<str:pk>', views.updatestuff, name='updatestuff'),
]