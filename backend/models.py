from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(16))  # 'user' or 'agent'
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config.get('DATABASE_URL', 'sqlite:///data.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
