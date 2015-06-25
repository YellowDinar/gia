from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from gia import settings
from account.views import MyRegistrationView

urlpatterns = patterns('',
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'next_page': 'result'}, name='auth_login'),
    # url(r'^accounts/login/(?P<next_page>.*)/$', 'django.contrib.auth.views.login', name='auth_login_next'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': 'index'}, name='auth_logout'),
    url(r'^accounts/logout/(?P<next_page>.*)/$', 'django.contrib.auth.views.logout', name='auth_logout_next'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('online_test.urls')),
    url(r'^account/', include('account.urls')),

)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()