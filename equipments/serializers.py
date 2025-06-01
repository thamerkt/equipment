from rest_framework import serializers
from .models import (
    Stuff, Category, StuffManagement, Review, EquipmentImage, test,
    Visitor, ItemView, CartActivity, Rental,
    SiteStat, TrafficSource, DeviceStat, CategoryStat,Favorite
)

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class StuffManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StuffManagement
        fields = '__all__'

class StuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stuff
        fields = '__all__'
class WishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = test
        fields = '__all__'

class EquipmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentImage
        fields = ['id', 'stuff', 'url', 'alt', 'position']

# ======================= New Serializers =======================

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = '__all__'
        read_only_fields = ('first_visit', 'last_visit')

class ItemViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemView
        fields = '__all__'
        read_only_fields = ('timestamp',)

class CartActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CartActivity
        fields = '__all__'
        read_only_fields = ('timestamp',)

    


class RentalSerializer(serializers.ModelSerializer):
    duration = serializers.ReadOnlyField()
    
    class Meta:
        model = Rental
        fields = '__all__'

class SiteStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteStat
        fields = '__all__'

class TrafficSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficSource
        fields = '__all__'

class DeviceStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceStat
        fields = '__all__'

class CategoryStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryStat
        fields = '__all__'
