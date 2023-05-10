from flask import Flask, render_template, request, redirect, session, Response, jsonify
import mysql.connector
import enlace
from flask import make_response
import pdfkit
from bd import connectionBD
import os

from flask_mail import Mail, Message

connection = mysql.connector.connect(host='localhost',
                            user='root',
                            password='Eduar18_12',
                            db='registro')

cursor = connection.cursor()


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'e57147039@gmail.com'
app.config['MAIL_PASSWORD'] = 'xuerdmjucxuhdlld'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



app.secret_key="super secret key"




@app.route("/")
def index_():
    return render_template('login.html')

@app.route("/login.html")
def PedirCita():
    return render_template('login.html')

@app.route("/clinica.html")
def index():
    return render_template('clinica.html', nombre=session['nombre'])

@app.route("/agregar_datos.html")
def formulario_agregar_dato():
    return render_template('agregar_datos.html')

@app.route("/actualizar.html")
def actualizar():
    return render_template('actualizar.html')

@app.route("/Contactanos.html")
def Contactanos():
    return render_template('Contactanos.html')

@app.route("/QuienesSomos.html")
def QuienesSomos():
    return render_template('QuienesSomos.html')

@app.route("/servicios.html")
def servicios():
    return render_template('servicios.html')

@app.route("/pedircita.html")
def pedircita():
    return render_template('pedircita.html')

@app.route("/registro.html")
def registro():
    return render_template('registro.html')

@app.route("/form.html")
def form():
    return render_template('form.html')

@app.route("/nombre.html")
def nombre():
    return render_template('nombre.html')

@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():
    nombre = request.form["nombre"]
    password = request.form["password"]
    gmail = request.form["gmail"]
    Query = f"INSERT INTO registro(nombre, password, gmail) VALUES ('{nombre}', '{password}', '{gmail}')"
    cursor.execute(Query)
    connection.commit()

    return redirect("/login.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    msg=''
    if request.method=='POST':
        nombre =request.form['nombre']
        password = request.form["password"]
        gmail = request.form["gmail"]
        cursor.execute("SELECT nombre, password, gmail FROM registro WHERE nombre=%s AND password=%s AND gmail=%s",(nombre, password, gmail))
        record = cursor.fetchone()
        if record:
            session['logeado']=True
            session['nombre']= record[0]
            return redirect("/clinica.html")
        else:
            msg='no se encontró el usuario'
    return render_template('login.html')

@app.route('/salir')
def salir():
    session.pop('logeado', None)
    session.pop('nombre', None)

    return redirect("/login.html")


@app.route("/guardar_datos", methods=["POST"])
def guardar_datos():
    Nombres = request.form["Nombres"]
    Apellidos = request.form["Apellidos"]
    Fecha_de_nacimiento = request.form["Fecha_de_nacimiento"]
    Direccion = request.form["Direccion"]
    Telefono = request.form["Telefono"]
    Gmail = request.form["Gmail"]
    enlace.insertar_datos(Nombres, Apellidos, Fecha_de_nacimiento, Direccion, Telefono, Gmail)

    return redirect("/datos")


@app.route("/datos")
def datos():
    datos = enlace.obtener_datos()
    return render_template("datos.html", datos=datos)


@app.route("/eliminar_juego", methods=["POST"])
def eliminar_datos():
    enlace.eliminar_datos(request.form["id"])
    return redirect("/datos")


@app.route("/editar_dato/<int:id>")
def editar_dato(id):
    dato = enlace.obtener_datos_por_id(id)
    return render_template("actualizar.html", dato=dato)

@app.route("/pdf/<int:id>")
def pdf(id):
    dato = enlace.obtener_datos_por_id(id)
    return render_template("form.html", dato=dato)


@app.route("/actualizar_dato", methods=["POST"])
def actualizar_dato():
    id = request.form["id"]
    Nombres = request.form["Nombres"]
    Apellidos = request.form["Apellidos"]
    Fecha_de_nacimiento = request.form["Fecha_de_nacimiento"]
    Direccion = request.form["Direccion"]
    Telefono = request.form["Telefono"]
    Gmail = request.form["Gmail"]
    enlace.actualizar_datos(Nombres, Apellidos, Fecha_de_nacimiento, Direccion, Telefono, Gmail, id)

    return redirect("/datos")

@app.route('/pdf', methods =["POST"])
def pdf_imprimir():
    id = request.form["id"]
    Nombres = request.form["Nombres"]
    Apellidos = request.form["Apellidos"]
    Fecha_de_nacimiento = request.form["Fecha_de_nacimiento"]
    Direccion = request.form["Direccion"]
    Telefono = request.form["Telefono"]
    Gmail = request.form["Gmail"]
    enlace.actualizar_datos(Nombres, Apellidos, Fecha_de_nacimiento, Direccion, Telefono, Gmail, id)
    html = render_template("pdf_pdf.html", Nombres=Nombres, Apellidos=Apellidos, Fecha_de_nacimiento=Fecha_de_nacimiento, Direccion=Direccion, Telefono=Telefono, Gmail=Gmail)
    pdf = pdfkit.from_string(html, False)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=output.pdf"
    return response
    return render_template("pdf_pdf.html")


@app.route("/buscar.html")
def buscar():
    return render_template('buscar.html')

@app.route('/', methods=['GET','POST'])
def inicio():
    return render_template('buscar.html')
      
@app.route('/BuscarPacientes', methods=['GET','POST'])
def BuscarPacientes():
    if request.method == "POST":
        search = request.form['buscar']
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)
        querySQL = cur.execute("SELECT * FROM datos WHERE id='%s' ORDER BY id  DESC" % (search,))
        resultadoBusqueda = cur.fetchone()  
        cur.close()
        conexion_MySQLdb.close()
        return render_template('pedircita.html', miData = resultadoBusqueda, busqueda = search)
    return redirect("/pedircita")  

