from flask import Flask, request, jsonify

app = Flask(__name__)

def is_valid_string(s):
    # DFA logic for (0+1)*
    for char in s:
        if char not in ['0', '1']:
            return False
    return True

@app.route('/process', methods=['POST'])
def process_string():
    data = request.get_json()
    input_string = data['inputString']
    result = "Accepted" if is_valid_string(input_string) else "Rejected"
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
