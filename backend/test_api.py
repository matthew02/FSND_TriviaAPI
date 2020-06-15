#!/usr/bin/env python3
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from api.app import create_application
from api.models.model import db
from api.models.category import Category
from api.models.question import Question


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_application('Testing')
        self.client = self.app.test_client()
        #self.app_context = self.app.app_context()
        #self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        #self.app_context.pop()
        db.session.remove()
        db.drop_all()

    def test_get_one_question(self):
        """Test getting a specific question."""
        response = self.client.get('/questions/2')
        print(f'test_get_one_question response is {response}')
        self.assertEqual(response.status_code, 200)

#        data = json.loads(response.data)
#        self.assertTrue(data['success'])
#        self.assertEqual(data['totalQuestions'], 19)
#        self.assertTrue(len(data['categories']))
#        self.assertTrue(len(data['questions']) == 1)

    def test_get_default_page_of_questions(self):
        """Test getting the default page of questions."""
        response = self.client.get('/questions')
        print(f'test_get_default_page_of_questions response is {response}')
        self.assertEqual(response.status_code, 200)
#
#        data = json.loads(response.data)
#        self.assertTrue(data['success'])
#        self.assertEqual(data['totalQuestions'], 19)
#        self.assertTrue(len(data['categories']))
#        self.assertTrue(len(data['questions']))


    def test_get_categories(self):
        """Test getting the list of trivia categories."""
        response = self.client.get('/categories')
        print(f'test_get_categories response is {response}')
        self.assertEqual(response.status_code, 200)
#
#        data = json.loads(response.data)
#        self.assertTrue(data['success'])
#        self.assertEqual(data['totalQuestions'], 19)
#        self.assertTrue(len(data['categories']))
#        self.assertTrue(len(data['questions']))


if __name__ == "__main__":
    unittest.main()
