from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cocoabeans.db'
db = SQLAlchemy(app)

class User(db.Model):
    username = db.Column(db.String(20), nullable=False, primary_key=True)
    password = db.Column(db.String(20), nullable=False)
    isCommissioner = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<User %r>' % self.username
    
class Commission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20))
    price = db.Column(db.String(5))

    def __repr__(self):
        return '<User %r>' % self.username
    
with app.app_context():
    db.create_all()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        user_var = request.form['user_name']
        user_var2 = request.form['user_pass']
        new_user = User(username=user_var, password=user_var2)

        try: 
            db.session
            db.session.add(new_user)
            db.session.commit()
            return redirect('/')
        
        except:
            return 'Error'

    else:
        users = User.query.order_by(User.username).all()
        return render_template('index.html', users=users)

if __name__== "__main__":
    app.run(debug=True)