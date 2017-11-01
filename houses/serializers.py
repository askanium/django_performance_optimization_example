from rest_framework import serializers

from houses.models import House, Country
from utils.hash import Hasher


class HouseSerializer(serializers.ModelSerializer):
    """Serialize a `houses.House` instance."""

    id = serializers.ReadOnlyField(source="hash")
    country = serializers.ReadOnlyField(source="country.hash")

    class Meta:
        model = House
        fields = (
            'id',
            'address',
            'country',
            'sq_meters',
            'price'
        )
