from flask import Flask, request, jsonify
 
app = Flask(__name__)
 
@app.route('/get', methods=['GET'])
def get_endpoint():
    params = request.args
    return jsonify(params)
 
@app.route('/post', methods=['POST'])
def post_endpoint():
    if request.is_json:
        params = request.json
    else:
        params = request.form
        return jsonify(params)
   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)