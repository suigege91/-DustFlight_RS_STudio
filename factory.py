from flask import Flask
from flask_session import Session
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from configuration.config import Configuration_Development
from apps.DF_Blog_Application import df_blog_application

db = SQLAlchemy()


def app_generator():
    app = Flask(__name__)
    app.config.from_object(Configuration_Development)
    app.register_blueprint(df_blog_application)

    Session(app)
    CSRFProtect(app)
    db.init_app(app)

    @app.route("/app_generator")
    def section_app_generator():
        print("====================================================================================")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("####################################################################################")
        return "<h1>[CONSOLE] Running App_Generator_Tester Successfully !</h1>"
        print("####################################################################################")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("====================================================================================")

    return app
