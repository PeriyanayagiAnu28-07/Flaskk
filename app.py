from flask import Flask,render_template,url_for,request,redirect
from flask_cors import CORS
from flask import Flask, jsonify
import pymysql
import itertools


app=Flask(__name__)
CORS(app)

class Database :
    def __init__(self):
       host="127.0.0.1"
       user="root"
       password="Peri2020"
       db="crud"
       self.con = pymysql.connect(host=host, user=user, password=password, db=db,cursorclass=pymysql.cursors.DictCursor)
       self.cur= self.con.cursor()
    
    def insert(self,username,password,confirm,address):
        sql="insert into usersdata(username,password,reconfirm,address) values(%s,%s,%s,%s)"
        self.cur.execute(sql,[username,password,confirm,address])
        self.con.commit()
        self.con.close()
        
    def listdata(self):
        self.cur= self.con.cursor()
        sql="select * from usersdata"
        self.cur.execute(sql)
        res=self.cur.fetchall()
        return res
    


@app.route("/")#home page
def home():
    return render_template('home.html');


#register page    
@app.route("/register",methods=['GET','POST'])
def register():
    db=Database() 
    #username='Subha'
    #password='subha123'
    #confirm='subha123'
    #address='Karaikudi'   
    #db.insert(username,password,confirm,address)    
    if request.method=='POST':
       username=request.form['username']
       password=request.form['password']
       confirm=request.form['confirm']
       address=request.form['address']
       
       db.insert(username,password,confirm,address)

       return redirect(url_for('added'))#redirect to added
     #return "registered"
    return render_template('register.html');

@app.route("/listuser",methods=['GET','POST'])
def listuser():
    db=Database()
    da=db.listdata()
    #print(da)
    return {"data":da}
    #flash('List of users')
    #return render_template('listuser.html',data=da)
    
    
@app.route("/added",methods=['POST','GET'])
def added():
    #return "added"
    return render_template('add.html')

if __name__=='__main__':
   app.run(debug=True)