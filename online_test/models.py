from django.db import models
from django.core.files.storage import FileSystemStorage

quest_fss = FileSystemStorage(location='/media/images')
lect_fss = FileSystemStorage(location='/media/lectures')

class Topic(models.Model):
    name = models.CharField(max_length=40)
    about = models.TextField()
    def __unicode__(self):
        return self.name
    
class Question(models.Model):
    question = models.CharField(max_length=300)
    image = models.ImageField(blank=True, upload_to='questions')
    answer1 = models.CharField(max_length=40, blank=True)
    answer2 = models.CharField(max_length=40, blank=True)
    answer3 = models.CharField(max_length=40, blank=True)
    answer4 = models.CharField(max_length=40, blank=True);
    test = (
            ('A', answer1),
            ('B', answer2),
            ('C', answer3),
            ('D', answer4),
        )
    answer = models.CharField(max_length=40, blank=True, choices=test)
    correct_answer = models.CharField(max_length=40)
    topic = models.ForeignKey(Topic)
    def __unicode__(self):
        return self.question
    
class Lecture(models.Model):
    name = models.CharField(max_length=40)
    lecture = models.FileField(upload_to='lectures')
    topic = models.ForeignKey(Topic)
    def __unicode__(self):
        return self.name