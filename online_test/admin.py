from django.contrib import admin
from online_test.models import *

class QuestionAdmin(admin.ModelAdmin):
    list_display = [ 'question', 'topic']

class LectureAdmin(admin.ModelAdmin):
    list_display = ['name', 'topic']


admin.site.register(Topic)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Lecture, LectureAdmin)
