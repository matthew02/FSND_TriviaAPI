import unittest

from tests.client import app


class QuizTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.client = app.test_client()

    def tearDown(self):
        """Executed after reach test"""

    def test_getting_a_new_random_question_for_a_quiz(self):
        """Test getting a new random trivia question for a quiz."""
        response = self.client.post('/quizzes', json={
            'quiz_category': {'type': 'Art', 'id': '2'},
            'previous_questions': [16, 17, 18],
        })
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['question']['id'], 19)
