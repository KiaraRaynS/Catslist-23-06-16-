"""projectcastlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import logout, login
from django.conf import settings
from django.conf.urls.static import static
from appcatslist.views import IndexView, RegisterView, ProfileView, CityListView, UserProfileView, PostDetailView
from appcatslist.views import NewPostCategory, NewPostSubCategory, NewPostFinal, CityCategoryListView, CitySubCategoryListView
from appcatslist.views import SubCategorySortPriceDesc, SubCategorySortPriceAsc, SubCategorySortDateThumbView, SubCategorySortPriceAscThumbView
from appcatslist.views import SubCategorySortPriceDescThumbView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='indexview'),
    url(r'logout/$', logout, name='logout'),
    url(r'login/$', login, name='login'),
    url(r'^register/$', RegisterView.as_view(), name='registerview'),
    # User Edit Profile View
    url(r'^accounts/profile/$', ProfileView.as_view(), name='profileview'),
    # View User Profile Details
    url(r'profiledetails/(?P<username>\w+)/$', UserProfileView.as_view(), name='userprofileview'),
    # View Cities
    url(r'^cities/(?P<city>\w+)/$', CityListView.as_view(), name='citylistview'),
    url(r'^cities/(?P<city>\w+)/(?P<category>\w+)/$', CityCategoryListView.as_view(), name='citycategorylistview'),
    url(r'^cities/(?P<city>\w+)/(?P<category>\w+)/(?P<subcategory>\w+)/$', CitySubCategoryListView.as_view(), name='citysubcategorylistview'),
    # Sort subcategory list
    url(r'^cities/(?P<city>\w+)/(?P<category>\w+)/(?P<subcategory>\w+)/sort/pricedesc/$', SubCategorySortPriceDesc.as_view(), name='subcategorysortpricedesc'),
    url(r'^cities/(?P<city>\w+)/(?P<category>\w+)/(?P<subcategory>\w+)/sort/priceasc/$', SubCategorySortPriceAsc.as_view(), name='subcategorysortpriceasc'),
    # Thumbnail view
    url(r'^cities/(?P<city>\w+)/(?P<category>\w+)/(?P<subcategory>\w+)/thumbview/$', SubCategorySortDateThumbView.as_view(), name='subcategorysortdatethumbview'),
    url(r'^cities/(?P<city>\w+)/(?P<category>\w+)/(?P<subcategory>\w+)/sort/pricedesc/thumbview/$', SubCategorySortPriceAscThumbView.as_view(), name='offerpostpricedescthumbview'),
    url(r'^cities/(?P<city>\w+)/(?P<category>\w+)/(?P<subcategory>\w+)/sort/priceasc/thumbview/$', SubCategorySortPriceDescThumbView.as_view(), name='offerpostpriceascthumbview'),
    # Make New Post
    url(r'^newpost/$', NewPostCategory.as_view(), name='newpostcategory'),
    url(r'^newpost/(?P<category>\w+)/$', NewPostSubCategory.as_view(), name='newpostsubcategory'),
    url(r'^newpost/(?P<category>\w+)/(?P<subcategory>\w+)/$', NewPostFinal.as_view(), name='newpostfinal'),
    url(r'^postdetail/(?P<pk>\d+)/$', PostDetailView.as_view(), name='postdetailview')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
