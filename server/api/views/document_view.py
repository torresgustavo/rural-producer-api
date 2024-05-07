
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from api.serializers.document_types_serializer import DocumentTypesSerializer
from api.repositories.document_type_repository import DocumentTypeRepository

class DocumentTypesView(APIView):
    def get(self, request: Request, format = None):
        document_types = DocumentTypeRepository().get_all()
        serializer = DocumentTypesSerializer(document_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
