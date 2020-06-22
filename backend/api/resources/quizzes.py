"""API interface for trivia quizzes."""
import random

from flask import Response, current_app, jsonify, request

from api.models.category import Category
from api.models.question import Question


class QuizAPI():
    """API interface for the Trivia quizzes."""

    @staticmethod
    def dispatch_question() -> Response:
        """Dispatches new questions to an active game."""
        # NOTE: The front-end is buggy and doesn't pass the correct category id,
        # so we must lookup the category by 'type' instead. The 'type' passed
        # from the front-end for ALL is 'click', otherwise it is the name of the
        # category ('science', 'art', etc...)
        request_json = request.get_json()

        # Fetch all questions from the user-selected category
        category = request_json.get('quiz_category')
        if category.get('type') == 'click':
            questions = Question.fetch_all()
        else:
            category = Category.fetch_first_filtered({
                'type': category.get('type')
            })
            questions = Question.fetch_all_filtered({
                'category': category.get('id')
            })

        # Enumerate the set of questions which have not previously been asked
        previous_questions = set(request_json.get('previous_questions'))
        all_questions = set([question['id'] for question in questions])
        available_questions = all_questions - previous_questions

        # Select a random question from those available, or None
        if available_questions:
            question = random.choice(tuple(available_questions))
        else:
            question = None

        return jsonify({
            'success': True,
            'question': question and Question.fetch_by_id(question),
        })


current_app.add_url_rule(
    rule='/quizzes',
    endpoint='quiz',
    view_func=QuizAPI.dispatch_question,
    methods=['POST']
)
