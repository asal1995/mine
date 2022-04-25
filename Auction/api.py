from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import UpdateModelMixin, ListModelMixin


class AuctionView(ListModelMixin, GenericViewSet):
    serializer_class = AuctionSerializers
    queryset = Auction.objects.all()

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        print(type(self.get_serializer))
        return Response(serializer.data, status=status.HTTP_200_OK)
