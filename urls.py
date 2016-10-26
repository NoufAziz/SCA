from django.conf.urls import url
from projects import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #/StudentsClubAcademy
    url(r'^$', views.list_Projects, name='list_Projects'),
    #/StudentsClubAcademy/Project/1/
    url(r'^(?P<Project_id>\d+)/$', views.show_Project, name='show_Projects'),
    #/StudentsClubAcademy/Project/1/comment/
    url(r'^(?P<Project_id>\d+)/comment/$', views.comment, name='comment'),
]
