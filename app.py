from flask import Flask
from routes import api

app = Flask(__name__)

# Register the blueprint for API routes
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
