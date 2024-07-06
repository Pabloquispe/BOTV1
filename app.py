from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class='config.Config'):
    app = Flask(__name__, template_folder='vistas/templates')
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from controladores import main_routes
    app.register_blueprint(main_routes.bp)

    @app.route('/')
    def home():
        return "Hello, World!"

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('500.html'), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

