from django.db import models
import datetime
from django.utils import timezone

from polyknoly.resources.staticStuff import POL_PARTY_CHOICES, ANSWERS

#Information/Resources

# https://docs.djangoproject.com/en/3.0/topics/db/
# https://docs.djangoproject.com/en/3.0/intro/tutorial04/
# Models and DB 

# 'blank' => determines if field is required in a form
    # True means its not required
    # False is required


# Create your models here.
class Candidate(models.Model):

    #Data
    # --------------------------------------------------------------- 
    fname = models.CharField(max_length=200, null=True, blank=True, verbose_name='First Name')
    lname = models.CharField(max_length=200, null=True, blank=False, verbose_name='Last Name')
    pol_office = models.CharField(max_length=200, null=True, blank=True, verbose_name='Political Office')
    pol_party = models.CharField(max_length=200, null=True, blank=True, choices=POL_PARTY_CHOICES, verbose_name="Political Party")
    link = models.CharField(max_length=200, null=True, blank=True, verbose_name='Link to Page')
    #image store binary data? bytes? need to look for more info
    #----------------------------------------------------------------
    #Methods
    def __str__(self):
        return "{1}, {0}".format(self.fname, self.lname)
         
    # --------------------------------------------------------------- 

class Question(models.Model):
    #Data
    # --------------------------------------------------------------- 
    question_text = models.CharField(max_length=200, verbose_name='Question')
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
    response_text = models.CharField('response', max_length=200, blank=True, null=True)
    answer = models.CharField(max_length=5, null=True, blank=True, choices=ANSWERS)
    pub_date = models.DateTimeField(default=timezone.now, verbose_name='date published')
    # --------------------------------------------------------------- 

    #Methods
    def __str__(self):
        return self.response_text
    # --------------------------------------------------------------- 
