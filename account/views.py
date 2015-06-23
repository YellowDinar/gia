# # -*- coding: utf-8 -*-
from registration.backends.simple.views import RegistrationView
from django.contrib.auth import views as auth_views

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return 'index'