from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .cancer import cancer
    from .diabetic import diabetic

    app.register_blueprint(diabetic, url_prefix='/diabetic')
    app.register_blueprint(cancer,url_prefix='/c')
    
    return app