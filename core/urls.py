from django.urls import path

from . import views


urlpatterns = [

    path('', views.home),

    path('project/<int:id>/', views.project_detail),

    path('create-project/', views.create_project),

    path('create-task/<int:id>/', views.create_task),

    path('comment/<int:id>/', views.add_comment),

    path('notifications/', views.notifications, name='notifications'),

]