"""Defines the trivia Category model."""

from typing import Any, Dict, Optional

from api.models.model import db, Model


class Category(Model):
    """This class represents a trivia Category."""
    __tablename__ = 'categories'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    type = db.Column(db.String)

    def __repr__(self):
        return f'<Category {self.id} {self.type}>'

    @classmethod
    def fetch_all(
        cls,
        order_by: Optional[object] = None
    ) -> Optional[Dict[str, Any]]:
        """Fetches all categories, ordered.

        Args:
            order_by: SQLAlchemy ORDER BY criterion (see SQLAlchemy docs)

        Returns:
            An ordered dict of all categories or None.
        """
        categories = cls.query.order_by(order_by).all()
        if categories:
            return {category.id: category.type for category in categories}

#    @classmethod
#    def validate_all(cls, json: Dict[str, Any]) -> None:
#        """Validates all model attributes of this resource."""
#        raise NotImplementedError
