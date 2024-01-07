from test_file import User, app, db

u1=User(username='Shahzaib', email='sohail.abbas@isb.nu.edu.pk',address='Joharabad',course='PAI')
u2=User(username='Chacha', email='ammar.masood@isb.nu.edu.pk',address='ISlamabad',course='DS')

with app.app_context():
    db.session.add(u1)
    db.session.add(u2)
    db.session.commit()