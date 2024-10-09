from flask import Flask, request, jsonify

app = Flask(__name__)

# Example endpoint to annotate genetic variants
@app.route('/annotate', methods=['POST'])
def annotate():
    try:
        # Extract data from the request body
        data = request.get_json()
        variants = data.get('variants', [])
        annotations = []

        # Mock response for testing purposes
        for variant in variants:
            annotations.append({
                "id": variant["id"],
                "annotation": "mock data for testing"
            })

        return jsonify(annotations), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)

