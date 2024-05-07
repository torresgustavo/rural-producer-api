from rest_framework import serializers

from api.models.document_type_model import DocumentType

class DocumentTypesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DocumentType
        fields = ['id', 'name']