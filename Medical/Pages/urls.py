from unicodedata import name
from winreg import QueryValue
from django.urls import path
from . import views
from .models import *

urlpatterns = [
    path('', views.basehome, name='basehome'),
    path('engineer/<int:id>/', views.Eengineer.eng_home, name='engineer'),
    path('engineer/<int:id>/services/upload', views.Eengineer.upload, name='eng_services'),
    path('engineer/<int:id>/services/thnx', views.Eengineer.thanks, name='thanks'),
    path('engineer/<int:id>/services/datasets', views.Eengineer.dataset, name='dataset'),
    path('engineer/<int:id>/services/datasets/<str:disease>', views.Eengineer.imagedata, name='imagedata'),
    path('doctor/<int:id>/', views.Ddoctor.doc_home, name='doctor'),
    path('doctor/<int:id>/check up', views.Ddoctor.check_up, name='check1'),
    path('doctor/<int:id>/check up/<str:disease>', views.Ddoctor.check_up, name='check2'),
    path('doctor/<int:id>/check up/<str:predict>/result', views.Ddoctor.result, name='result'),
    path('doctor/<int:id>/services/', views.Ddoctor.doctor, name='doc_services'),
    path('doctor/<int:id>/services/Bio analysis/', views.Ddoctor.Biophase, name='bio_analysis'),
    path('doctor/<int:id>/services/Bio analysis/<str:image>/', views.Ddoctor.bioAnalysis, name='bio_window'),
    path('login/', views.User.signIn, name='login'),
    path('error404/', views.error, name='error'),
    path('register/', views.User.signUp, name='register'),
    path('doctor/<int:id>/profile/', views.Ddoctor.doc_profile, name='doc_profile'),
    #path('doctor/<str:name>/profile/edit', views.dis_doc_profile, name='dis_doc_profile'),
    path('engineer/<int:id>/profile/', views.Eengineer.eng_profile, name='eng_profile'),
    path('engineer/<int:id>/<int:mod>/edit', views.Eengineer.edit_model, name='dis_eng_profile'),
]
