from rest_framework import serializers
from .models import Category, Subcategory, Product, Cart, CartItem

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'slug', 'image')
        
        
class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ('id', 'name','slug', 'image','subcategories')

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    subcategory = serializers.StringRelatedField()
    image_small = serializers.ImageField(read_only=True)
    image_medium = serializers.ImageField(read_only=True)
    image_large = serializers.ImageField(read_only=True)
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'price', 'image', 'image_small', 'image_medium', 
                  'image_large', 'category', 'subcategory')
    
    def get_image_small(self, obj):
        return obj.image.url if obj.image else None
    
    def get_image_medium(self, obj):
        return obj.image.url if obj.image else None
    
    def get_image_large(self, obj):
        return obj.image.url if obj.image else None

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = CartItem
        fields = ('id', 'product', 'quantity')
        
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()
    quantity = serializers.SerializerMethodField()
    
    class Meta:
        model = Cart
        fields = ('id', 'user', 'items', 'quantity', 'total')
    
    def get_total(self, obj):
        return sum(item.product.price * item.quantity for item in obj.items.all())
     
    def get_quantity(self, obj):
        return sum(item.quantity for item in obj.items.all())