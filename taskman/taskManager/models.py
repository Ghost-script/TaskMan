from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=40,unique=True)
    status = models.CharField(max_length=20)
    deadline_date = models.DateTimeField('deadline_date')
    added_date = models.DateTimeField('added_date')
    
    detail = models.TextField()
    
    def __str__(self):              # __unicode__ on Python 2
        return self.title


class TaskLog(models.Model):
	task = models.ForeignKey(Task)
	action = models.CharField(max_length=20)

	def __str__(self):              # __unicode__ on Python 2
		return "{task} was {action} by you".format(task=self.task.title,action=self.action.lower(),user=self.task.user)