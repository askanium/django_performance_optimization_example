from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from houses.models import House, Country
from houses.serializers import HouseSerializer
from utils.hash import Hasher


class HouseListAPIView(ListAPIView):
    model = House
    serializer_class = HouseSerializer
    country = None

    def get_queryset(self):
        country = get_object_or_404(Country, pk=self.country)
        queryset = self.model.objects.filter(country=country)
        return queryset

    def list(self, request, *args, **kwargs):
        # Validation code to check for `country` param should be here
        country = self.request.GET.get("country")

        self.country = Hasher.to_object_pk(country)
        queryset = self.get_queryset()

        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)