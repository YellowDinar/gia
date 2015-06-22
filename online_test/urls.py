from django.conf.urls import patterns, include, url



urlpatterns = patterns('online_test.views',
    url(r'^$', 'index', name='index'),
    url(r'online_test', 'online_test', name="online_test"),
    url(r'topics/', 'getTopics', name="topics"),
    url(r'about/', 'about', name="about"),
)


