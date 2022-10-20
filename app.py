from flask import Flask, render_template , request,url_for, redirect, flash
from flask_mysqldb import MySQL


app= Flask(__name__)

app.config['MYSQL_HOST']= 'localhost' 
app.config['MYSQL_USER']= 'root' 
app.config['MYSQL_PASSWORD']= '' 
app.config['MYSQL_DB']= 'contactdb' 

app.secret_key= 'secretkey'

mysql = MySQL(app)
@app.route('/')
def index():
    cursor= mysql.connection.cursor()
    cursor.execute('SELECT * FROM contacto')
    data = cursor.fetchall()
    return render_template('index.html', contacts=data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        name= request.form['nombre']
        apellido=request.form['apellido']
        correo=request.form['correo']
        telefono=request.form['telefono']
        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO contacto (nombre,apellido,correo,telefono) VALUE (%s,%s,%s,%s)',(name,apellido,correo,telefono))
        mysql.connection.commit()
        flash('Contacto agregado satisfactoriamente')
        return redirect(url_for('index'))



@app.route('/edit_contact/<id>')
def edit_contact(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM contacto WHERE id= %s',(id))
    data = cursor.fetchone()
    return render_template('edit-contact.html',contact =data)

@app.route('/update_contact/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        name= request.form['nombre']
        apellido=request.form['apellido']
        correo=request.form['correo']
        telefono=request.form['telefono']
        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE contacto
            SET nombre=%s, apellido=%s, correo=%s, telefono=%s
            WHERE id=%s
        """,(name,apellido,correo,telefono,id))
        mysql.connection.commit()
        flash('Información del contacto actualizada')
        return redirect(url_for('index'))

@app.route('/delete_contact/<string:id>')
def delete_contact(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM contacto WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Se ha borrado satisfactoriamente el contacto')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port= 3000, debug=True)

