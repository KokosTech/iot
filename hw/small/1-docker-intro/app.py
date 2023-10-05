from flask import Flask
from services import marks_service as ms # btw I have no clue how to work with flask, so I'm doing it the JS way

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/tests', methods=['GET'])
def get_tests():
    with open("static/marks.csv") as file:
        return ms.get_average_tests_marks(file)

@app.route('/failed', methods=['GET'])
def get_failed():
    with open("static/marks.csv") as file:
        return ms.get_failing_students(file)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
