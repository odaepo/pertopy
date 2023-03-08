from django.db import models

# Create your models here.
class Task(models.Model):
    """Modello di un singolo task"""

    title = models.CharField(max_length=200)
    #status = models.ChoicesField(choices=[("todo", "To Do"), ("doing", "Doing"), ("done", "Done")], default="todo")

    def __str__(self):
        return self.title

class Status(models.Model):
    """Modello di uno stato"""

    title = models.CharField(max_length=200)
    description = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="statuses")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="children", null=True, blank=True)

    def __str__(self):
        return self.title
class Slot(models.Model):
    """Modello di un singolo slot"""

    title = models.CharField(max_length=200)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="slots")

    def __str__(self):
        return self.title

