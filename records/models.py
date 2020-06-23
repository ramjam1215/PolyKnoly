from django.db import models
import datetime
from django.utils import timezone

#Information/Resources
# Create your models here.
# https://docs.djangoproject.com/en/3.0/topics/db/
#https://docs.djangoproject.com/en/3.0/intro/tutorial02/




# Create your models here.
class Candidate(models.Model):

    #Data
    # --------------------------------------------------------------- 
    name = models.CharField(max_length=50)
    office = models.CharField(max_length=50)
    pol_party = models.CharField(max_length=20)
    #image store binary data? bytea? need to look for more info
    #race = models.CharField(max_length=20)
    #----------------------------------------------------------------
    #Methods
    def __str__(self):
        return self.name
    # --------------------------------------------------------------- 

class Question(models.Model):
    #Data
    # --------------------------------------------------------------- 
    question_text = models.CharField(max_length=200)
    # --------------------------------------------------------------- 

    #Methods
    def __str__(self):
        return self.question_text
    # --------------------------------------------------------------- 

class Response(models.Model):

    #Data
    # --------------------------------------------------------------- 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    response_text = models.CharField('response', max_length=200)
    pub_date = models.DateTimeField('date published')
    # --------------------------------------------------------------- 

    #Methods
    def __str__(self):
        return self.response_text
    # --------------------------------------------------------------- 
