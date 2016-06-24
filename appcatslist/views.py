from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView, UpdateView
from appcatslist.models import UserProfile
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loginform'] = AuthenticationForm()
        return context


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/accounts/profile/'


class ProfileView(UpdateView):
    model = UserProfile
    fields = ['userdescription', 'preferredcity']
    template_name = 'profile.html'
    success_url = reverse_lazy('profileview')

    def get_object(self, queryset=None):
        return self.request.user
