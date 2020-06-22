import unittest

from tests.client import app


class CategoriesTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.client = app.test_client()

    def tearDown(self):
        """Executed after reach test"""

    def test_getting_the_list_of_categories(self):
        """Test getting the list of trivia categories."""
        response = self.client.get('/categories')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(len(data['categories']), 6)

    def test_getting_all_questions_from_a_category(self):
        """Test getting a list of trivia questions by category."""
        response = self.client.get('/categories/2/questions')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['current_category']['id'], 2)
        self.assertEqual(data['current_category']['type'], 'Art')
        self.assertEqual(len(data['questions']), 4)

    def test_getting_all_questions_from_a_non_existent_category(self):
        """Test getting a list of trivia questions from a category that doesn't exist."""
        response = self.client.get('/categories/100/questions')
        self.assertEqual(response.status_code, 404)

        data = response.get_json()
        self.assertFalse(data['success'])

    def test_that_delete_method_is_disallowed(self):
        """Test method-not-allowed deleting trivia categories."""
        response = self.client.delete('/categories')
        self.assertEqual(response.status_code, 405)

        data = response.get_json()
        self.assertFalse(data['success'])
