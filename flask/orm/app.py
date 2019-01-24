from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#flask
app = Flask(__name__)
#alchemySQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#sqlalchemy 초기화
db = SQLAlchemy(app)
#migrate 초기화
migrate = Migrate(app,db)

#table만들기
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    memo = db.Column(db.Text)
    
    def __repr__(self):
        return f'<User {self.id} : {self.name}, {self.email}>'
    

# if __name__ == '__main__' :
#     app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)

# flask db init
# flask db migrate
# flask db upgrade


# 정리
# Create
# user = User(name ='miz',email='miz@gmail.com')
# db.session.add(user)
# db.session.commit()

#[Read]m
# SELECT * FROM users;
# users = User.query.all() # 복수

# SELECT *FROM users WHERE name='miz' ;
# users = User.query.filter_by(name='miz').all()

# SELECT *FROM users WHERE name='miz' LIMIT 1;
# user = User.query.filter_by(name='miz').first()

# SELECT * FROM userts WHERE id = 2 LIMIT 1;
# user = User.query.get(2)
# user.name
# uner.email
# primary key만 get으로 가져올 수 있음.

# SELECT * FROM users WHERE email LIKE '%miz%';
# users = User.query.filter(User.email.like('%miz%')).all()

# ORDER
# users = User.query.order_by(User.name).all()

# LIMIT
# users = User.query.limit(1).all()

# OFFSET
# users = User.query.offset(2).all()

# ORDER + LIMIT + OFFSET
# users = User.query.order_by(User.name).limit(1).offset(2).all()

# DELETE FROM users WHERE id = 1;
# user = User.query.get(1)
# db.session.delete(user)
# db.session.commit()

# UPDATE users SET name = 'miz' WHERE id = 2;
# user = User.query.get(2)
# user.name = 'miz'
# db.session.commit()