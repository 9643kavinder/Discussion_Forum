from django_elasticsearch_dsl import Document, fields, Index
from django_elasticsearch_dsl.registries import registry
from api.models import CustomUser


@registry.register_document
class UserDocument(Document):
    name = fields.TextField(
        attr='name',
        fields={
            'suggest': fields.Completion(),
        }
    )

    class Index:
        name = 'users'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = CustomUser
        fields = ['id', 'email', 'phone']