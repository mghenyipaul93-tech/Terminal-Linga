
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))

    # One Document -> Many Translations
    translations = relationship("Translation", back_populates="document")

    # One User -> Many Documents
    user = relationship("User", back_populates="documents")

    def __repr__(self):
        return f"<Document(title='{self.title}')>"