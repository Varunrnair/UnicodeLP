from . import views
from django.urls import path

urlpatterns = [
    path('',views.func ,name ='func'),
    path('<str:pk>', views.deletestuff, name='deletestuff'),
    path('update/<str:pk>', views.updatestuff, name='updatestuff'),
]