from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False, nullable=False)
    email=db.Column(db.String(20), unique=False, nullable=False)
    address= db.Column(db.String(20), unique=False, nullable=False)
    course= db.Column(db.String(20), unique=False, nullable=False)

@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

if __name__ == '__main__':
    # This condition ensures that the following code is only executed
    # when the script is run directly (not imported as a module).
    # It will create the database tables when the script is run.
    # Create the Flask app context
    with app.app_context():
        # Create the database tables when the script is run
        db.create_all()
        u1=User(username='Sohail', email='sohail.abbas@isb.nu.edu.pk',address='Joharabad',course='PAI')
        u2=User(username='Ammar Masood', email='ammar.masood@isb.nu.edu.pk',address='ISlamabad',course='DS')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
    app.run(debug=True)