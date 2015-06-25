# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from models import *
import random as random_number
from django.contrib.auth.decorators import login_required
from account.models import UserProfile
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    res = UserProfile.objects.all().order_by('result').reverse()
    context = {
        'result': res[0].result,
        'user': res[0].user
    }

    return render(request, 'online_test/index.html', context)


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
        if len(questions):
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


# @csrf_protect
def check(request):
    if request.POST:
        data = dict(request.POST.lists())
        q_kol = 0
        c_kol = 0
        e_kol = 0
        for key in data:
            if key.isdigit():
                q_kol += 1
                user_answer = data[key][0].encode('ascii', 'ignore')
                question = Question.objects.get(id=key)
                if user_answer == question.get_choices_value():
                    c_kol += 1
                else:
                    e_kol += 1
        user = User.objects.get(username=request.user.get_username())
        result = str(c_kol * 100 / q_kol)
        try:
            profile = UserProfile.objects.get(user=user)
            profile.result = result
            profile.save()
        except ObjectDoesNotExist:
            profile = UserProfile.objects.create(user=user, result=result)
            profile.save()
        return redirect('result')


@login_required()
def go(request):
    topics = Topic.objects.all()
    context = {
        'len': len(topics)
    }
    return render(request, 'online_test/go.html', context)


@login_required()
def get_profile(request):
    user = User.objects.get(username=request.user.get_username())
    try:
        profile = UserProfile.objects.get(user=user)
    except ObjectDoesNotExist:
        profile = UserProfile.objects.create(user=user)
        profile.save()
    # print profile.user.email
    return render(request, 'online_test/result.html', {'result': profile})





