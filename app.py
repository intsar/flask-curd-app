from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="flask_curd"
)



# Home page
@app.route('/')
def index():
    cursor = db.cursor(dictionary=True);
    cursor.execute("SELECT * FROM users");
    data = cursor.fetchall();
    cursor.close();
    return render_template('index.html', data= data);

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        name = request.form.get('name') or request.name
        email = request.form.get('email') or request.email
        phone = request.form.get('phone') or request.phone
        cursor = db.cursor()
        cursor.execute("SELECT * from flask_curd.users where email = %s", (email,))
        emailExists = cursor.fetchone()
        if emailExists :
            error = "Email Id already exists"
            return render_template('add.html', error=error)
        
        cursor.execute("INSERT INTO flask_curd.users (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        db.commit()
        cursor.close()
        return redirect(url_for('index'))
    return render_template('add.html');

@app.route('/delete/<int:id>',methods=['GET'])
def delete(id): 
    cursor = db.cursor()
    cursor.execute("DELETE FROM flask_curd.users where id = %s", (id,))
    db.commit()
    cursor.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    if request.method == 'GET':
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * from users where id = %s", (id,))
        user = cursor.fetchone()
        cursor.close()
        return render_template('edit.html', user = user)
    else :
        name = request.form.get('name') or request.name
        email = request.form.get('email') or request.email
        phone = request.form.get('phone') or request.phone
        cursor = db.cursor()
        cursor.execute(""" UPDATE flask_curd.users 
                       SET name =%s, email = %s, phone = %s 
                       WHERE id=%s 
                       """, (name, email, phone, id))
        db.commit()
        cursor.close()
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)



