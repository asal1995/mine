from rest_framework import serializers
from User.models import Bider
from khodro45_app.models import Auction, Brand, Bid


class AuctionSerializers(serializers.ModelSerializer):
    # bider = serializers.SerializerMethodField()

    class Meta:
        model = Auction
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        bidder = Bid.objects.filter(auction=instance.id)
        bid_serilizare = BidSerializer(bidder, many=True)
        representation['bider'] = bid_serilizare.data
        return representation

    # def get_bider(self, instance):
    #     bidder = instance.winner.all()
    #     # bidder = Bid.objects.filter(auction=instance.id)
    #     bid_serilizare = BidSerializer(bidder, many=True)
    #     return bid_serilizare.data
