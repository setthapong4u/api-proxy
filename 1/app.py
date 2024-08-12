from flask import Flask, request, jsonify, redirect
import requests

app = Flask(__name__)

@app.route('/proxy', methods=['GET'])
def proxy():
    """
    Proxy endpoint to inspect Accept header and forward to backend.
    """
    accept_header = request.headers.get('Accept')

    if accept_header in ['application/json', 'text/plain']:
        # Forward request to api-backend
        try:
            response = requests.get(f'http://api-backend:5000/data', headers={'Accept': accept_header})
            return (response.content, response.status_code, response.headers.items())
        except requests.exceptions.RequestException as e:
            return jsonify({"error": "Failed to reach backend service"}), 502
    else:
        response = jsonify({"error": "Unsupported Accept header"})
        response.status_code = 406
        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
