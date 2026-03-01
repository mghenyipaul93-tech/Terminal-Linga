
from datetime import datetime


class DocumentService:
    def __init__(self):
        self.documents = {}
        self.counter = 1

    def _generate_id(self):
        document_id = self.counter
        self.counter += 1
        return document_id

    def create_document(self, user_id, original_text, translated_text, language):
        if not original_text:
            raise ValueError("Original text cannot be empty.")
        if not translated_text:
            raise ValueError("Translated text cannot be empty.")

        document_id = self._generate_id()

        document = {
            "id": document_id,
            "user_id": user_id,
            "original_text": original_text,
            "translated_text": translated_text,
            "language": language,
            "created_at": datetime.now()
        }

        self.documents[document_id] = document
        return document

    def get_documents_by_user(self, user_id):
        return [
            doc for doc in self.documents.values()
            if doc["user_id"] == user_id
        ]

    def get_all_documents(self):
        return list(self.documents.values())