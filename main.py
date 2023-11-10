from flask import Flask, request, jsonify
from flask_cors import CORS
from my_connection import Connection as conn

app = Flask(__name__)
CORS(app)


@app.route("/vistoria/finalizar", methods=['POST'])
def insert_bike() -> jsonify:
    try:
        bikeData = request.get_json()
        conn.insert_new_bicycle(bikeData)
        return jsonify(bikeData), 201
    except Exception as e:
        print("Error inserting new bike: ", e)
        return jsonify({"message": "An error occurred."}), 500


@app.route("/bikes/<int:client_id>")
def find_all_bikes_by_client_id(client_id) -> jsonify:
    try:
        bicycles = conn.select_bikes_by_client_id(client_id)
        return jsonify(bicycles), 200
    except Exception as e:
        print("Error finding bikes by client id: ", e)
        return jsonify({"message": "An error occurred."}), 500


if __name__ == "__main__":
    app.run(debug=True, port=8080)
