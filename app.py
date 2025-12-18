from flask import Flask, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def home():
    return jsonify(message="Hello, Azure!")

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
