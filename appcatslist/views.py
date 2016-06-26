from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView
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


class PostDetailView(DetailView):
    model = OfferPost

    def get_object(self):
        post = self.kwargs['pk']
        return OfferPost.objects.get(id=post)


class NewPostCategory(TemplateView):
    template_name = 'categoryselect.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryList.objects.all()
        return context


class NewPostSubCategory(TemplateView):
    template_name = 'subcategoryselect.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.kwargs['category']
        context['subcategories'] = SubCategoryList.objects.filter(category__category=category)
        return context


class NewPostFinal(CreateView):
    success_url = '/'
    model = OfferPost
    fields = ['title', 'description', 'price', 'city', 'photo']

    def form_valid(self, form):
        offerpost = form.save(commit=False)
        offerpost.user = self.request.user
        subcategoryname = self.kwargs['subcategory']
        subcategory = SubCategoryList.objects.get(subcategory=subcategoryname)
        offerpost.subcategory = subcategory
        return super().form_valid(form)


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
        context = super().get_context_data(**kwargs)
        context['city'] = City.objects.get(city=city)
        context['categories'] = CategoryList.objects.all()
        return context
        """
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
        """
        return context


class CityCategoryListView(TemplateView):
    template_name = 'citycategorylistview.html'

    def get_context_data(self, **kwargs):
        city = self.kwargs['city']
        categoryitem = self.kwargs['category']
        category = CategoryList.objects.get(category=categoryitem)
        context = super().get_context_data(**kwargs)
        context['city'] = City.objects.get(city=city)
        context['subcategories'] = SubCategoryList.objects.filter(category=category)
        return context


class CitySubCategoryListView(TemplateView):
    template_name = 'citysubcategorylistview.html'

    def get_context_data(self, **kwargs):
        citykey = self.kwargs['city']
        city = City.objects.get(city=citykey)
        categorykey = self.kwargs['category']
        category = CategoryList.objects.get(category=categorykey)
        subcategorykey = self.kwargs['subcategory']
        subcategory = SubCategoryList.objects.get(subcategory=subcategorykey)
        context = super().get_context_data(**kwargs)
        context['city'] = City.objects.get(city=city)
        context['category'] = CategoryList.objects.get(category=category)
        context['subcategory'] = SubCategoryList.objects.get(subcategory=subcategory)
        context['listings'] = OfferPost.objects.filter(subcategory=subcategory).order_by('-date')
        return context


class SubCategorySortPriceDesc(TemplateView):
    template_name = 'subcategorysortviewdesc.html'

    def get_context_data(self, **kwargs):
        citykey = self.kwargs['city']
        city = City.objects.get(city=citykey)
        categorykey = self.kwargs['category']
        category = CategoryList.objects.get(category=categorykey)
        subcategorykey = self.kwargs['subcategory']
        subcategory = SubCategoryList.objects.get(subcategory=subcategorykey)
        context = super().get_context_data(**kwargs)
        context['city'] = City.objects.get(city=city)
        context['category'] = CategoryList.objects.get(category=category)
        context['subcategory'] = SubCategoryList.objects.get(subcategory=subcategory)
        context['listing'] = OfferPost.objects.filter(subcategory=subcategory).order_by('-price')
        return context


class SubCategorySortPriceAsc(TemplateView):
    template_name = 'subcategorysortviewasc.html'

    def get_context_data(self, **kwargs):
        citykey = self.kwargs['city']
        city = City.objects.get(city=citykey)
        categorykey = self.kwargs['category']
        category = CategoryList.objects.get(category=categorykey)
        subcategorykey = self.kwargs['subcategory']
        subcategory = SubCategoryList.objects.get(subcategory=subcategorykey)
        context = super().get_context_data(**kwargs)
        context['city'] = City.objects.get(city=city)
        context['category'] = CategoryList.objects.get(category=category)
        context['subcategory'] = SubCategoryList.objects.get(subcategory=subcategory)
        context['listing'] = OfferPost.objects.filter(subcategory=subcategory).order_by('price')
        return context


class SubCategorySortDateGalleryView(TemplateView):
    template_name = 'subcategorysortdatethumbview.html'

    def get_context_data(self, **kwargs):
        citykey = self.kwargs['city']
        city = City.objects.get(city=citykey)
        categorykey = self.kwargs['category']
        category = CategoryList.objects.get(category=categorykey)
        subcategorykey = self.kwargs['subcategory']
        subcategory = SubCategoryList.objects.get(subcategory=subcategorykey)
        context = super().get_context_data(**kwargs)
        context['city'] = City.objects.get(city=city)
        context['category'] = CategoryList.objects.get(category=category)
        context['subcategory'] = SubCategoryList.objects.get(subcategory=subcategory)
        context['offerposts'] = OfferPost.objects.filter(subcategory=subcategory)
        return context


class SubCategorySortPriceAscGalleryView(TemplateView):
    template_name = 'subcategorysortpriceascthumbview.html'

    def get_context_data(self, **kwargs):
        citykey = self.kwargs['city']
        categorykey = self.kwargs['category']
        subcategorykey = self.kwargs['subcategory']
        subcategory = SubCategoryList.objects.get(subcategory=subcategorykey)
        context = super().get_context_data(**kwargs)
        context['city'] = City.objects.get(city=citykey)
        context['category'] = CategoryList.objects.get(category=categorykey)
        context['subcategory'] = SubCategoryList.objects.get(subcategory=subcategorykey)
        context['offerposts'] = OfferPost.objects.filter(subcategory=subcategory)
        return context


class SubCategorySortPriceDescGalleryView(TemplateView):
    template_name = 'subcategorysortpricedescthumbview.html'

    def get_context_data(self, **kwargs):
        citykey = self.kwargs['city']
        categorykey = self.kwargs['category']
        subcategorykey = self.kwargs['subcategory']
        subcategory = SubCategoryList.objects.get(subcategory=subcategorykey)
        context = super().get_context_data(**kwargs)
        context['city'] = City.objects.get(city=citykey)
        context['category'] = CategoryList.objects.get(category=categorykey)
        context['subcategory'] = SubCategoryList.objects.get(subcategory=subcategory)
        context['offerpost'] = OfferPost.objects.filter(subcategory=subcategory)
        return context
