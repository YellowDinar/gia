import random as random_number
from django.shortcuts import render
from models import *
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'online_test/index.html')

def about(request):
    return render(request, 'online_test/about.html')

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
    topics = Topic.objects.all()
    context = {
        'topics': topics
    }
    for topic in context['topics']:
        lectures = Lecture.objects.filter(topic=topic.id)
        topic.__setattr__("lectures", lectures)
    return render(request, 'online_test/topics.html', context)