@app.route('/BuscarPaciente', methods=['GET','POST'])
def BuscarPaciente():
    if request.method == "POST":
        search = request.form['buscar']
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)
        querySQL = cur.execute("SELECT * FROM datos WHERE Nombres='%s' ORDER BY id  DESC" % (search,))
        resultadoBusqueda = cur.fetchone()  
        cur.close()
        conexion_MySQLdb.close()
        return render_template('pedircita.html', miData = resultadoBusqueda, busqueda = search)
    return redirect("/pedircita") 

@app.route("/email.html")
def email():
    return render_template('email.html')

@app.route('/create', methods =["POST"])
def create():
    Folio = request.form["Folio"]
    Nombres = request.form["Nombres"]
    Apellidos = request.form["Apellidos"]
    Telefono = request.form["Telefono"]
    Direccion = request.form["Direccion"]
    Fecha = request.form["Fecha"]
    Menu = request.form["Menu"]
    Gmail = request.form["Gmail"]
    enlace.insertar_cita(Folio, Nombres, Apellidos, Telefono, Direccion, Fecha, Menu, Gmail)

    msg = Message('CITA REGISTRADA', sender = 'e57147039@gmail.com', recipients=[Gmail])
    msg.html = render_template("email.html", Folio=Folio, Nombres=Nombres, Apellidos=Apellidos, Telefono=Telefono, Direccion=Direccion, Fecha=Fecha, Menu=Menu, Gmail=Gmail)
    msg.body=Folio
    mail.send(msg)
    
    success= 'USUARIO REGISTRADO Y ENVIADO AL CORREO'
 
    return render_template('buscar.html', success=success) 


@app.route("/ajaxpost",methods=["POST","GET"])
def ajaxpost():
    conexion= connectionBD()
    cur = conexion.cursor()  
    if request.method == 'POST':
        queryString = request.form['queryString']
        print(queryString)
        query = "SELECT * from datos WHERE Nombres LIKE '{}%' LIMIT 10".format(queryString)
        cur.execute(query)
        datos = cur.fetchall()
    return jsonify({'htmlresponse': render_template('response.html', datos=datos)})

if __name__  == '__main__':
    app.run(host='0.0.0.0', port='4000', debug=True) 

