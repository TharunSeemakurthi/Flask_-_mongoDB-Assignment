# Flask_-_mongoDB-Assignment
This assignment contains answers for Flask and MongoDB 

1. Create a Flask application with an /api route. When this route is accessed, it should return a JSON list. The data should be stored in a backend file, read from it, and sent as a response.

To achieve this have created a data.json file to update the data manually, then we have called the data.json file in the flask code using open (file, r) as file and json.load 
We have imported jsonify, flask, and json 

2. Create a form on the frontend that, when submitted, inserts data into MongoDB Atlas. Upon successful submission, the user should be redirected to another page displaying the message "Data submitted successfully". If there's an error during submission, display the error on the same page without redirection.

To achieve this, I have created multiple files like app.py, index.html, success.html, .env & requirements.txt
have added MongoDB credentials through the .env file and called the same in app.py file
We have imported flask, pymongo, dnspython, json, and python-dotenv(mongo creds file)
To catch the errors, we have used try and catch blocks 
