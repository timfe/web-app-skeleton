from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect


# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "\x1b@\x97*#\xcc\xe3\xd9\x19\xbaf\\\x1b\xbaJ\x8a\xb6W\x89QI\xf80\x90"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['UPLOAD_FOLDER'] = 'app/data/upload'
    app.debug = True

    db.init_app(app)
    csrf.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .views import views as views_blueprint

    app.register_blueprint(views_blueprint)

    with app.app_context():
        db.create_all()  # create all tables defined in models
        app.debug = True
        return app