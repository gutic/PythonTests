# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk
import tkMessageBox
import tkFileDialog
import time
#consante archivos
arch_usr = 'user.txt'
arch_mov = 'mov.txt'

class Aplicacion(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        contenedor = tk.Frame(self)
        contenedor.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        contenedor.grid_rowconfigure(0, weight=1)
        contenedor.grid_columnconfigure(0, weight=1)

        self.title("prueba py")

        self.frames = {}
        for f in (Login, PaginaUsuario, Puntaje, PaginaAdmin):   #, PaginaUsuario, Puntaje
            frame = f(parent=contenedor, controller=self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.mostrar_frame(Login)

    def mostrar_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()
class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ttk.Label(self, text='Iniciar sesión').grid(row=0, columnspan=2)
        ttk.Label(self, text="Usuario").grid(row=1, column=0)
        ttk.Label(self, text="contraseña").grid(row=2, column =0)
        self.usuario = tk.Entry(self, width=50)
        self.clave = tk.Entry(self, width=50, show='*')
        self.usuario.grid(row=1, column=1)
        self.clave.grid(row=2, column=1)
        btn_login = ttk.Button(self, text='JUGAR', command=self.login)
        btn_login.grid(row=3, columnspan=2)
        btn_admin = ttk.Button(self,text='ABM usuario',
                                command=lambda: controller.mostrar_frame(PaginaUsuario))
        btn_admin.grid(row=4, columnspan=2)
        ttk.Button(self, text="Puntajes", command= lambda:controller.mostrar_frame(Puntaje)).grid(row=5, columnspan=2)
        btn_salir = ttk.Button(self, text='Salir', command=controller.quit)
        btn_salir.grid(row=6, columnspan=2)
        self.controller = controller

    def login(self):
        cod_usuario = 0
        usuario = self.usuario.get()
        clave = self.clave.get()
        existe = False
        try:
            f = open(arch_usr)
            for linea in f:
                registro = linea.split(',')
                if usuario == registro[2] and clave == registro[3].strip():
                    existe = True
                    cod_usuario = registro[0]

            f.close()
        except:
            pass
        if not existe:
            tkMessageBox.showerror('Error','usuario o clave incorrecta')
        else:
            fecha = (time.strftime("%d/%m/%y"))
            import pelota
            pelota.main(cod_usuario, fecha)

class Puntaje(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

class PaginaAdmin(tk.Frame):
    def __init__(self, parent, controller, cod_usuario=0, fecha=0):
        tk.Frame.__init__(self, parent)
        ttk.Label(self, text='JUGAR / PUNTAJE').grid(row=0, columnspan=2)
        self.usuario = cod_usuario
        self.fecha = fecha

    def jugar(self):
        pass

class PaginaUsuario(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # configuracion de los controles y la interfaz grafica
        ttk.Label(self, text='ABM USUARIO', justify=tk.CENTER).grid(row=0, columnspan=3)
        ttk.Label(self, text='BUSCAR POR USUARIO').grid(row=1)
        self.input_buscar = ttk.Entry(self, width=50)
        self.input_buscar.grid(row=1, column=1, padx=10)
        self.input_buscar.focus()
        self.btn_buscar = ttk.Button(self, text='Buscar', command=self.buscar)
        self.btn_buscar.grid(row=1, column=2, padx=10)
        ttk.Label(self, text='NOMBRE:').grid(row=2, column=0)
        self.input_nombre = tk.Entry(self, width=50, state=tk.DISABLED)
        self.input_nombre.grid(row=2, column=1, padx=10)
        ttk.Label(self, text='NOMBRE DE USUARIO:').grid(row=3, column=0)
        self.input_usuario = tk.Entry(self, width=50, state=tk.DISABLED)
        self.input_usuario.grid(row=3, column=1, padx=10)
        ttk.Label(self, text='CLAVE:').grid(row=4, column=0)
        self.input_clave = tk.Entry(self, show='*', width=50, state=tk.DISABLED)
        self.input_clave.grid(row=4, column=1, padx=10)
        grupo_botones = tk.Frame(self)
        btn_nuevo = ttk.Button(grupo_botones, text='Nuevo', command=self.nuevo)
        btn_nuevo.pack(side=tk.LEFT)
        self.btn_guardar = ttk.Button(grupo_botones, text='Guardar',
                                    state=tk.DISABLED, command=self.guardar)
        self.btn_guardar.pack(side=tk.LEFT)
        self.btn_modificar = ttk.Button(grupo_botones, text='Modificar', state=tk.DISABLED,
                                        command=self.modificar)
        self.btn_modificar.pack(side=tk.LEFT)
        self.btn_eliminar = ttk.Button(grupo_botones, text='Eliminar',
                                        state=tk.DISABLED, command=self.eliminar)
        self.btn_eliminar.pack(side=tk.LEFT)
        btn_cancelar = ttk.Button(grupo_botones, text='Cancelar',
                                command= self.cancelar).pack(side=tk.LEFT)
        grupo_botones.grid(row=5, columnspan=3, pady=10)
        self.controller = controller

    def cancelar(self):
        self.activar_buscar()
        self.desactivar_campos()
        self.controller.mostrar_frame(Login)

    def subir_archivo(self):
        '''
            Retorna un diccionario en conformado por cada usuario en el archivo:
            'id' => {'nombre': 'Pepe', usuario: 'pepito', clave: 1234}
        '''
        usuarios = {}
        ultimo_id = 0
        try:
            f = open(arch_usr, 'r')
        except IOError:
            f = open(arch_usr, 'w+')
        for linea in f:
            registro = linea.split(',')
            valores = {'nombre': registro[1], 'usuario' : registro[2], 'clave': registro[3].strip()}
            usuarios[registro[0]] = valores
            if  int(registro[0]) > ultimo_id:
                ultimo_id = int(registro[0])
        f.close()
        return usuarios, ultimo_id

    def limpiar_campos(self):
        self.input_nombre.delete(0, tk.END)
        self.input_usuario.delete(0, tk.END)
        self.input_clave.delete(0, tk.END)

    def desactivar_buscar(self):
        self.input_buscar.config(state=tk.DISABLED)
        self.btn_buscar.config(state=tk.DISABLED)

    def activar_buscar(self):
        self.input_buscar.config(state=tk.NORMAL)
        self.btn_buscar.config(state=tk.NORMAL)

    def activar_campos(self):
        self.input_nombre.config(state=tk.NORMAL)
        self.input_usuario.config(state=tk.NORMAL)
        self.input_clave.config(state=tk.NORMAL)

    def desactivar_campos(self):
        self.input_nombre.config(state=tk.DISABLED)
        self.input_usuario.config(state=tk.DISABLED)
        self.input_clave.config(state=tk.DISABLED)

    def nuevo(self):
        self.limpiar_campos()
        self.desactivar_buscar()
        self.activar_campos()
        self.input_nombre.focus()
        self.btn_guardar.config(state=tk.NORMAL)

    def existe_usuario(self, username):
        # subida del archivo a memoria
        self.usuarios, self.ultimo_id = self.subir_archivo()
        for usuario in self.usuarios.values():
            if usuario['usuario'] == username:
                return True
        return False

    def buscar(self):
        # subida del archivo a memoria
        self.usuarios, self.ultimo_id = self.subir_archivo()
        busqueda = self.input_buscar.get()
        for usuario in self.usuarios.items():
            if busqueda in usuario[1]['usuario']:
                self.limpiar_campos()
                self.activar_campos()
                self.registro_actual = usuario[0]
                self.input_nombre.insert(0, usuario[1]['nombre'])
                self.input_usuario.insert(0, usuario[1]['usuario'])
                self.input_clave.insert(0, usuario[1]['clave'])
                self.btn_modificar.config(state=tk.NORMAL)
                self.btn_eliminar.config(state=tk.NORMAL)
                self.btn_guardar.config(state=tk.DISABLED)
                return
        tkMessageBox.showinfo('Info', 'se han encontrado 0 resultados')
        self.input_buscar.focus()

    def guardar(self):
        usuario = self.input_usuario.get()
        if not self.existe_usuario(usuario):
            nombre = self.input_nombre.get()
            clave = self.input_clave.get()
            self.ultimo_id += 1
            with open(arch_usr, 'a') as f:
                registro = "{0},{1},{2},{3}\n".format(self.ultimo_id, nombre, usuario, clave)
                f.write(registro)
                tkMessageBox.showinfo("Exito", "Usuario guardado con exito!!")
                self.limpiar_campos()
                self.desactivar_campos()
                self.activar_buscar()
                self.btn_guardar.config(state=tk.DISABLED)
        else:
            tkMessageBox.showwarning('Error', 'El nombre de usuario ya existe')
            self.input_usuario.focus()

    def modificar(self):
        '''
            Obtiene los datos ingresados en los campos de texto, elimina el registro
            del diccionario, lo actualizo en el diccionario y reescribe el archivo con
            los nuevos datos
        '''
        nombre = self.input_nombre.get()
        usuario = self.input_usuario.get()
        clave = self.input_clave.get()
        del self.usuarios[self.registro_actual]
        self.usuarios[self.registro_actual] = {'nombre': nombre, 'usuario':usuario, 'clave':clave}
        with open(arch_usr, 'w') as f:
            for usuario in self.usuarios.items():
                registro = "{0},{1},{2},{3}\n".format(usuario[0], usuario[1]['nombre'], usuario[1]['usuario'], usuario[1]['clave'])
                f.write(registro)
        self.limpiar_campos()
        self.desactivar_campos()
        self.btn_modificar.config(state=tk.DISABLED)
        self.btn_eliminar.config(state=tk.DISABLED)
        tkMessageBox.showinfo('Exito!!', 'Registro modificado con exito!')

    def eliminar(self):
        '''
            elimina el registro del diccionario y reescribe el archivo sin dicho registro
        '''
        res = tkMessageBox.askyesno('Elimar', 'Esta seguro de eliminar el registro?')
        if res == tk.YES:
            del self.usuarios[self.registro_actual]
            with open(arch_usr, 'w') as f:
                for usuario in self.usuarios.items():
                    registro = "{0},{1},{2},{3}\n".format(usuario[0], usuario[1]['nombre'], usuario[1]['usuario'], usuario[1]['clave'])
                    f.write(registro)
            self.limpiar_campos()
            self.desactivar_campos()
            self.btn_modificar.config(state=tk.DISABLED)
            self.btn_eliminar.config(state=tk.DISABLED)
            tkMessageBox.showinfo('Exito!!', 'Registro eliminado con exito!')




if __name__== '__main__':
    app = Aplicacion()
    app.mainloop()
