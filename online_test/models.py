# -*- coding: utf-8 -*-
from django.db import models
from django.core.files.storage import FileSystemStorage

quest_fss = FileSystemStorage(location='/media/images')
lect_fss = FileSystemStorage(location='/media/lectures')

class Topic(models.Model):
    name = models.CharField(u'Название', max_length=200)
    about = models.TextField(
        u'Описание'
    )

    class Meta:
        verbose_name = u'Топик'
        verbose_name_plural = u'Топики'

    def __unicode__(self):
        return self.name


class Question(models.Model):
    question = models.CharField(u'Вопрос', max_length=300)
    image = models.ImageField(u'Картинка', blank=True, upload_to='questions')
    answer1 = models.ImageField(u'Ответ 1', upload_to='answers')
    answer2 = models.ImageField(u'Ответ 2', upload_to='answers')
    answer3 = models.ImageField(u'Ответ 3', upload_to='answers')
    answer4 = models.ImageField(u'Ответ 4', upload_to='answers')
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    choices = (
        (a, answer1),
        (b, answer2),
        (c, answer3),
        (d, answer4),
    )
    correct_answer = models.ImageField(u'Правильный ответ', choices=choices)
    topic = models.ForeignKey(Topic)

    class Meta:
        verbose_name = u'Воспрос'
        verbose_name_plural = u'Вопросы'

    def get_choices_value(self):
        return self.correct_answer

    def __unicode__(self):
        return self.question
    
class Lecture(models.Model):
    name = models.CharField(u'Название', max_length=200)
    lecture = models.FileField(u'Лекция', upload_to='lectures')
    topic = models.ForeignKey(Topic)

    class Meta:
        verbose_name = u'Лекция'
        verbose_name_plural = u'Лекции'

    def __unicode__(self):
        return self.name