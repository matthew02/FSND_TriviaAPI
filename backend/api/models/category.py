"""Defines the trivia Category model."""
from typing import Any, Dict

from api.models.model import db, Model


class Category(Model):
    """This class represents a trivia Category."""
    __tablename__ = 'categories'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    type = db.Column(db.String)

    def __repr__(self):
        return f'<Category {self.id} {self.type}>'

    @classmethod
    def validate_all(cls, json: Dict[str, Any]) -> None:
        """Validates all model attributes of this resource."""
        raise NotImplementedError
