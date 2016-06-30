from django.shortcuts import render
from rest_framework import generics
from appcatslist.models import CategoryList, SubCategoryList, OfferPost
from apicatslist.serializers import CategoryListSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = CategoryList.objects.all()
    serializer_class = CategoryListSerializer
