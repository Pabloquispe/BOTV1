from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_session import Session
import os

app = Flask(__name__, template_folder='app/main/templates')
app.config.from_object(os.getenv('FLASK_CONFIG') or 'default')

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# Session(app)

@app.route('/')
def home():
    return "Hello, World!"

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)

