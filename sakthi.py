from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['users']

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    user_data = {
        'username': username,
        'email': email,
        'password': password
    }
    
    collection.insert_one(user_data)
    
    return "success"

if __name__ == '__main__':
    app.run(debug=True)
