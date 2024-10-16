from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return {"message": "Welcome to the Genetic Variant Annotator API!"}, 200

@app.route('/annotate', methods=['POST'])
def annotate():
    data = request.get_json()
    annotations = []
    for variant in data.get('variants', []):
        annotations.append({
            "id": variant["id"],
            "annotation": "mock data for testing"
        })
    return jsonify(annotations), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)

