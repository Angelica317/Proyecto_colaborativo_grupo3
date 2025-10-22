from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite que el frontend acceda al backend

@app.route('/courses', methods=['GET'])
def get_courses():
    courses = [
        {"name": "Introducción a la Programación", "duration": "6 semanas"},
        {"name": "Inteligencia Artificial Básica", "duration": "8 semanas"},
        {"name": "Desarrollo Web", "duration": "10 semanas"}
    ]
    return jsonify(courses)

if __name__ == '__main__':
    app.run(debug=True)
