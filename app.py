from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/calculate', methods=['GET'])
def calculate_sum():
    data_type = request.args.get('dataType', '').lower()
    data_string = request.args.get('string', '')

    try:
        if data_type == 'single':
            # Safely parse the data_string as a Python dictionary
            params = eval(data_string)  # Only use eval with trusted input
            num1 = int(params.get('a', 0))
            num2 = int(params.get('b', 0))
            result = num1 + num2
            return jsonify({'sum': result})

        elif data_type == 'array':
            # Parse key-value pairs from the string
            params = {k: int(v) for k, v in [pair.split('=') for pair in data_string.split('&')]}
            num1 = params.get('a', 0)
            num2 = params.get('b', 0)
            result = num1 + num2
            return jsonify({'sum': result})

        elif data_type == 'json':
            # Parse JSON-like input from the string
            params = json.loads(data_string)
            num1 = int(params.get('a', 0))
            num2 = int(params.get('b', 0))
            result = num1 + num2
            return jsonify({'sum': result})

        elif data_type == 'object':
            # Similar to JSON; process the query string into a dictionary
            params = {k: int(v) for k, v in [pair.split('=') for pair in data_string.split('&')]}
            num1 = params.get('a', 0)
            num2 = params.get('b', 0)
            result = num1 + num2
            return jsonify({'sum': result})

        else:
            return jsonify({'error': 'Invalid dataType. Supported values: single, array, json, object.'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


