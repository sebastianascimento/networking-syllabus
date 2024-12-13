from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)  # Título da tarefa
    description = models.TextField(blank=True, null=True)  # Descrição opcional
    completed = models.BooleanField(default=False)  # Status da tarefa
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação

    def __str__(self):
        return self.title
