from flask import Flask, request, jsonify, send_file
import os
import zipfile
from scriptGenerator2 import getScript
from xmlConverter import extract_user_actions
from flask_cors import CORS
import traceback
 
app = Flask(__name__)
CORS(app)
 
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'tests'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
 
@app.route('/run-script', methods=['POST'])
def run_script():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded', 'scripts': {}}), 400
 
    files = request.files.getlist('file')
    results = {}
 
    for file in files:
        filename = file.filename
        base_name = os.path.splitext(filename)[0]
        input_path = os.path.join(UPLOAD_FOLDER, filename)
        output_script_path = os.path.join(OUTPUT_FOLDER, f'script_{base_name}_test.py')
 
        try:
            file.save(input_path)
            extract_user_actions(input_path)  # Process XML
            selenium_data = getScript('output.xml')  # Adjust if needed
 
            with open(output_script_path, 'w', encoding='utf-8') as f:
                f.write(selenium_data)
 
            results[filename] = selenium_data
        except Exception as e:
            results[filename] = f"Error: {str(e)}\n{traceback.format_exc()}"
 
    return jsonify({
        "message": "Script(s) generated successfully.",
        "scripts": results
    })
 
@app.route('/download-all-scripts', methods=['GET'])
def download_all_scripts():
    zip_path = "all_scripts.zip"
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in os.listdir(OUTPUT_FOLDER):
            if file.endswith(".py"):
                zipf.write(os.path.join(OUTPUT_FOLDER, file), arcname=file)
    return send_file(zip_path, as_attachment=True)
 
if __name__ == '__main__':
    app.run(debug=True)
 
 




 # import subprocess  # Add at top if not already

# @app.route('/execute-generated-script', methods=['POST'])
# def execute_generated_script():
#     try:
#         result = subprocess.run(['python', OUTPUT_SCRIPT], capture_output=True, text=True, timeout=60)
#         return jsonify({
#             'stdout': result.stdout,
#             'stderr': result.stderr
#         })
#     except subprocess.TimeoutExpired:
#         return jsonify({'stderr': 'Script execution timed out'}), 500
#     except Exception as e:
#         return jsonify({'stderr': str(e)}), 500
