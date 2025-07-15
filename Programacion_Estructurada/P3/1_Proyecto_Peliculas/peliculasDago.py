# peliculas=[]

#dict u objeto para almacenar los atributos (nombre, categoria, clasificacion, genero e idioma)

# peliculas={
#           "nombre":"",
#           "categoria":"",
#           "clasificacion:"",
#           "genero":"",
#           "idioma":""
import mysql.connector
from mysql.connector import Error

pelicula={}


def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("\n\t...Oprima cualquier tecla para continuar ...")
  input()  

def conectarDB():
  try:
    conexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd_peliculas"   
    )
    return conexion
  except Error as e:
    print(f"El error que sucedio es: {e}")
    return None

def crearPeliculas():
  borrarPantalla()
  conexionBd=conectarDB()
  if conexionBd!=None:
    print("\U0001F4DD  .:: Alta de Películas ::. \n")  # 📝
  pelicula.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
  pelicula.update({"categoria":input("Ingresa la categoria: ").upper().strip()})
  pelicula.update({"clasificacion":input("Ingresa la clasificacion: ").upper().strip()})
  pelicula.update({"genero":input("Ingresa el genero: ").upper().strip()})
  pelicula.update({"idioma":input("Ingresa el idioma: ").upper().strip()})
  ############### AGREGAR REGISTRO A LA BASE DE DATOS
  try:
    cursor=conexionBd.cursor()
    sql=(
      "INSERT INTO peliculas (id, nombre, categoria, clasificacion, genero, idioma) VALUES (NULL, %s, %s, %s, %s, %s)"
          #  (
          #      pelicula["nombre"],
          #      pelicula["categoria"],
          #      pelicula["clasificacion"],
          #      pelicula["genero"],
          #      pelicula["idioma"]
          #  )
    )
    val=(pelicula['nombre'], pelicula['categoria'], pelicula['clasificacion'], pelicula['genero'], pelicula['idioma'])
    
    cursor.execute(sql, val)
    conexionBd.commit()
    print("\n\t\U0001F389 ..:::: La operación se realizó con éxito :::..")  # 🎉
  except Error as e:
    print(f"Erros al intentar insertar un registro en la base de datos {e}")
  
  # cursor.execute("INSERT INTO peliculas {id, nombre, categoria, clasificacion, genero, idioma} VALUES {NULL, %s, %s, %s, %s, %s}, (pelicula['nombre'], pelicula['categoria'], pelicula['clasificacion'], pelicula['genero'], pelicula['idioma'])")
  
def mostrarPeliculas():
  borrarPantalla()
  conexion=conectarDB()
  
  cursor= conexion.cursor()
  sql=("SELECT * FROM peliculas")
  cursor.execute(sql)
  registros=cursor.fetchall()
  
  if registros:
    print("\n \U0001F50D  .:: Mostrar Películas ::. \n")  # 🔍
    print(f"{'|'}{'id':<10} {'|'}{'nombre':<20} {'|'}{'categoria':<20}{'|'}{'clasificacion':<15}{'|'}{'genero':<16}{'|'}{'idioma':<17}{'|'}")
    print(f"{'-'*120}")
    for fila in registros:
      print(f"{'|'}{fila [0]:<10}{'|'} {fila [1]:<20}{'|'} {fila [2]:<20}{'|'} {fila [3]:<15}{'|'} {fila [4]:<16}{'|'} {fila [5]:<17}{'|'}")
  else: 
    print("\t\u274C No hay películas en el sistema.")  # ❌

