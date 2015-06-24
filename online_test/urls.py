from django.conf.urls import patterns, url



urlpatterns = patterns('online_test.views',
    url(r'^$', 'index', name='index'),
    url(r'online_test', 'online_test', name="online_test"),
    url(r'topics/', 'getTopics', name="topics"),
    url(r'about/', 'about', name="about"),
    url(r'check', 'check', name="check"),
    url(r'go', 'go', name="go"),
    url(r'result', 'get_profile', name="result"),
)


