from django.urls import path
from . import views

#add paths for url navigation 
app_name = 'records'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:candidate_id>/info/', views.candInfo, name='info'),
    path('<int:response_id>/results/', views.results, name='results'),
    path('input/', views.inputCand, name='input'),
    path('newData/', views.addData, name='addData')
]