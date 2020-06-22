# Full-Stack Trivia Front-End

## Getting Started

> _Tip_: This front-end is designed to work with a [Flask-based back-end](https://github.com/udacity/FSND/tree/master/projects/02_trivia_api/starter/backend). It is recommended you stand up the backend first and then the front-end should integrate smoothly.

### Installing Dependencies

#### Installing Node and NPM
This project depends on Node.js and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM uses the `package.json` file located in the `/frontend` directory of this repository. After cloning, navigate to the `/frontend` directory in your terminal and run:

`$ npm install`

## Running The Front-End

The front-end app was built using create-react-app. In order to run the app, navigate to the `/frontend` directory and run:

`$ npm start`

Open [http://localhost:3000](http://localhost:3000) to view it in the browser.
<br>
# Full-Stack Trivia Back-End

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

This project uses a Pipenv virtual environment. This keeps the dependencies neatly packaged. Instructions for installing Pipenv on your platform can be found in the [pipenv docs](https://pypi.org/project/pipenv/)

#### Python Dependencies

Once you have installed Pipenv, you will install the dependency packages by navigating to the `/backend` directory and running:

`$ pipenv install`

This will install all of the required packages selected within the `Pipfile` file.

## Database Setup

> ***Note:*** Installation and startup of PostgreSQL is outside the scope of this document. Refer to the PostgreSQL website for more information. 

With PostgreSQL running, create the database and populate it using the provided `trivia.psql` file. Navigate to the `/backend` folder in your terminal and run:

```
$ createdb trivia
$ psql trivia < trivia.psql
```

## Running the server

Prior to running the server, you will need to activate your virtual environment. Navigate to the `backend` directory and run:
`$ pipenv shell`

Then to start the server, run:
`$ ./run.py`
<br>
# API Documentation
## Available Endpoints
[**GET** /categories](#get_categories)

[**GET** /categories/\<category_id\>/questions](#get_categories_questions)

[**GET** /questions](#get_questions)

[**GET** /questions/\<question_id\>](#get_question_by_id)

[**POST** /questions](#post_question)

[**POST** /questions/search](#search_questions)

[**DELETE** /questions/\<question_id\>](#delete_question)

[**POST** /quizzes](#dispatch_question)
## Individual Endpoints

<a id="get_categories"></a>**GET** /categories
 - Fetches a list of trivia categories
 - Request Arguments: None
 - Request Body Parameters: None
 - Returns: A JSON object with key-value pairs:
   - ***categories***: (*Object*) a list of all trivia categories
     - ***id***: (*String*) category_id
     - ***name***: (*String*) category_name
   - ***success***: (*Boolean*) true

**Example:**
```
$ curl http://localhost:5000/categories
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4" : "History",
        "5" : "Entertainment",
        "6" : "Sports"
    },
    "success": true
}
```
<br>

<a id="get_categories_questions"></a>**GET** /categories/\<category_id\>/questions

 - Fetches a list of all trivia questions from a specific category
 - Request Arguments: None
 - Returns: A JSON object with key-value pairs:
   - ***current_category***: (*Integer*) id of the current category of questions
   - ***questions***: (*Array[Object]*) a list of questions
     - ***answer***: (*String*) answer to the question
     - ***category***: (*Integer*) category of the question
     - ***difficulty***: (*Integer*) question difficulty
     - ***id***: (*Integer*) question id
     - ***question***: (*String*) question
   - ***success***: (*Boolean*) true
   - ***total_questions***: (*Integer*) total number of trivia questions in the game

**Example:**
```
$ curl http://localhost:5000/categories/1/questions
{
    "current_category": {
        "id": 1,
        "type": "Science"
    },
    "questions": [
        {
            "answer": "The Liver",
            "category": 1,
            "difficulty": 4,
            "id": 20,
            "question": "What is the heaviest organ in the human body?"
        },
        {
            "answer": "Alexander Fleming",
            "category": 1,
            "difficulty": 3,
            "id": 21,
            "question": "Who discovered penicillin?"
        },
        {
            "answer": "Blood",
            "category": 1,
            "difficulty": 4,
            "id": 22,
            "question": "Hematology is a branch of medicine involving the study of what?"
        }
    ],
    "success": true,
    "total_questions": 19
}
```
<br>

<a id="get_questions"></a>**GET** /questions

 - Fetches a paginated list of all trivia questions
 - Request Arguments: **page**=\<*page_number*\> (default: 1)
 - Request Body Parameters: None
 - Returns: A JSON object with key-value pairs:
   - ***categories***: (*Object*)
     - ***id***: (*String*) category_id
     - ***name***: (*String*) category_name
   - ***current_category***: (*unused*) null 
   - ***questions***: (*Array[Object]*) a list of questions
     - ***answer***: (*String*) answer to the question
     - ***category***: (*Integer*) category of the question
     - ***difficulty***: (*Integer*) question difficulty
     - ***id***: (*Integer*) question id
     - ***question***: (*String*) question
   - ***success***: (*Boolean*) true
   - ***total_questions***: (*Integer*) total number of trivia questions in the game

**Example:**
```
$ curl http://localhost:5000/questions?page=2
{                                                                                                                                                                                                                                    [25/4494]
    "categories": {                                                                                                                                                                                                                          
        "1": "Science",                                                                                                                                                                                                                       
        "2": "Art",                                                                                                                                                                                                                           
        "3": "Geography",                                                                                                                                                                                                                     
        "4": "History",                                                                                                                                                                                                                       
        "5": "Entertainment",                                                                                                                                                                                                                 
        "6": "Sports"                                                                                                                                                                                                                         
    },                                                                                                                                                                                                                                        
    "currentCategory": null,                                                                                                                                                                                                                  
    "questions": [                                                                                                                                                                                                                            
        {                                                                                                                                                                                                                                     
            "answer": "Agra",                                                                                                                                                                                                                 
            "category": 3,                                                                                                                                                                                                                    
            "difficulty": 2,                                                                                                                                                                                                                  
            "id": 15,                                                                                                                                                                                                                         
            "question": "The Taj Mahal is located in which Indian city?"                                                                                                                                                                      
        },                                                                                                                                                                                                                                    
        {                                                                                                                                                                                                                                     
            "answer": "Escher",                                                                                                                                                                                                               
            "category": 2,                                                                                                                                                                                                                    
            "difficulty": 1,                                                                                                                                                                                                                  
            "id": 16,                                                                                                                                                                                                                         
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"                                                                                                                                         
        },                                                                                                                                                                                                                                    
        {                                                                                                                                                                                                                                     
            "answer": "Mona Lisa",
            "category": 2,
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
        },
        {
            "answer": "One",
            "category": 2,
            "difficulty": 4,
            "id": 18,
            "question": "How many paintings did Van Gogh sell in his lifetime?"
        },
        {
            "answer": "Jackson Pollock",
            "category": 2,
            "difficulty": 2,
            "id": 19,
            "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
        },
        {
            "answer": "The Liver",
            "category": 1,
            "difficulty": 4,
            "id": 20,
            "question": "What is the heaviest organ in the human body?"
        },
        {
            "answer": "Alexander Fleming",
            "category": 1,
            "difficulty": 3,
            "id": 21,
            "question": "Who discovered penicillin?"
        },
        {
            "answer": "Blood",
            "category": 1,
            "difficulty": 4,
            "id": 22,
            "question": "Hematology is a branch of medicine involving the study of what?"
        },
        {
            "answer": "Scarab",
            "category": 4,
            "difficulty": 4,
            "id": 23,
            "question": "Which dung beetle was worshipped by the ancient Egyptians?"
        }
    ],
    "success": true,
    "totalQuestions": 19
}
```
 <br>

<a id="get_question_by_id"></a>**GET** /questions/\<question_id\>

 - Fetches a specific trivia question
 - Request Arguments: None
 - Request Body Parameters: None
 - Returns: A JSON object with key-value pairs:
   - ***categories***: (*Object*)
     - ***id***: (*String*) category_id
     - ***name***: (*String*) category_name
   - ***current_category***: (*Integer*) id of the category of this question
   - ***questions***: (*Array[Object]*) a list of questions
     - ***answer***: (*String*) answer to the question
     - ***category***: (*Integer*) category of the question
     - ***difficulty***: (*Integer*) question difficulty
     - ***id***: (*Integer*) question id
     - ***question***: (*String*) question
   - ***success***: (*Boolean*) true
   - ***total_questions***: (*Integer*) total number of trivia questions in the game

**Example:**
```
$ curl http://localhost:5000/questions/2
{                                                                                                                                                                                                                                             
    "categories": {                                                                                                                                                                                                                           
        "1": "Science",                                                                                                                                                                                                                       
        "2": "Art",                                                                                                                                                                                                                           
        "3": "Geography",                                                                                                                                                                                                                     
        "4": "History",                                                                                                                                                                                                                       
        "5": "Entertainment",                                                                                                                                                                                                                 
        "6": "Sports"                                                                                                                                                                                                                         
    },                                                                                                                                                                                                                                        
    "currentCategory": 5,                                                                                                                                                                                                                     
    "questions": [                                                                                                                                                                                                                            
        {                                                                                                                                                                                                                                     
            "answer": "Apollo 13",                                                                                                                                                                                                            
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        }
    ],
    "success": true,
    "totalQuestions": 19
}

```
<br>

<a id="post_question"></a>**POST** /questions

 - Adds a new trivia question to the game
 - Request Arguments: None
 - Request Body Parameters: A JSON object with key-value pairs:
   - ***question***: (*String*) question
   - ***answer***: (*String*) answer to the question
   - ***category***: (*Integer*) category of the question
   - ***difficulty***: (*Integer*) question difficulty
 - Returns: A JSON object with key-value pairs:
   - ***questions***: (*Array[Object]*) a list of questions
     - ***answer***: (*String*) answer to the question
     - ***category***: (*Integer*) category of the question
     - ***difficulty***: (*Integer*) question difficulty
     - ***id***: (*Integer*) question id
     - ***question***: (*String*) question
   - ***success***: (*Boolean*) true
   - ***total_questions***: (*Integer*) total number of trivia questions in the game

**Example:**
```
$ curl -X POST http://pythondev.local:5000/questions -H "Content-Type: application/json" -d '{"question":"What is the answer?", "answer":"seven", "category":"1", "difficulty":"5"}'
{
  "questions": [
    {
      "answer": "seven", 
      "category": 1, 
      "difficulty": 5, 
      "id": 24, 
      "question": "What is the answer?"
    }
  ], 
  "success": true, 
  "totalQuestions": 20
}
``` 
<br>

<a id="search_questions"></a>**POST** /questions/search

 - Searches all trivia questions and returns a list of questions matching the search term
 - Request Arguments: None
 - Request Body Parameters: A JSON object with key-value pairs:
   - ***search_term***: (*String*) a case-insensitive search term
 - Returns: A JSON object with key-value pairs:
   - ***current_category***: (*Integer*) null
   - ***questions***: (*Array[Object]*) a list of questions
     - ***answer***: (*String*) answer to the question
     - ***category***: (*Integer*) category of the question
     - ***difficulty***: (*Integer*) question difficulty
     - ***id***: (*Integer*) question id
     - ***question***: (*String*) question
   - ***success***: (*Boolean*) true
   - ***total_questions***: (*Integer*) total number of trivia questions matching the search term

**Example:**
```
$ curl -X POST http://pythondev.local:5000/questions/search -H "Content-Type: application/json" -d '{"search_term":"hematology"}''{"question":"What is the answer?", "answer":"seven", "category":"1", "difficulty":"5"}'
{
  "current_category": null,
  "questions": [
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ], 
  "success": true, 
  "totalQuestions": 1
}
``` 
 <br>

<a id="delete_question"></a>**DELETE** /questions/\<question_id\>

 - Deletes a trivia question from the game
 - Request Arguments: None
 - Request Body Parameters: None
 - Returns: A JSON object with key-value pairs:
   - ***success***: (*Boolean*) true
   - ***total_questions***: (*Integer*) total number of trivia questions in the game

**Example:**
```
$ curl -X DELETE http://localhost:5000/questions/2
{
    "success": true,
    "totalQuestions": 18
}

```
<br>

<a id="dispatch_question"></a>**POST** /quizzes

 - Fetches a random question
 - Request Arguments: None
 - Request Body Parameters: A JSON object with key-value pairs:
   - ***previous_questions***: (*Array[Integer]*) a list of question ids to exclude from the random selection
   - ***quiz_category***: (*Object*) category of the desired question
     - ***type***: (*String*) category name (use 'click' for all categories)
     - ***id***: (*Integer*) category id
 - Returns: A JSON object with key-value pairs:
   - ***question***: (*Object*)
     - ***answer***: (*String*) answer to the question
     - ***category***: (*Integer*) category of the question
     - ***difficulty***: (*Integer*) question difficulty
     - ***id***: (*Integer*) question id
     - ***question***: (*String*) question
   - ***success***: (*Boolean*) true

**Example:**
```
$ curl -X POST http://pythondev.local:5000/quizzes -H "Content-Type: application/json" -d '{"previous_questions":[16,18], "quiz_category":{"type":"Art", "id": 2}}'
{
  "question": {
    "answer": "Mona Lisa", 
    "category": 2, 
    "difficulty": 3, 
    "id": 17, 
    "question": "La Giaconda is better known as what?"
  }, 
  "success": true
}
``` 

