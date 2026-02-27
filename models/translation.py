
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Translation(Base):
    __tablename__ = "translations"

    id = Column(Integer, primary_key=True)
    explanation_text = Column(String, nullable=False)
    analogy = Column(String)

    document_id = Column(Integer, ForeignKey("documents.id"))
    dialect_id = Column(Integer, ForeignKey("dialects.id"))

    # Many Translations -> One Document
    document = relationship("Document", back_populates="translations")

    # Many Translations -> One Dialect
    dialect = relationship("Dialect", back_populates="translations")

    def __repr__(self):
        return f"<Translation(document_id={self.document_id}, dialect_id={self.dialect_id})>"