"""API interface for trivia question Categories."""
import datetime

from flask import Response, current_app, jsonify

from api.models.category import Category
from api.models.question import Question


class CategoryAPI():
    """API interface for Categories of trivia questions."""

    @staticmethod
    def get() -> Response:
        """Fetches a list of all categories."""
        return jsonify({
            'success': True,
            'categories': {
                category['id']: category['type']
                for category
                in Category.fetch_all(Category.id)
            }
        })

    @staticmethod
    def get_questions(category_id: int) -> Response:
        """Fetches a list of all questions in a specified category."""
        return jsonify({
            'success': True,
            'questions': Question.fetch_all_filtered({'category': category_id}),
            'total_questions': Question.count_all(),
            'current_category': Category.fetch_by_id(category_id),
        })


current_app.add_url_rule(
    rule='/categories',
    endpoint='categories',
    view_func=CategoryAPI.get,
    methods=['GET']
)

current_app.add_url_rule(
    rule='/categories/<int:category_id>/questions',
    endpoint='questions_by_category',
    view_func=CategoryAPI.get_questions,
    methods=['GET']
)
