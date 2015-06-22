# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import *
import random as random_number
from django.contrib.auth.decorators import login_required
import json

class Answer:
    def __init__(self, id, answer):
        self.id = id
        self.answer = answer

def index(request):
    return render(request, 'online_test/index.html')

def about(request):
    return render(request, 'online_test/about.html')

def sign_up_template(request):
    return render(request, 'registration/email_registration_include.html')

@login_required()
def online_test(request):
    topics = Topic.objects.all()
    context = {
        'questions': []
    }
    for topic in topics:
        questions = Question.objects.filter(topic=topic.id)
        context['questions'].append(random_number.choice(questions))
    return render(request, 'online_test/test.html', context)

@login_required()
def getTopics(request):
    topics = Topic.objects.all();
    context = {
        'topics': topics
    }
    for topic in context['topics']:
        lectures = Lecture.objects.filter(topic=topic.id)
        topic.__setattr__("lectures", lectures)
    return render(request, 'online_test/topics.html', context)

def check(request):
    if request.POST:
        data = request.POST['']
        print data
        # objs = json.loads(request.POST.decode('utf-8'))
        # for o in objs:
        #     record = Answer(o.id, o.value)
        #     record.save()
        # print record
        return HttpResponse("Отлично")
    else:
        return HttpResponse("Ошибка!")

def go(request):
    topics = Topic.objects.all()
    context = {
        'len': len(topics)
    }
    return render(request, 'online_test/go.html', context)
