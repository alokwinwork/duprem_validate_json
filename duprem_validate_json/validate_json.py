from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/validate-service', methods=['POST'])
def validate_json_input():
    # Get the JSON input data from the request body
    json_input = request.json

    # Validate the JSON input data
    # Add your validation logic here
    if 'firstname' not in json_input:
        return jsonify(error="Missing firstname field"), 400
    if 'lastname' not in json_input:
        return jsonify(error="Missing lastname field"), 400
    if 'gender' not in json_input:
        return jsonify(error="Missing gender field"), 400
    if 'age' not in json_input:
        return jsonify(error="Missing age field"), 400

    # If the input data passes validation, return a success response
    return jsonify(success=True), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
