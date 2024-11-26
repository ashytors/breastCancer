#inisialisasi konfigurasi aplikasi
from flask import Flask
from .routes import bp as routes_bp

def create_app():
    app = Flask(__name__, template_folder='templates')

    #konfigurasi aplikasi
    app.config['UPLOAD_FOLDER'] = './board/static/uploads'
    app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

    #register b;ueprint
    app.register_blueprint(routes_bp)

    return app
