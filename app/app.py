from flask import Flask
app= Flask(__name__)

from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
import psycopg2


   

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:12345@host.docker.internal:5432/Test'
db=SQLAlchemy(app)
from app import db

class Employee2(db.Model):
    __tablename__='Employee2'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(150),  nullable=False)
    salary = db.Column(db.String(150), nullable=False)
    dept=db.Column(db.String(150), nullable=False)
    
    def __init__(self, username,password, email,salary,dept):
        self.username = username
        self.password = password
        self.email = email
        self.salary = salary
        self.dept = dept

@app.route('/esubmit', methods=['GET','POST'])
def esubmit():
    try:

        




        if request.method=='POST':
            



            print("heloo")
            username =request.form['username']
            password =request.form['password']
            email=request.form['email']
            salary=request.form['salary']
            dept=request.form['dept']

                
  

            employee=Employee2(username,password,email,salary,dept)
            db.session.add(employee)
            db.session.commit()
            return "added successfully"
        else:

         
            return render_template('eadd.html')
        

    except:
        return "error"

@app.route("/")
def index():
    db.create_all()
    
    return "hello world"

   
#    
   
    

if __name__ == '__main__':
    # Running app in debug mode
    #db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)




    






 
