
from django.shortcuts import render, get_object_or_404
from projects.models import Project


def index(request):
    #Same as list_posts; however, the order of the posts is based on the date.
    latest_Project_list = Project.objects.order_by('-pub_date')[:5]
    context = {'latest_project_list': latest_Project_list}
    return render(request, 'projects/index_bootstrap.html', context)

def list_Projects(request):
    Projects = Project.objects.all()
    context = {'Projects': Projects}
    return render(request, "Projects/list.html", context)

def show_Project(request, Project_id):
    project = get_object_or_404(Project, pk=Project_id)
    return render(request, 'Projects/show_Project.html', {'Project': Project})

def comment(request, Project_id):
    pass