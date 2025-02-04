# HNG-stage1

Stage 1 Backend - Number Classification API
This is a Python-based API that classifies a given number and returns mathematical properties about it along with a fun fact. It checks if the number is prime, perfect, Armstrong, and whether it's odd or even. Additionally, it fetches a fun fact related to the number from an external API.

Features
Classify numbers and return:

Whether the number is prime
Whether the number is perfect
Whether the number is Armstrong
Whether the number is odd or even
The sum of its digits
A fun fact about the number
Returns results in JSON format

Handles CORS for cross-origin requests

Supports GET requests

Requirements
Python 3.7+
Django 3.x+
Django REST Framework
External API: NumbersAPI
Installation
1. Clone the Repository
Clone this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/RexDavid06/HNG-stage1.git
cd HNG-stage1
2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.

bash
Copy
Edit
python -m venv venv
Activate the virtual environment:

Windows:

bash
Copy
Edit
venv\Scripts\activate
macOS/Linux:

bash
Copy
Edit
source venv/bin/activate
3. Install Dependencies
Install the required dependencies using pip:

bash
Copy
Edit
pip install -r requirements.txt
4. Set Up Django Project
After installing the dependencies, migrate the database:

bash
Copy
Edit
python manage.py migrate
5. Run the Development Server
Start the Django development server:

bash
Copy
Edit
python manage.py runserver
The API should now be running at http://127.0.0.1:8000.

6. Test the API
You can test the API by visiting the following endpoint:

bash
Copy
Edit
http://127.0.0.1:8000/api/classify-number?number=371
7. Deploy to Production
You can deploy this API to any platform of your choice, such as Heroku, AWS, or DigitalOcean. Make sure to configure your CORS settings for production use.

API Endpoints
1. Classify Number
Endpoint: GET /api/classify-number?number=<number>

Parameters:

number (required): The number to classify.
Response Format (200 OK):

json
Copy
Edit
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
Response Format (400 Bad Request):

json
Copy
Edit
{
    "number": "alphabet",
    "error": true
}
How It Works
Prime Check: The API checks if the number is divisible by 1 and itself.
Perfect Number: It checks if the sum of the divisors of the number equals the number itself.
Armstrong Number: The API checks if the sum of the digits raised to the power of the number of digits equals the number.
Even/Odd: It checks whether the number is divisible by 2 (even) or not (odd).
Fun Fact: A fun fact about the number is fetched from the NumbersAPI.
