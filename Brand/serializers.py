from rest_framework import serializers
from User.models import Bider
from khodro45_app.models import Auction, Brand, Bid


class BrandListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='brand-detail', format=None)

    class Meta:
        model = Brand
        fields = ['id', 'title', 'created_time', 'url']

    def to_internal_value(self, data):
        title = data.get('title')
        if len(title) > 10:
            raise serializers.ValidationError({
                'title': 'May not be more than 10 characters.'})
        return {'title': title}


class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


serializer = BrandDetailSerializer()
print(repr(serializer))


class BrandUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['title', 'created_time']
        extra_kwargs = {
            'created_time': {'read_only': True}
        }


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['bider'] = instance.bider.username

        return representation


