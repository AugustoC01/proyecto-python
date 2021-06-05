import tkinter
from tkinter import *
from tkinter import messagebox as mb
import sqlite3

class Aplicacion():
	def __init__(self):
		self.raiz = Tk()
		self.raiz.title("Base de datos")
		self.frame_et = Frame(self.raiz)
		self.frame_cam = Frame(self.raiz)
		self.frame_bot = Frame(self.raiz)
		self.barra_menu = Menu(self.raiz)
		self.raiz.config(menu = self.barra_menu)
		self.frame_bot.pack(side = BOTTOM, pady = 5)
		self.frame_et.pack(side = LEFT)
		self.frame_cam.pack(side = LEFT)

		# Declara base de datos y cursor
		#self.conexion = sqlite3.connect("Base_2")
		#self.cursor = self.conexion.cursor()

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
		self.campo_id.delete(0, len(self.campo_id.get()))
		self.campo_nombre = tkinter.Entry(self.frame_cam, textvariable = self.nombre)
		self.campo_clave = tkinter.Entry(self.frame_cam, show = "*", textvariable = self.clave)
		self.campo_apellido = tkinter.Entry(self.frame_cam, textvariable = self.apellido)
		self.campo_direccion = tkinter.Entry(self.frame_cam, textvariable = self.direccion)
		self.campo_comentarios = tkinter.Entry(self.frame_cam, textvariable = self.comentarios)
		self.boton_crear = tkinter.Button(self.frame_bot, text = "Crear", command = self.crear_entrada)
		self.boton_leer = tkinter.Button(self.frame_bot, text = "Leer", command = self.leer_entrada)
		self.boton_act = tkinter.Button(self.frame_bot, text = "Actualizar", command = self.actualizar_entrada)
		self.boton_borrar = tkinter.Button(self.frame_bot, text = "Borrar", command = self.borrar_entrada)
		
		#MENU SUPERIOR
		self.menu_bbdd = Menu(self.barra_menu, tearoff = 0)
		self.menu_borrar = Menu(self.barra_menu, tearoff = 0)
		self.menu_crud = Menu(self.barra_menu, tearoff = 0)
		self.menu_ayuda = Menu(self.barra_menu, tearoff = 0)
		self.barra_menu.add_cascade(label = "BBDD", menu = self.menu_bbdd)
		self.menu_bbdd.add_command(label = "Conectar", command = lambda: self.conectar_base())
		self.menu_bbdd.add_command(label = "Salir", command = lambda: self.ventana_mensaje(True, ""))
		self.barra_menu.add_cascade(label = "Borrar", menu = self.menu_borrar)
		self.menu_borrar.add_command(label = "Borrar campos", command = lambda: self.borrar_campos())
		self.barra_menu.add_cascade(label = "CRUD", menu = self.menu_crud)
		self.barra_menu.add_cascade(label = "Ayuda", menu = self.menu_ayuda)

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
			
	#CREA TODAS LAS VENTANAS EMERGENTES
	def ventana_mensaje(self, salir, mensaje):
		if salir:
			r = mb.askquestion("Salir", "¿Desea salir de la aplicacion?")
			if r == "yes":
				self.conexion.commit()
				self.conexion.close()
				self.raiz.quit()
		else:
			mb.showinfo("BBDD", mensaje)

	#SE CONECTA A LA BASE DE DATOS Y CREA LA TABLA
	def conectar_base(self):
		self.conexion = sqlite3.connect("Base_2")
		self.cursor = self.conexion.cursor()
		try:
			self.cursor.execute('''
			CREATE TABLE registro_personas(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE VARCHAR(20),
			CLAVE VARCHAR(16),
			APELLIDO VARCHAR(20),
			DIRECCION VARCHAR(30),
			COMENTARIOS VARCHAR(50))
			''')
			self.ventana_mensaje(False, "Base de datos creada")
		except:
			self.ventana_mensaje(False, "Base de datos conectada")

	#VACIA LOS CAMPOS
	def borrar_campos(self):
		self.campo_id.delete(0, len(self.campo_id.get()))
		self.campo_nombre.delete(0, len(self.campo_nombre.get()))
		self.campo_clave.delete(0, len(self.campo_clave.get()))
		self.campo_apellido.delete(0, len(self.campo_apellido.get()))
		self.campo_direccion.delete(0, len(self.campo_direccion.get()))
		self.campo_comentarios.delete(0, len(self.campo_comentarios.get())) 

	#AGREGA UNA NUEVA ENTRADA AL REGISTRO
	def crear_entrada(self):
		lista_datos = (self.nombre.get(), self.clave.get(), self.apellido.get(), self.direccion.get(), self.comentarios.get())
		self.cursor.execute('INSERT INTO registro_personas VALUES (NULL, ?, ?, ?, ?, ?)', lista_datos)
		self.borrar_campos()
		self.ventana_mensaje(False, "Registro creado con exito")

	#MUESTRA LOS DATOS DE UNA ENTRADA INDICANDO NUMERO DE ID
	def leer_entrada(self):
		try:
			self.cursor.execute('SELECT * FROM registro_personas WHERE ID=:num_id', {'num_id': self.id.get()})
			lista_datos = self.cursor.fetchone()
			self.borrar_campos()
			self.campo_id.insert(0, lista_datos[0])
			self.campo_nombre.insert(0, lista_datos[1])
			self.campo_clave.insert(0, lista_datos[2])
			self.campo_apellido.insert(0, lista_datos[3])
			self.campo_direccion.insert(0, lista_datos[4])
			self.campo_comentarios.insert(0, lista_datos[5]) 
		except:
			self.ventana_mensaje(False, "Ese registro no existe")

	#ACTUALIZA DATOS DE UNA ENTRADA EXISTENTE
	def actualizar_entrada(self):
		lista_nuevos = [self.nombre.get(), self.clave.get(), self.apellido.get(), self.direccion.get(), self.comentarios.get()]
		self.cursor.execute('''
							UPDATE registro_personas SET 
							nombre=:nuevo_nombre, clave=:clave_nuevo, 
							apellido=:apellido_nuevo, direccion=:direccion_nuevo,
							comentarios=:comentarios_nuevos
			 				WHERE ID=:num_id''', 
			 				{'nuevo_nombre': lista_nuevos[0], 'clave_nuevo': lista_nuevos[1], 'apellido_nuevo': lista_nuevos[2],
			 				'direccion_nuevo': lista_nuevos[3], 'comentarios_nuevos': lista_nuevos[4], 'num_id': self.id.get()})
		self.ventana_mensaje(False, "Registro actualizado con exito")

	#ELIMINA UNA ENTRADA DE LA BASE DE DATOS
	def borrar_entrada(self):
		self.cursor.execute('DELETE FROM registro_personas WHERE ID=:num_id', {'num_id': self.id.get()})
		self.borrar_campos()
		self.ventana_mensaje(False, "Registro borrado con exito")

def main():
    mi_app = Aplicacion()

if __name__ == '__main__':
	main()