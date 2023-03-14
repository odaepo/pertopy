from django.db import models

# Create your models here.
class Task(models.Model):
    """Modello di un singolo task"""

    title = models.CharField(max_length=200)
    description = models.TextField(default = " ")
    #status = models.CharField(choices=[("todo", "To Do"), ("doing", "Doing"), ("done", "Done")], default="todo")
    status = models.ForeignKey('Status', on_delete=models.CASCADE, related_name="tasks", null=True, blank=True)
    min = models.IntegerField(default=0)
    max = models.IntegerField(default=100)
    attuale = models.IntegerField(default=0)
    priorita = models.IntegerField(default=0)
    impotanza = models.IntegerField(default=0)
    minuti = models.IntegerField(default=0)
    contesto = models.ForeignKey('Contesto', on_delete=models.CASCADE, related_name="tasks", null=True, blank=True)
    scadenza = models.DateField(null=True, blank=True)






    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
class Contesto(models.Model):
    """Contesto di un task"""
    title = models.CharField(max_length=200)
    description = models.TextField(default = " ")

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']
        verbose_name = 'Contesto'
        verbose_name_plural = 'Contesti'
class TaskRtask(models.Model):
    """Definisce le relazioni (kind) fra Task (tra il PrentTask ed in childrenTask)"""

    title = models.CharField(max_length=200)
    description = models.TextField(default = " ")
    ptask = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="ptask", null=True, blank=True)
    ctask = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="ctask", null=True, blank=True)
    kind = models.CharField(choices=[("contiene", "contiene"), ("altro", "altro")], default="contiene",max_length=20)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']
        verbose_name = 'TaskRtask'
        verbose_name_plural = 'TaskRtasks'


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

class StatusRstatus(models.Model):
    """Definisce le transazioni da uno stato all'altro possibili"""
    fromStatus = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="fromStatus", null=True, blank=True)
    toStatus = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="toStatus", null=True, blank=True)



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

