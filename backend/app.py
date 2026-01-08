
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from .models import db, Message, init_db
from .deepseek_client import call_deepseek
from .config import Config
import os

import os
FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend'))
app = Flask(__name__, static_folder=None)
CORS(app)
app.config.from_object(Config)
init_db(app)

@app.route('/api/query', methods=['POST'])
def query():
    data = request.json
    text = data.get('text')
    msg = Message(role='user', content=text)
    db.session.add(msg)
    db.session.commit()
    reply = call_deepseek(text)
    rmsg = Message(role='agent', content=reply)
    db.session.add(rmsg)
    db.session.commit()
    return jsonify({'reply': reply})


# 静态文件和首页路由
@app.route('/')
def index():
    return send_from_directory(FRONTEND_DIR, 'index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(os.path.join(FRONTEND_DIR, 'static'), filename)

if __name__ == '__main__':
    app.run(debug=True)
