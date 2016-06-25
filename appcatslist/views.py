from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from appcatslist.models import UserProfile, City, CategoryList, OfferPost, SubCategoryList
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loginform'] = AuthenticationForm()
        context['cities'] = City.objects.all()
        return context


# Post related Classes

class CityListingView(ListView):

    def get_context_data(self, **kwargs):
        city = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['items'] = OfferPost.objects.filter(city__pk=city)
        return context


# User related Classes


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/accounts/profile/'


class ProfileView(UpdateView):
    model = UserProfile
    fields = ['userdescription', 'preferredcity', 'photo']
    template_name = 'profile.html'
    success_url = reverse_lazy('profileview')

    def get_object(self, queryset=None):
        return self.request.user.userprofile


class UserProfileView(TemplateView):
    template_name = 'userprofile.html'

    def get_queryset(self):
        user = self.kwargs['username']
        print(user)
        return UserProfile.objects.get(user__username=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.kwargs['username']
        context['userinformation'] = UserProfile.objects.filter(user__username=user)
        context['listings'] = OfferPost.objects.filter(user__username=user)
        return context


class CityListView(ListView):
    template_name = 'citylistview.html'

    def get_queryset(self):
        city = self.kwargs['city']
        return OfferPost.objects.filter(city__city=city)

    def get_context_data(self, **kwargs):
        city = self.kwargs['city']
        item1 = CategoryList.objects.all()[0]
        print(item1)
        item2 = CategoryList.objects.all()[1]
        print(item2)
        itemslist = OfferPost.objects.filter(subcategory__category=item1)
        print(itemslist)
        context = super().get_context_data(**kwargs)
        context['allitems'] = OfferPost.objects.filter(city__city=city)
        context['subcategory'] = SubCategoryList.objects.all()
        context['items'] = OfferPost.objects.filter(city__city=city).filter(subcategory__category=item1)
        context['services'] = OfferPost.objects.filter(city__city=city).filter(subcategory__category=item2)
        return context
