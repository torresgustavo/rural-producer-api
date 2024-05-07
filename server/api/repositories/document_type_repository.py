from typing import List

from api.models.document_type_model import DocumentType

class DocumentTypeRepository():

    def get_all(self):
        result = DocumentType.objects.all()
        return result