def borrarPeliculas():
   borrarPantalla()
   conexion=conectarDB()
  
   cursor= conexion.cursor()
   nombre=input("Dame el nombre de la pelicula a borrar: ").lower().strip()
   sql=("SELECT * FROM peliculas where nombre=%s")
   val=(nombre,)
   cursor.execute(sql,val)
   registros=cursor.fetchall()
  
   if registros:
     print("\n \U0001F50D  .:: Mostrar Películas ::. \n")  # 🔍
     print(f"{'|'}{'id':<10} {'|'}{'nombre':<20} {'|'}{'categoria':<20}{'|'}{'clasificacion':<15}{'|'}{'genero':<16}{'|'}{'idioma':<17}{'|'}")
     print(f"{'-'*120}")
     for fila in registros:
        print(f"{'|'}{fila [0]:<10}{'|'} {fila [1]:<20}{'|'} {fila [2]:<20}{'|'} {fila [3]:<15}{'|'} {fila [4]:<16}{'|'} {fila [5]:<17}{'|'}")
     resp=input(f"¿Deseas borrar la pelicula de {nombre}? (SI/NO): ").lower().strip()
     if resp=="si":
       sql="DELETE FROM peliculas WHERE nombre=%s"
       val=(nombre, )
       cursor.execute(sql, val)
       conexion.commit()
       input("\n\t..:::: La operacion se realizo con exito::::.. ✅")
     else:
       print("\t..::La accion se canceló con exito::..")
      # print("\n \U0001F50D  .:: Buscar Películas ::. \n")  # 🔍
      # print(f"{'|'}{'id':<8} {'|'}{'nombre':<19} {'|'}{'categoria':<20}{'|'}{'clasificacion':<15}{'|'}{'genero':<16}{'|'}{'idioma':<17}{'|'}")
      # print(f"{'-'*112}")
      # for fila in registros:
      #   print(f"{'|'}{fila [0]:<10}{'|'} {fila [1]:<20}{'|'} {fila [2]:<20}{'|'} {fila [3]:<15}{'|'} {fila [4]:<16}{'|'} {fila [5]:<17}{'|'}")
   else: 
      print("\t\u274C Esta a eliminar no se encuentra en el sistema.")  # ❌

def buscarPeliculas():
  borrarPantalla()
  conexion=conectarDB()
  
  cursor= conexion.cursor()
  nombre=input("Dame el nombre de la pelicula a buscar: ").lower().strip()
  sql=("SELECT * FROM peliculas where nombre=%s")
  val=(nombre,)
  cursor.execute(sql,val)
  registros=cursor.fetchall()
  
  if registros:
    print("\n \U0001F50D  .:: Buscar Películas ::. \n")  # 🔍
    print(f"{'|'}{'id':<8} {'|'}{'nombre':<19} {'|'}{'categoria':<20}{'|'}{'clasificacion':<15}{'|'}{'genero':<16}{'|'}{'idioma':<17}{'|'}")
    print(f"{'-'*112}")
    for fila in registros:
      print(f"{'|'}{fila [0]:<10}{'|'} {fila [1]:<20}{'|'} {fila [2]:<20}{'|'} {fila [3]:<15}{'|'} {fila [4]:<16}{'|'} {fila [5]:<17}{'|'}")
  else: 
    print("\t\u274C Esta pelicula no existe.")  # ❌

def modificarPeliculas():
  borrarPantalla()
  conexion=conectarDB()
  cursor=conexion.cursor()
  nombre=input("Dame el nombre de la pelicula a modificar: ").lower().strip()
  sql=("SELECT * FROM peliculas where nombre=%s")
  val=(nombre,)
  cursor.execute(sql,val)
  registros=cursor.fetchall()

  if registros:
      print("\n \U0001F50D  .:: Mostrar Películas ::. \n")  # 🔍
      print(f"{'|'}{'id':<10} {'|'}{'nombre':<20} {'|'}{'categoria':<20}{'|'}{'clasificacion':<15}{'|'}{'genero':<16}{'|'}{'idioma':<17}{'|'}")
      print(f"{'-'*120}")
      for fila in registros:
        print(f"{'|'}{fila [0]:<10}{'|'} {fila [1]:<20}{'|'} {fila [2]:<20}{'|'} {fila [3]:<15}{'|'} {fila [4]:<16}{'|'} {fila [5]:<17}{'|'}")
        resp=input(f"¿Deseas actualizar la pelicula de {nombre}? (SI/NO): ").lower().strip()
      if resp=="si":
        pelicula["nombre"]=input("nombre: ").lower().strip()
        pelicula["categoria"]=input("categoria: ").lower().strip()
        pelicula["clasificacion"]=input("clasificacion: ").lower().strip()
        pelicula["genero"]=input("genero: ").lower().strip()
        pelicula["idioma"]=input("idioma: ").lower().strip()
        sql=" UPDATE peliculas SET nombre = %s, categoria = %s, clasificacion = %s, genero = %s, idioma = %s WHERE nombre = %s"
        val=(pelicula['nombre'], pelicula['categoria'], pelicula['clasificacion'], pelicula['genero'], pelicula['idioma'], nombre)
        cursor.execute(sql, val)
        conexion.commit()
        input("\n\t..:::: La operacion se realizo con exito::::.. ✅")
      else:
       print("\t..::La accion se canceló con exito::..")
  else: 
      print("\t\u274C Esta a eliminar no se encuentra en el sistema.")  # ❌


