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

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_application('Testing')
        self.client = self.app.test_client()
        #self.ctx = self.app.app_context()
        #self.ctx.push()

    def tearDown(self):
        """Executed after reach test"""
        db.session.remove()
        #self.ctx.pop()


    def test_get_one_question(self):
        """Test getting a specific question."""
        response = self.client.get('/questions/2')

        data = response.get_json()
        #print(f'question data is {data}')
        #print(f'question mimetype is {response.mimetype}')
        self.assertEqual(response.status_code, 200)

        #self.assertTrue(data['success'])
        #self.assertEqual(data['totalQuestions'], 19)
        #self.assertTrue(len(data['categories']))
        #self.assertTrue(len(data['questions']) == 1)


#    def test_get_default_page_of_questions(self):
#        """Test getting the default page of questions."""
#        response = self.client.get('/questions')
#        print(f'test_get_default_page_of_questions response is {response}')
#        self.assertEqual(response.status_code, 200)
##
##        data = json.loads(response.data)
##        self.assertTrue(data['success'])
##        self.assertEqual(data['totalQuestions'], 19)
##        self.assertTrue(len(data['categories']))
##        self.assertTrue(len(data['questions']))
#
#
    def test_get_categories(self):
        """Test getting the list of trivia categories."""
        response = self.client.get('/categories')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        #print(f'categories data is {data}')
        #print(f'categories mimetype is {response.mimetype}')


    def test_get_category_of_questions(self):
        """Test getting a list of trivia questions by category."""
        response = self.client.get('/categories/2/questions')

        data = response.get_json()
        #print(f'category questions data is {data}')
        #print(f'category questions mimetype is {response.mimetype}')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
