from django.db import models

class TaskCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "task_category"


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(TaskCategory, null = True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = "tasks"
