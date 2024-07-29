from rest_framework import serializers
from .models import Rating
class RatingSerializer(serializers.ModelSerializer):
    # owner_email = serializers.ReadOnlyField(source='owner.email')
    owner = serializers.ReadOnlyField(source='owner.email')
    product=serializers.ReadOnlyField(source='product.title')

    class Meta:
        model = Rating
        fields = '__all__'

