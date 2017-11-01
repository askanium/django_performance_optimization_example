from factory.declarations import SubFactory
from factory.django import DjangoModelFactory
from factory.faker import Faker
from factory.fuzzy import FuzzyInteger

from houses.models import House, Country


class CountryFactory(DjangoModelFactory):
    class Meta:
        model = Country

    name = Faker('country')


class HouseFactory(DjangoModelFactory):
    class Meta:
        model = House

    country = SubFactory(CountryFactory)

    address = Faker('address')
    sq_meters = FuzzyInteger(30, 400)
    kitchen_sq_meters = FuzzyInteger(5, 100)
    nr_bedrooms = FuzzyInteger(1, 7)
    nr_bathrooms = FuzzyInteger(1, 4)
    nr_floors = FuzzyInteger(1, 4)
    year_built = FuzzyInteger(1960, 2017)
    house_color_outside = Faker('safe_color_name')
    distance_to_nearest_kindergarten = FuzzyInteger(100, 5000)
    distance_to_nearest_school = FuzzyInteger(100, 5000)
    distance_to_nearest_hospital = FuzzyInteger(100, 5000)
    has_cellar = FuzzyInteger(0, 1)
    has_pool = FuzzyInteger(0, 1)
    has_garage = FuzzyInteger(0, 1)
    price = FuzzyInteger(50000, 500000)
