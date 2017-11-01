import basehash
from django.contrib.contenttypes.models import ContentType


class Hasher(object):
    @classmethod
    def from_model(cls, obj, klass=None):
        if obj.pk is None:
            return None
        return cls.make_hash(obj.pk, klass if klass is not None else obj)

    @classmethod
    def make_hash(cls, object_pk, klass):
        base36 = basehash.base36()
        content_type = ContentType.objects.get_for_model(klass, for_concrete_model=False)
        return base36.hash('%(contenttype_pk)03d%(object_pk)06d' % {
            'contenttype_pk': content_type.pk,
            'object_pk': object_pk
        })
        
    @classmethod
    def parse_hash(cls, obj_hash):
        base36 = basehash.base36()
        unhashed = '%09d' % base36.unhash(obj_hash)
        contenttype_pk = int(unhashed[:-6])
        object_pk = int(unhashed[-6:])
        return contenttype_pk, object_pk

    @classmethod
    def to_object_pk(cls, obj_hash):
        return cls.parse_hash(obj_hash)[1]
