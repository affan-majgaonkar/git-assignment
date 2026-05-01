from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
db = client.test
collection = db['flask_tutorial']

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    try:
        form_data = dict(request.json)
        collection.insert_one(form_data)
        return jsonify({"message": "Data submitted successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/view', methods=['GET'])
def view():

        data = list(collection.find())

        data = list(data)

        for item in data:
            print(item)
            del item['_id']

        return jsonify({"data": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)