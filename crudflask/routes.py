from flask import  url_for,redirect,flash,render_template,request
from crudflask import app , db
from crudflask.models import User
from crudflask.forms import InsertForm,UpdateForm


@app.route("/")
def home():
    form = InsertForm()
    users = User.query.all()  
    return render_template('home.html',title='home',users=users,form=form)

@app.route("/insert",methods=['POST'])
def insert():
    form = InsertForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data,phone=form.phone.data)
        db.session.add(user)
        db.session.commit()
        flash("The user has beeen added successfly",'success')
        return redirect(url_for('home'))
       
    return render_template('home.html',title='insert',form=form)


@app.route("/update/<username>",methods=['GET', 'POST'])
def update(username):
    form = UpdateForm()
    user =  User.query.filter_by(username=username).first()
    
    if form.validate_on_submit():
        change=False
        if user.email != form.email.data:
            row = User.query.filter_by(email=form.email.data).first() 
            change=True
            if row:
                flash('Email alredy used , pleaze choose another one','warning')
                return redirect(url_for('home'))
            user.email = form.email.data
            
        if user.username != form.username.data:
            row = User.query.filter_by(username=form.username.data).first() 
            change=True
            if row:
                flash('UserName alredy used , Pleaze choose another one','warning') 
                return redirect(url_for('home'))               
            user.username = form.username.data      
            
        if  user.phone != form.phone.data:  
            row = User.query.filter_by(phone=form.phone.data).first() 
            change=True
            if row:
                flash('Phone alredy used , Pleaze choose another one','warning')
                return redirect(url_for('home'))
            user.phone = form.phone.data                
             
        if change :   
            db.session.commit()
            flash("The user has beeen Update successfly",'success')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        flash("Methos Gett","success")
        form.username.data = user.username
        form.email.data = user.email
        form.phone.data = user.phone
       
    return render_template('home.html',title='home',form=form,user=user)

@app.route("/delete/<username>",methods=['GET', 'POST'])
def delete(username):
    user =  User.query.filter_by(username=username).first()
    db.session.delete(user)
    db.session.commit()
    flash("The user has beeen Update successfly",'success')
    return redirect(url_for('home'))