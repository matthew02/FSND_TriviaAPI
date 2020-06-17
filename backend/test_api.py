#!/usr/bin/env python3
import os
import unittest
from flask_sqlalchemy import SQLAlchemy

from api.app import create_application
from api.models.model import db
from api.models.category import Category
from api.models.question import Question




class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    app = create_application('Testing')

    def setUp(self):
        """Define test variables and initialize app."""
        self.client = self.app.test_client()

    def tearDown(self):
        """Executed after reach test"""


    def test_get_one_question(self):
        """Test getting a specific question."""
        response = self.client.get('/questions/2')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['totalQuestions'], 19)
        self.assertEqual(len(data['questions']), 1)
        self.assertGreater(len(data['categories']), 0)

    def test_get_missing_question(self):
        """Test getting a question that doesn't exist."""
        response = self.client.get('/questions/100')
        self.assertEqual(response.status_code, 404)

        data = response.get_json()
        self.assertFalse(data['success'])

    def test_get_default_page_of_questions(self):
        """Test getting the default page of questions."""
        response = self.client.get('/questions')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['totalQuestions'], 19)
        self.assertEqual(len(data['questions']), 10)
        self.assertGreater(len(data['categories']), 0)

    def test_get_specific_page_of_questions(self):
        """Test getting a specific page of questions."""
        response = self.client.get('/questions?page=2')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['totalQuestions'], 19)
        self.assertEqual(len(data['questions']), 9)
        self.assertGreater(len(data['categories']), 0)

    def test_get_missing_page_of_questions(self):
        """Test getting a page of questions that doesn't exist."""
        response = self.client.get('/questions?page=100')
        self.assertEqual(response.status_code, 404)

        data = response.get_json()
        self.assertFalse(data['success'])

    def test_post_new_question(self):
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

    def test_z_delete_question(self):
        """Test deleting a question from the game."""
        response = self.client.delete('/questions/24')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(data['success'])

    def test_search_questions(self):
        """Test searching the questions for a specific term."""
        response = self.client.post('/questions/search', json={
            'search_term': 'who',
        })
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['total_questions'], 3)

    def test_get_categories(self):
        """Test getting the list of trivia categories."""
        response = self.client.get('/categories')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(len(data['categories']), 6)

    def test_get_category_of_questions(self):
        """Test getting a list of trivia questions by category."""
        response = self.client.get('/categories/2/questions')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['current_category']['id'], 2)
        self.assertEqual(data['current_category']['type'], 'Art')
        self.assertEqual(len(data['questions']), 4)

    def test_get_missing_category_of_questions(self):
        """Test getting a list of trivia questions from a category that doesn't exist."""
        response = self.client.get('/categories/100/questions')
        self.assertEqual(response.status_code, 404)

        data = response.get_json()
        self.assertFalse(data['success'])

    def test_delete_categories_disallowed_method(self):
        """Test method-not-allowed deleting trivia categories."""
        response = self.client.delete('/categories')
        self.assertEqual(response.status_code, 405)

        data = response.get_json()
        self.assertFalse(data['success'])

    def test_post_quiz_retrieve_new_question(self):
        """Test getting a new trivia question for a quiz."""
        response = self.client.post('/quizzes', json={
            'quiz_category': {'type': 'Art', 'id': '2'},
            'previous_questions': [16, 17, 18],
        })
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['question']['id'], 19)

if __name__ == "__main__":
    unittest.main()
