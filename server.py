from flask_app import app
from flask_app.controller import main
import os

if __name__ == "__main__":
    # Heroku requires app to run on host 0.0.0.0 and a dynamic port from the environment
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
