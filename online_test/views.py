from django.shortcuts import render
from django.http import HttpResponse
from models import *
from reportlab.pdfgen import canvas
from io import BytesIO
from gia import settings
import random as random_number

def index(request):
    return render(request, 'online_test/index.html')

def about(request):
    return render(request, 'online_test/about.html')

def sign_up_template(request):
    return render(request, 'registration/email_registration_include.html')

def online_test(request):
    topics = Topic.objects.all()
    context = {
        'questions': []
    }
    for topic in topics:
        questions = Question.objects.filter(topic=topic.id)
        context['questions'].append(random_number.choice(questions))
    return render(request, 'online_test/test.html', context)

def getTopics(request):
    topics = Topic.objects.all();
    context = {
        'topics': topics
    }
    for topic in context['topics']:
        lectures = Lecture.objects.filter(topic=topic.id)
        topic.__setattr__("lectures", lectures)
    return render(request, 'online_test/topics.html', context)
