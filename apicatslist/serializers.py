from rest_framework import serializers
from appcatslist.models import CategoryList, SubCategoryList, OfferPost


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryList


class SubCategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategoryList


class OfferPostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
                default=serializers.CurrentUserDefault()
                )

    class Meta:
        model = OfferPost
