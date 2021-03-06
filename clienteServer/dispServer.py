from flask import Flask, request, json
from pymongo import MongoClient

app = Flask(__name__)
mongo_client = MongoClient()
mongo_client['HomeControl'].temperature.drop ()

@app.route("/homecontrol/api/v1.0/temperature", methods=['POST'])
def api_temperature():
    if request.headers['Content-Type'] == 'text/plain':
        print (request.data)
        return 'OK', 200
    elif request.headers['Content-Type'] == 'application/json':
        print (json.dumps(request.json))
        mongo_client['HomeControl']['temperature'].insert(request.json)
        print (mongo_client['HomeControl']['temperature'].count ())
        return "OK", 200
    else:
        return "Unsupported Media Type", 415

if __name__ == '__main__':
    app.run(debug = False)