from rest_framework import serializers

from .models import *
from drf_writable_nested import WritableNestedModelSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "img"]

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ["id", "category_id", "name"]

class Img_for_instrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Img_for_instrument
        fields = ["instrument_id", "photo"]


class InstrumentsSerializer(WritableNestedModelSerializer , serializers.ModelSerializer):

    category = CategorySerializer(read_only=False)
    subcategory = SubcategorySerializer(read_only=False)

    class Meta:
        model = Instruments
        fields = ["article", "name", "price", "description", "characteristics", "category", "subcategory", "main_img"]
        

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
