from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Simulated API endpoint URL (not used in actual API call)
SIMULATED_API_ENDPOINT = 'https://3gzk2i47k7.execute-api.eu-north-1.amazonaws.com/st1/12'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/myresource', methods=['POST'])
def get_sum():
    try:
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
    except ValueError:
        return jsonify({'error': 'Invalid input. Please enter valid numbers.'}), 400
    try:
        result = num1 + num2 
        simulated_response = {'sum': result} 
        return jsonify(simulated_response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
