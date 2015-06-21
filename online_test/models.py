# -*- coding: utf-8 -*-
from django.db import models
from django.core.files.storage import FileSystemStorage

quest_fss = FileSystemStorage(location='/media/images')
lect_fss = FileSystemStorage(location='/media/lectures')

class Topic(models.Model):
    name = models.CharField(u'Название', max_length=200)
    about = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Топик'
        verbose_name_plural = u'Топики'

class Question(models.Model):
    question = models.CharField(u'Вопрос', max_length=300)
    image = models.ImageField(u'Картинка', blank=True, upload_to='questions')
    answer1 = models.CharField(u'Ответ 1', max_length=40, blank=True)
    answer2 = models.CharField(u'Ответ 2', max_length=40, blank=True)
    answer3 = models.CharField(u'Ответ 3', max_length=40, blank=True)
    answer4 = models.CharField(u'Ответ 4', max_length=40, blank=True)
    correct_answer = models.CharField(u'Правильный ответ', max_length=40)
    topic = models.ForeignKey(Topic)

    def __unicode__(self):
        return self.question

    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'
    
class Lecture(models.Model):
    name = models.CharField(u'Название', max_length=200)
    lecture = models.FileField(u'Лекция', upload_to='lectures')
    topic = models.ForeignKey(Topic)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Лекция'
        verbose_name_plural = u'Лекции'