# def consultarPeliculas():
#   borrarPantalla()
#   print("\n\t.:: Consultar Peliculas ::.")
#   if len(peliculas)>0:
#     for i in range(0,len(peliculas)):
#       print(f"{i+1}: {peliculas[i]}")
#   else:
#     print("No hay peliculas en el sistema")
    
# def vaciarPeliculas():
#     borrarPantalla()
#     print("\n\t..:::Borrar o Eliminar Todas las peliculas::..")
#     resp=input("Deseas quitar o borrar todas las peliculas del sistema? SI/NO ").upper()
#     if resp=="SI":
#         peliculas.clear()
#         input("\n\t..:::: La operacion se realizo con exito::::..")
#     else:
#         input("\n\t..:::: Volviendo atras::::..")
        
# def buscarPeliculas():
#     borrarPantalla()
#     print("\n\t..:: Buscar peliculas::..")
#     pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
#     encontro=0
#     if not(pelicula_buscar in peliculas):
#         print("\n\t\t..::No se encontró la pelicula a buscar")
#     else:
#         for i in range(0,len(peliculas)):
#             if pelicula_buscar==peliculas[i]:
#                 print(f"La pelicula {pelicula_buscar} si la tenemos y esta en la casilla {i+1}")
#                 encontro+=1
#         if encontro>0:
#             print(f"Tenemos {encontro} peliculas con este titulo")
#             input("\n\t..:::: La operacion se realizo con exito::::..")
            
# def eliminarPeliculas():
#     borrarPantalla()
#     print("\n\t..:: Borrar peliculas::..")
#     pelicula_borrar=input("Ingrese el nombre de la pelicula que desea borrar: ").upper().strip()
#     found=0
#     if not(pelicula_borrar in peliculas):
#         print("No se encontro ninguna pelicula con ese nombre")
#     else: 
#         respuesta="SI"
#         while pelicula_borrar in peliculas and respuesta=="SI":
#             respuesta=input("¿Deseas quitar o borrar la pelicula del sistema? SI/NO ").upper()
#             if respuesta=="SI":
#                 posicion=peliculas.index(pelicula_borrar)
#                 print(f"La pelicula que se borró fue {pelicula_borrar} y estaba en la casilla {posicion+1}")
#                 peliculas.remove(pelicula_borrar)
#                 found+=1
#                 input("\n\t...:: La operacion se realizó con exito::..")
#         print(f"Se borro {found} pelicula(s) con este titulo")        

# def modificarPelicula():
  #  borrarPantalla()
  #  print("\n\t.:: Modificar Películas ::. \n")
  #  pelicula_buscar=input("Ingrese el nombre de la película que desea buscar: ").upper().strip()
  #  encontro=0
  #  if not(pelicula_buscar in peliculas): 
  #     print("\n\t\t ¡No se encuentra la película a buscar!")   
  #  else:   
  #     for i in range(0,len(peliculas)):
  #       if pelicula_buscar==peliculas[i]:
  #         resp=input("¿Deseas actualizar la pelicula? (Si/No) ").lower()
  #         if resp=="si":
  #            peliculas[i]=input("\nIntroduce el nuevo nombre de la película: ").upper().strip()
  #            encontro+=1
  #            print("\n\t\t::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
      
  #     print(f"\nSe modifico {encontro} pelicula(s) con este titulo")
