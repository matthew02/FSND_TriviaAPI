"""Defines the trivia Question model."""
from typing import Any, Dict, Optional

from flask import abort

from api.models.model import db, Model


class Question(Model):
    """This class represents a trivia Question."""
    __tablename__ = 'questions'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    question = db.Column(db.String)
    answer = db.Column(db.String)
    category = db.Column(db.String)
    difficulty = db.Column(db.Integer)

    def __repr__(self):
        return f'<Question {self.id} {self.question}>'

    @classmethod
    def search(cls, search_term: str, order_by: Optional[object] = None):
        """Fetches all resources matching a search term from the database."""
        resources = cls.query.filter(cls.question.ilike(f'%{search_term}%')).order_by(order_by).all()
        if not resources:
            abort(404)
        return [resource.json() for resource in resources]

    @classmethod
    def validate_all(cls, json: Dict[str, Any]) -> None:
        """Validates all model attributes of this resource."""
        raise NotImplementedError
