from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField()

    created_by = models.ForeignKey(

        User,

        on_delete=models.CASCADE

    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name


class Task(models.Model):

    project = models.ForeignKey(

        Project,

        on_delete=models.CASCADE

    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    assigned_to = models.ForeignKey(

        User,

        on_delete=models.CASCADE

    )

    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title


class Comment(models.Model):

    task = models.ForeignKey(

        Task,

        on_delete=models.CASCADE

    )

    user = models.ForeignKey(

        User,

        on_delete=models.CASCADE

    )

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.text

class Notification(models.Model):
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
