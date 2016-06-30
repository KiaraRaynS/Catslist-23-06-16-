from django.shortcuts import render
from rest_framework import generics
from appcatslist.models import CategoryList, SubCategoryList, OfferPost
from apicatslist.serializers import CategoryListSerializer, SubCategoryListSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = CategoryList.objects.all()
    serializer_class = CategoryListSerializer


class CategoryListDetailAPIView(generics.RetrieveAPIView):
    queryset = CategoryList.objects.all()
    serializer_class = CategoryListSerializer


class SubCategoryListAPIView(generics.ListAPIView):
    queryset = SubCategoryList.objects.all()
    serializer_class = SubCategoryListSerializer


class SubCategoryListDetailAPIView(generics.RetrieveAPIView):
    queryset = SubCategoryList.objects.all()
    serializer_class = SubCategoryListSerializer
