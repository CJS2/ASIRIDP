from flask import Flask,jsonify,render_template,request,redirect
import pymysql
from ClaseConnect import *

app = Flask(__name__) 

@app.route("/") 
def presentacion():
    return render_template('inicio.html')

@app.route('/add',methods=["GET","POST"])
def add():
    try:
        
        Nombre=request.form.get("Nombre")
        Apellido=request.form.get("Apellido")
        Posicion=request.form.get("Posicion")
        cone=ClaseConnect()
        cone.EjecutarSQL("INSERT INTO jugadores (Nombre,Apellido,Posicion) VALUES('"+Nombre+"','"+Apellido+"','"+Posicion+"')")
        cone.RealizarCambio()
        datos=cone.DevolverDatos()
        print (datos)
    except Exception:
        cone.NoRealizarCambio()
        print ("Error en las altas")
    return redirect("/view")

@app.route("/update",methods=["POST"])
def update():
    id=request.form.get("id")
    nombre=request.form.get("nombre")
    apellido=request.form.get("apellido")
    posicion=request.form.get("posicion")
    cone=ClaseConnect()
    cone.EjecutarSQL("UPDATE jugadores SET nombre='"+nombre+"', apellido='"+apellido+"', posicion='"+posicion+"' WHERE id="+id)
    cone.RealizarCambio()
    return redirect ("/view")

@app.route('/delete',methods=["GET","POST"])
def delete():
    try:     
        id=request.form.get('id')
        cone=ClaseConnect()
        cone.EjecutarSQL("DELETE FROM jugadores WHERE id="+id)
        cone.RealizarCambio()
    except Exception:
        cone.NoRealizarCambio()
        print ("Error en las bajas")
    return redirect("/view")

@app.route("/list") 
def listadoalumnos():
    cone=ClaseConnect()
    cone.EjecutarSQL("SELECT * FROM jugadores")
    datos=cone.DevolverDatos()
    respuesta=jsonify(datos)
    cone.CerrarBaseDatos()
    return respuesta

@app.route("/view") 
def listview():
    cone=ClaseConnect()
    cone.EjecutarSQL("SELECT * FROM jugadores")
    data=cone.DevolverDatos()
    cone.CerrarBaseDatos()
    return render_template('lista.html',datos=data)

@app.route("/all") 
def listall():
    cone=ClaseConnect()
    cone.EjecutarSQL("SELECT * FROM jugadores")
    data=cone.DevolverDatos()
    cone.CerrarBaseDatos()
    return render_template('añadir.html',datos=data)



@app.route("/acdel")
def listactdel():
    cone=ClaseConnect()
    cone.EjecutarSQL("SELECT * FROM jugadores")
    data=cone.DevolverDatos()
    cone.CerrarBaseDatos()
    return render_template('bajayactualizar.html',datos=data)

if __name__ == "__main__": #__main__programa principal
    app.run()







