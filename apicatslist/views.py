from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, filters
from appcatslist.models import CategoryList, SubCategoryList, OfferPost
from apicatslist.serializers import CategoryListSerializer, SubCategoryListSerializer, OfferPostSerializer


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


class OfferPostListAPIView(generics.ListAPIView):
    queryset = OfferPost.objects.all()
    serializer_class = OfferPostSerializer


class OfferPostDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = OfferPost.objects.all()
    serializer_class = OfferPostSerializer


class OfferPostBySubCategoryListAPIView(generics.ListAPIView):
    serializer_class = OfferPostSerializer

    def get_queryset(self):
        subcategory = self.kwargs['pk']
        return OfferPost.objects.filter(subcategory__id=subcategory)


class OfferPostByCategoryListAPIView(generics.ListAPIView):
    serializer_class = OfferPostSerializer

    def get_queryset(self):
        category = self.kwargs['pk']
        return OfferPost.objects.filter(subcategory__category=category)
