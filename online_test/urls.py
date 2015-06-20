from django.conf.urls import patterns, include, url



urlpatterns = patterns('online_test.views',
    url(r'^$', 'index', name='index'),
    url(r'email_registration', include('email_registration.urls')),
    url(r'sign_up', 'sign_up_template'),
    url(r'online_test', 'online_test', name="online_test"),
    url(r'topics/', 'getTopics', name="topics"),
    url(r'about/', 'about', name="about"),
)


