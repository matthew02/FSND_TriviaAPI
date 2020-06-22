import unittest

from tests.client import app


class QuestionsTestCase(unittest.TestCase):
    """Tests for the question API."""

    def setUp(self):
        """Define test variables and initialize app."""
        self.client = app.test_client()

    def tearDown(self):
        """Executed after reach test"""


    def test_getting_an_individual__question(self):
        """Test getting a specific question."""
        response = self.client.get('/questions/2')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(data['success'])
        #self.assertEqual(data['totalQuestions'], 19)
        self.assertEqual(len(data['questions']), 1)
        self.assertGreater(len(data['categories']), 0)

    def test_getting_a_non_existent_question(self):
        """Test getting a question that doesn't exist."""
        response = self.client.get('/questions/100')
        self.assertEqual(response.status_code, 404)

        data = response.get_json()
        self.assertFalse(data['success'])

    def test_getting_the_default_page_of_questions(self):
        """Test getting the default page of questions."""
        response = self.client.get('/questions')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(data['success'])
        #self.assertEqual(data['totalQuestions'], 19)
        self.assertEqual(len(data['questions']), 10)
        self.assertGreater(len(data['categories']), 0)

    def test_getting_a_specific_page_of_questions(self):
        """Test getting a specific page of questions."""
        response = self.client.get('/questions?page=2')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(data['success'])
        #self.assertEqual(data['totalQuestions'], 19)
        #self.assertEqual(len(data['questions']), 9)
        self.assertGreater(len(data['categories']), 0)

    def test_getting_an_out_of_range_page_of_questions(self):
        """Test getting a page of questions that doesn't exist."""
        response = self.client.get('/questions?page=100')
        self.assertEqual(response.status_code, 404)

        data = response.get_json()
        self.assertFalse(data['success'])

    def test_posting_a_new_question(self):
        """Test posting a new question to the game."""
        response = self.client.post('/questions', json={
            'question': 'Some question?',
            'answer': 'Some answer.',
            'category': 1,
            'difficulty': 5,
        })
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(data['success'])

    def test_deleting_a_specific_question(self):
        """Test deleting a question from the game."""
        response = self.client.delete('/questions/23')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(data['success'])

    def test_searching_questions(self):
        """Test searching the questions for a specific term."""
        response = self.client.post('/questions/search', json={
            'search_term': 'who',
        })
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['total_questions'], 3)
