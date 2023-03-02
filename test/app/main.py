from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
from datetime import datetime
import pytz

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
app.config['SQLALCHEMY_ECHO'] = True

# sessionを使う際にSECRET_KEYを設定
app.config['SECRET_KEY'] = 'secret_key'  # TODO 後で変える
db = SQLAlchemy(app)

# 所持している本のテーブル
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # room_number = db.Column(db.Integer, nullable=False, unique=True)
    # created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))
    # user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, unique=True)
    # user = db.relationship("User", back_populates="room")
    # room_members = db.relationship("RoomMember", uselist=True, back_populates="room", cascade="all, delete, delete-orphan")
    # pins = db.relationship("Pin", uselist=True, back_populates="room", cascade="all, delete, delete-orphan")

def get_json():
    # jsonリクエストから値取得
    json = request.get_json()
    if type(json) == list:
        data = json[0]
    else:
        data = json
    return data
