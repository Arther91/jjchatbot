from flask import Flask, jsonify, request
import time

app = Flask(__name__)

@app.route("/bot", methods=["POST"])  # "methods" instead of "method"

# #responce
# def responce():
#     query = dict(request.from)['query']
#     result = query + " " + time.ctime()
#     return jsonify({"responce" : result})

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", )

def response():  # Corrected function name to "response"
    data = request.get_json()  # Using get_json() to parse JSON data
    query = data.get('query', '')  # Extracting 'query' from the JSON data
    result = query + " " + time.ctime()
    return jsonify({"response": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Added port parameter