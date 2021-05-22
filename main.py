import tkinter
from tkinter import *
import sqlite3

class Aplicacion():
	def __init__(self):
		self.raiz = Tk()
		self.raiz.title("Base de datos")
		self.frame_et = Frame(self.raiz)
		self.frame_cam = Frame(self.raiz)
		self.frame_bot = Frame(self.raiz)
		self.frame_bot.pack(side = BOTTOM, pady = 5)
		self.frame_et.pack(side = LEFT)
		self.frame_cam.pack(side = LEFT)

		# Declara base de datos
		self.conexion = sqlite3.connect("Base_2")
		self.cursor = self.conexion.cursor()

		# Declara variables de control
		self.id = IntVar()
		self.nombre = StringVar()
		self.clave = StringVar()
		self.apellido = StringVar()
		self.direccion = StringVar()
		self.comentarios = StringVar()

		# Declara widgets de la self.raiz
        # Se incluye el widget de tipo Button 'Crear' 'Leer' 'Actualizar' 'Borrar' 
		self.et_id = tkinter.Label(self.frame_et, text = "ID")
		self.et_nombre = tkinter.Label(self.frame_et, text = "Nombre")
		self.et_clave = tkinter.Label(self.frame_et, text = "Clave")
		self.et_apellido = tkinter.Label(self.frame_et, text = "Apellido")
		self.et_direccion = tkinter.Label(self.frame_et, text = "Direccion")
		self.et_comentarios = tkinter.Label(self.frame_et, text = "Comentarios")
		self.campo_id = tkinter.Entry(self.frame_cam, textvariable = self.id)
		self.campo_nombre = tkinter.Entry(self.frame_cam, textvariable = self.nombre)
		self.campo_clave = tkinter.Entry(self.frame_cam, show = "*", textvariable = self.clave)
		self.campo_apellido = tkinter.Entry(self.frame_cam, textvariable = self.apellido)
		self.campo_direccion = tkinter.Entry(self.frame_cam, textvariable = self.direccion)
		self.campo_comentarios = tkinter.Entry(self.frame_cam, textvariable = self.comentarios)
		self.boton_crear = tkinter.Button(self.frame_bot, text = "Crear", command = self.crear_entrada)
		self.boton_leer = tkinter.Button(self.frame_bot, text = "Leer", command = self.leer_entrada)
		self.boton_act = tkinter.Button(self.frame_bot, text = "Actualizar", command = self.actualizar_entrada)
		self.boton_borrar = tkinter.Button(self.frame_bot, text = "Borrar", command = self.borrar_entrada)

		self.et_id.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 5)
		self.et_nombre.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 5)
		self.et_clave.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 5)
		self.et_apellido.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 5)
		self.et_direccion.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 5)
		self.et_comentarios.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 5)
		self.campo_id.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 5)
		self.campo_nombre.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 5)
		self.campo_clave.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 5)
		self.campo_apellido.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 5)
		self.campo_direccion.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 5)
		self.campo_comentarios.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 5)
		self.boton_crear.pack(side = LEFT, fill = BOTH, expand = True, padx = 10, pady = 5)
		self.boton_leer.pack(side = LEFT, fill = BOTH, expand = True, padx = 10, pady = 5)
		self.boton_act.pack(side = LEFT, fill = BOTH, expand = True, padx = 10, pady = 5)
		self.boton_borrar.pack(side = LEFT, fill = BOTH, expand = True, padx = 10, pady = 5)
		self.raiz.mainloop()
		self.conexion.commit()
		self.conexion.close()
	
	def crear_tabla(self):
		try:
			self.cursor.execute('''
			CREATE TABLE if not exists registro_personas(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE VARCHAR(20),
			CLAVE VARCHAR(16),
			APELLIDO VARCHAR(20),
			DIRECCION VARCHAR(30),
			COMENTARIOS VARCHAR(50))
			''')
		except:
			print("La base de datos ha sido creada")			

	def crear_entrada(self):
		self.crear_tabla()
		lista_datos = (self.nombre.get(), self.clave.get(), self.apellido.get(), self.direccion.get(), self.comentarios.get())
		self.cursor.execute('INSERT INTO registro_personas VALUES (NULL, ?, ?, ?, ?, ?)', lista_datos)

	
		#AGREGAR UN TRY A LA LECTURA PARA Q NO SE BUGUEE SI NO EXISTE EL DATO CONSULTADO
		#FIJARSE PORQUE APARECE UN 0 EN ID CADA VEZ Q EJECUTO

	def leer_entrada(self):
		self.cursor.execute('SELECT * FROM registro_personas WHERE ID=:num_id', {'num_id': self.id.get()})
		lista = self.cursor.fetchone()
		self.campo_nombre.delete(0, len(self.campo_nombre.get()))
		self.campo_clave.delete(0, len(self.campo_clave.get()))
		self.campo_apellido.delete(0, len(self.campo_apellido.get()))
		self.campo_direccion.delete(0, len(self.campo_direccion.get()))
		self.campo_comentarios.delete(0, len(self.campo_comentarios.get())) 
		self.campo_nombre.insert(0, lista[1])
		self.campo_clave.insert(0, lista[2])
		self.campo_apellido.insert(0, lista[3])
		self.campo_direccion.insert(0, lista[4])
		self.campo_comentarios.insert(0, lista[5]) 

	def actualizar_entrada(self):
		pass

	def borrar_entrada(self):
		pass	

def main():
    mi_app = Aplicacion()

if __name__ == '__main__':
	main()