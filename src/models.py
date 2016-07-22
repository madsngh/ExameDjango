from django.db import models
from django.contrib.auth.models import User

class Total(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    marks = models.IntegerField(null=True)
    def __str__(self):
        return str(self.user)

class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    correct_answer = models.CharField(max_length=50)
    def __str__(self):
        return self.correct_answer

class Question(models.Model):
    correct_answer = models.OneToOneField(
        Answer,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    question=models.CharField(max_length=40)

    def __str__(self):              # __unicode__ on Python 2
        return self.question

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option=models.CharField(max_length=20)
    def __str__(self):
        return self.option

class Marks(models.Model):
    positive_marks=models.IntegerField(blank=False)
    negevetive_marks=models.IntegerField(default=0)

    def __str__(self):
        return "MakringScheme"


class StoreUserAns(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ques_id = models.IntegerField(primary_key=True,default=0)
    subans = models.CharField(max_length=50,blank=True,null=True)
