from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=40, unique=True)
    status = models.CharField(max_length=20)
    deadline_date = models.DateTimeField('deadline_date')
    added_date = models.DateTimeField('added_date')
    detail = models.TextField()

    def save(self, *args, **kwargs):
        a = super(Task, self).save(*args, **kwargs)
        print a, kwargs, args

        log = TaskLog(user=self.user,
                      task=self.title,
                      action="CREATE",
                      row_affected=1)
        log.save()

    def __str__(self): 
        return self.title


class TaskLog(models.Model):
    user = models.ForeignKey(User)
    task = models.CharField(max_length=100)
    action = models.CharField(max_length=20)
    row_affected = models.IntegerField()

    def __str__(self):
        if self.action == "CREATE":
            temp = "{task} was {action}d by you"
        if self.action in ['INCOMPLETE', 'COMPLETE']:
            if self.row_affected == 1:
                temp = "{task} task was marked {action} by you"
            else:
                temp = "{task} tasks were marked {action} by you"
        if self.action == "DELETE":
            if self.task == 1:
                temp = "{task} task was {action}d by you"
            else:
                temp = "{task} tasks were {action}d by you"

        return temp.format(task=self.task,
                           action=self.action.lower(),
                           user=self.user)
