from django.shortcuts import render, redirect

from .models import Project, Task, Comment

from django.contrib.auth.models import User

from .models import Notification

from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()

    return render(request, 'index.html', {
        'projects': projects
    })


def create_project(request):

    if request.method == 'POST':

        name = request.POST.get('name')

        description = request.POST.get('description')

        user = User.objects.first()

        Project.objects.create(

            name=name,

            description=description,

            created_by=user

        )

        Notification.objects.create(
    message="New task created!"
)

        return redirect('/')

    return render(request, 'create_project.html')


def project_detail(request, id):

    project = Project.objects.get(id=id)

    tasks = Task.objects.filter(project=project)

    return render(

        request,

        'project_detail.html',

        {

            'project': project,

            'tasks': tasks

        }

    )


def create_task(request, id):

    project = Project.objects.get(id=id)

    if request.method == 'POST':

        title = request.POST.get('title')

        description = request.POST.get('description')

        user = User.objects.first()

        Task.objects.create(

            project=project,

            title=title,

            description=description,

            assigned_to=user

        )

        Notification.objects.create(
    message="New task created!"
)

        return redirect(f'/project/{id}/')

    return render(

        request,

        'create_task.html',

        {

            'project': project

        }

    )


def add_comment(request, id):

    task = Task.objects.get(id=id)

    if request.method == 'POST':

        text = request.POST.get('text')

        user = User.objects.first()

        Comment.objects.create(

            task=task,

            user=user,

            text=text

        )

    return redirect(f'/project/{task.project.id}/')

def notifications(request):
    notes = Notification.objects.all().order_by('-created_at')

    return render(request, 'notifications.html', {
        'notes': notes
    })