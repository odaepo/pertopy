from django.db import models

# Create your models here.
class Task(models.Model):
    """Modello di un singolo task"""

    title = models.CharField(max_length=200)
    description = models.TextField(default = " ")
    #status = models.CharField(choices=[("todo", "To Do"), ("doing", "Doing"), ("done", "Done")], default="todo")
    status = models.ForeignKey('Status', on_delete=models.CASCADE, related_name="tasks", null=True, blank=True)



    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class Status(models.Model):
    """Modello di uno stato"""

    title = models.CharField(max_length=200)
    description = models.TextField()
    #task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="statuses")
    children = models.ManyToManyField('self', blank=True, symmetrical=False)

    #descrive la tipologia di stato.
    kind = models.CharField(choices=[ ("start", "start"),("incorso", "incorso"), ("installo", "installo"), ("annullata", "annullata"), ("end", "end")], default="incorso",max_length=20)

    def getNextStatues(self,id):
        return Status.objects.filter(children=id)

    def __str__(self):
        return self.title


class Slot(models.Model):
    """Modello di un singolo slot"""

    title = models.CharField(max_length=200)
    description = models.TextField(default = " ")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="slots", null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="slots", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Slot'
        verbose_name_plural = 'Slots'

