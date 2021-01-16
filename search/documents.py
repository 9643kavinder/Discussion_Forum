from django_elasticsearch_dsl import Document, fields, Index
from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl.registries import registry
from api.models import CustomUser, Post, Speciality


@registry.register_document
class UserDocument(Document):
    id = fields.KeywordField(attr='id')
    name = fields.TextField(
        attr="name",
        analyzer="english"
    )
    email = fields.KeywordField(attr='email')
    phone = fields.KeywordField(attr="phone")

    class Index:
        name = 'users'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = CustomUser


@registry.register_document
class DiscussionDocument(Document):
    id = fields.KeywordField(attr='id')
    message = fields.TextField(
        attr="message",
        analyzer="english"
    )
    speciality = fields.ObjectField(properties={
        'name': fields.TextField(attr="name", analyzer="standard"),
    }, attr="tags")

    class Index:
        name = 'posts'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Post
