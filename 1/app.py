# Container 1: app.py
from flask import Flask, request, jsonify, redirect
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/proxy', methods=['GET'])
def proxy():
    """
    Proxy endpoint to inspect Accept header and forward to backend.
    ---
    parameters:
      - name: Accept
        in: header
        type: string
        required: true
        description: The content type accepted by the client.
    responses:
      200:
        description: Success
      406:
        description: Not Acceptable
    """
    accept_header = request.headers.get('Accept')
    
    if accept_header in ['application/json', 'text/plain']:
        # Forward request to Container 2
        return redirect('http://container-2:5000/data', code=307)
    else:
        response = jsonify({"error": "Unsupported Accept header"})
        response.status_code = 406
        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
