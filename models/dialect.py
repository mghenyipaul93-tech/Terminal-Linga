
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class Dialect(Base):
    __tablename__ = "dialects"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    # One Dialect -> Many Translations
    translations = relationship("Translation", back_populates="dialect")

    def __repr__(self):
        return f"<Dialect(name='{self.name}')>"