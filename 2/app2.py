# Container 2: app.py
from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/data', methods=['GET'])
def get_data():
    """
    Endpoint to return data from the backend API.
    ---
    responses:
      200:
        description: Success
        schema:
          type: object
          properties:
            message:
              type: string
    """
    return jsonify({"message": "Data from backend API"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
