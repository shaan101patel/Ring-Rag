# This file defines custom types and interfaces used throughout the application, ensuring type safety and clarity in function signatures.

from typing import List, Dict, Any

class Document:
    def __init__(self, content: str, metadata: Dict[str, Any] = None):
        self.content = content
        self.metadata = metadata or {}

class FileUpload:
    def __init__(self, file_paths: List[str]):
        self.file_paths = file_paths

    def upload_files(self) -> List[Document]:
        # Logic to upload files and convert them to Document instances
        pass

class Query:
    def __init__(self, question: str, context: List[Document]):
        self.question = question
        self.context = context

class Result:
    def __init__(self, answer: str, source_documents: List[Document]):
        self.answer = answer
        self.source_documents = source_documents