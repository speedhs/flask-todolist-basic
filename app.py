from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATION']= False
db=SQLAlchemy(app)

class Todo(db.Model):
   id=db.Column(db.Integer, primary_key=True)
   title=db.Column(db.String(100))
   complete=db.Column(db.Boolean)

@app.route('/')
def index():
    #show all todo
    list=Todo.query.all()
    print(list)
    return render_template('face.html',list=list)


if __name__=='__main__':
    db.create_all()
    app.run(debug=True)
