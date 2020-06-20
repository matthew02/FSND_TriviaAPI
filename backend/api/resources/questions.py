"""API interface for trivia Questions."""

from typing import Optional

from flask import Response, current_app, jsonify, request

from api.models.category import Category
from api.models.question import Question
from config import Config


class QuestionAPI():
    """API interface for trivia Questions."""

    @staticmethod
    def delete(question_id: int) -> Response:
        """Deletes a question."""
        Question.delete_by_id(question_id)
        return jsonify({
            'success': True,
            'totalQuestions': Question.count_all(),
        })

    @staticmethod
    def get_one(question_id: int) -> Response:
        """Fetches one question from the database."""
        question = Question.fetch_by_id(question_id)

        categories = {
            category['id']: category['type']
            for category
            in Category.fetch_all(Category.id)
        }

        return jsonify({
            'success': True,
            'questions': [question],
            'totalQuestions': Question.count_all(),
            'categories': categories,
            'currentCategory': question['category'],
        })

    @staticmethod
    def get_page() -> Response:
        """Fetches one page of questions from the database.
        If no specific page is requested, default to page 1."""
        page = int(request.args.get('page', 1))
        questions = Question.fetch_page(page, Config.PAGE_LENGTH)

        categories = {
            category['id']: category['type']
            for category
            in Category.fetch_all(Category.id)
        }

        return jsonify({
            'success': True,
            'questions': questions,
            'totalQuestions': Question.count_all(),
            'categories': categories,
            'currentCategory': None,
        })

    @staticmethod
    def post_new() -> Response:
        """Adds a new question to the game."""
        question = Question(**request.get_json())
        question.insert()
        return jsonify({
            'success': True,
            'questions': [question.json()],
            'totalQuestions': Question.count_all(),
        })

    @staticmethod
    def search() -> Response:
        """Searches for a specific question."""
        results = Question.search(request.get_json()['search_term'])
        return jsonify({
            'success': True,
            'questions': results,
            'total_questions': len(results),
            'current_category': None,
        })


current_app.add_url_rule(
    rule='/questions/<int:question_id>',
    endpoint='delete_question',
    view_func=QuestionAPI.delete,
    methods=['DELETE']
)

current_app.add_url_rule(
    rule='/questions',
    endpoint='get_page_of_questions',
    view_func=QuestionAPI.get_page,
    methods=['GET']
)

current_app.add_url_rule(
    rule='/questions/<int:question_id>',
    endpoint='get_one_question',
    view_func=QuestionAPI.get_one,
    methods=['GET']
)

current_app.add_url_rule(
    rule='/questions',
    endpoint='post_new_question',
    view_func=QuestionAPI.post_new,
    methods=['POST']
)

current_app.add_url_rule(
    rule='/questions/search',
    endpoint='search_questions',
    view_func=QuestionAPI.search,
    methods=['POST']
)
