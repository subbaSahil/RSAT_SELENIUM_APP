from flask import Flask, request, jsonify
import os
from scriptGenerator import getScript
from xmlConverter import extract_user_actions
from flask_cors import CORS
from flask import send_file

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
OUTPUT_SCRIPT = "rsat_script.py"


@app.route('/download-script', methods=['GET'])
def download_script():
    try:
        return send_file(OUTPUT_SCRIPT, as_attachment=True)
    except Exception as e:
        return jsonify({'stderr': str(e)}), 500

@app.route('/run-script', methods=['POST'])
def run_script():
    if 'file' not in request.files:
        return jsonify({'stderr': 'No file uploaded'}), 400

    file = request.files['file']
    filename = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filename)

    try:
        extract_user_actions(filename)
        selenium_data = getScript()

        # Save the script to a .py file
        with open(OUTPUT_SCRIPT, "w", encoding="utf-8") as f:
            f.write(selenium_data)

        return jsonify({'stdout': selenium_data})
    except Exception as e:
        return jsonify({'stderr': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
