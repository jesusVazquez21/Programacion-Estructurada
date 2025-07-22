from conexionBD import *
import datetime

def registrar(nombre, apellidos, email, contrasena):
    try:
        
        fecha=datetime.datetime.now()
        sql="INSERT INTO usuarios (id, nombre, apellidos, email, password, fecha) VALUES ('%s', '%s', '%s', '%s', '%s');"
        val=(nombre, apellidos, email, contrasena, fecha)
        cursor.execute(sql, val)
        return True
    except:
        return False
    
def iniciar_sesion(email, contrasena):
    try:
        sql="SELECT * FROM usuarios where email=%s and password=%s"
        val=(email, contrasena)
        cursor.execute(sql, val)
        registros=cursor.fetchone()
        if registros:
            return registros
        else:
            return None
    except:
        return None
        