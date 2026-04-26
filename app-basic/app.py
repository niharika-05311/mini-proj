from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return "App Working"

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name', '')
    if name == "":
        return "Error: Name required"
    return f"Registered {name}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)