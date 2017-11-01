from django.db import models

from utils.hash import Hasher


class HashableModel(models.Model):
    """Provide a hash property for models."""
    class Meta:
        abstract = True

    @property
    def hash(self):
        return Hasher.from_model(self)


class Country(HashableModel):
    """Represent a country in which the house is positioned."""
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class House(HashableModel):
    """Represent a house with its characteristics."""

    # Relations
    country = models.ForeignKey(Country, related_name='houses')

    # Attributes
    address = models.CharField(max_length=255)
    sq_meters = models.PositiveIntegerField()
    kitchen_sq_meters = models.PositiveSmallIntegerField()
    nr_bedrooms = models.PositiveSmallIntegerField()
    nr_bathrooms = models.PositiveSmallIntegerField()
    nr_floors = models.PositiveSmallIntegerField(default=1)
    year_built = models.PositiveIntegerField(null=True, blank=True)
    house_color_outside = models.CharField(max_length=20)
    distance_to_nearest_kindergarten = models.PositiveIntegerField(null=True, blank=True)
    distance_to_nearest_school = models.PositiveIntegerField(null=True, blank=True)
    distance_to_nearest_hospital = models.PositiveIntegerField(null=True, blank=True)
    has_cellar = models.BooleanField(default=False)
    has_pool = models.BooleanField(default=False)
    has_garage = models.BooleanField(default=False)
    price = models.PositiveIntegerField()

    def __unicode__(self):
        return '{} {} {}'.format(self.country, self.address, self.price)
