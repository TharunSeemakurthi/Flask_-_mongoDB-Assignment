from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)

db = client.assignment
collection = db['FormData']
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']

            collection.insert_one({
                "name": name,
                "email": email
            })

            return render_template("success.html")

        except Exception as e:
            return render_template("form.html", error=str(e))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)