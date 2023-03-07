from django.db import models

# Create your models here.
class Task(models.Model):
    """Modello di un singolo task"""

    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Slot(models.Model):
    """Modello di un singolo slot"""

    title = models.CharField(max_length=200)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="slots")

    def __str__(self):
        return self.title