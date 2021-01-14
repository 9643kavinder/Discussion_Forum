from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import UserDocument


class UserDocumentSerializer(DocumentSerializer):
    class Meta:
        document = UserDocument
        fields = (
            'id',
            'name',
            'email',
            'phone',
        )