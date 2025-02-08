import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

#Variable
clientes = []
mascotas = []

#Clases principales
class SistemaVeterinaria:
    class Persona:
        id_counter = 1
        
        def __init__(self,nombre,contacto):
            self.id = SistemaVeterinaria.Persona.id_counter
            self.nombre = nombre
            self.contacto = contacto
            
            SistemaVeterinaria.Persona.id_counter += 1

    class Cliente(Persona):
        def __init__(self, nombre, contacto,direccion):
            super().__init__(nombre, contacto)
            self.direccion = direccion
            self.mascotas = []
            
        def agregar_mascota(self,mascota):
            self.mascotas.append(mascota)

    class Mascota:
        id_counter = 1
        
        def __init__(self,nombre,especie,raza,edad):
            self.id = SistemaVeterinaria.Mascota.id_counter
            self.nombre = nombre 
            self.especie = especie
            self.raza = raza
            self.edad = edad
            self.historia_clinico= []
            
            SistemaVeterinaria.Mascota.id_counter += 1
            
        def agregar_cita(self,cita):
            self.historia_clinico.append(cita)
            
        def mostar_historial(self):
            return self.historia_clinico
            
    class Cita:
        id_counter = 1
        
        def __init__(self,fecha,hora,servicio,veterinario):
            self.id = SistemaVeterinaria.Cita.id_counter
            self.fecha = fecha
            self.hora = hora
            self.servicio = servicio
            self.veterinario = veterinario
            
            SistemaVeterinaria.Cita.id_counter += 1


#Funciones auxiliares
def validar_fecha(fecha):
    from datetime import datetime
    try:
        datetime.strptime(fecha,"%Y-%m-%d")
        return True
    except ValueError:
        return False


#Funciones del sistemas 
def registrar_cliente(nombre,contacto,direccion): #Modificar
    cliente = SistemaVeterinaria.Cliente(nombre,contacto,direccion)
    clientes.append(cliente)
    messagebox.showinfo("Exito",f"Cliente registrado con exito. ID: {cliente.id}")
    
def registar_mascota(cliente_id, nombre_mascota,especie,raza, edad): #Modificar

    cliente = next((c for c in clientes if c.id == cliente_id), None)
    
    if not cliente:
        messagebox.showerror("Error", "Cliente no encontrado.")
        return 
    
    mascota = SistemaVeterinaria.Mascota(nombre_mascota,especie,raza,edad)
    cliente.agregar_mascota(mascota)
    mascotas.append(mascota)
    
    messagebox.showinfo("Exito",f"Mascota registrada con exito, ID :{mascota.id}")

def programar_cita(): #Modificar
    
    cliente_id = int(input("Ingrese el ID del cliente: "))
    cliente = next((c for c in clientes if c.id == cliente_id), None)
    
    if not cliente:
        print("Cliente no encontrado.")
        return
    
    mascota_id = int(input("Ingrese el ID del mascota: "))
    mascota = next((m for m in cliente.mascotas if m.id == mascota_id), None)
    
    if not mascota:
        print("Mascota no encontrado.")
        return
    
    fecha = input("Ingrese la fecha de la cita(YYYY-MM-DD): ")
    while not validar_fecha(fecha):
        print("Fecha invalida, Por Favor, use el formato YYYY-MM-DD")
        fecha = input("Ingrese la fecha de la cita(YYYY-MM-DD): ")
    hora = input("Ingrese la hora de la cita (HH:MM): ")
    servicio = input("Ingrese el servicio(Consultoria, vacunacion, etc.): ")
    veterinario = input("Ingrese nombre de Veterinario: ")
    
    cita = SistemaVeterinaria.Cita(fecha,hora,servicio,veterinario)
    mascota.agregar_cita(cita)
    print("Cita agendada")

def consultar_historia(): #Modificar
    
    print("Consultar historial de citas")
    
    cliente_id = int(input("Ingrese el ID del cliente: "))
    cliente = next((c for c in clientes if c.id == cliente_id), None)
    
    if not cliente:
        print("Cliente no encontrado.")
        return
    
    mascota_id = int(input("Ingrese el ID del mascota: "))
    mascota = next((m for m in cliente.mascotas if m.id == mascota_id), None)
    
    if not mascota:
        print("Mascota no encontrado.")
        return

    mascota.mostar_historial()
    
#Interfaz de usuario(Tkinter)
class VeterinariaApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Sistema Veterinaria")
        self.root.geometry("500x500")
        
        self.clientes = clientes
        self.mascotas = mascotas
        
        self.main_menu()
        
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def main_menu(self):
        self.clear_window()
        
        tk.Label(self.root, text="Sitemas Veterinaria", font=("Arial", 16)).pack(pady=10)
        
        tk.Button(self.root, text="Registar Cliente",command=self.registar_cliente).pack(pady=5)
        tk.Button(self.root, text="Registar Mascota",command=self.registar_mascota).pack(pady=5)
        tk.Button(self.root, text="Programar Cita",command="").pack(pady=5)
        tk.Button(self.root, text="Consultar Historial de Citas",command="").pack(pady=5)
        
    def registar_cliente(self):
        self.clear_window()
        
        tk.Label(self.root, text="Registar Clientes",font=("Arial", 16)).pack(pady=10)
        
        tk.Label(self.root, text="Nombre: ").pack(pady=5)
        nombre_entry = tk.Entry(self.root)
        nombre_entry.pack(pady=5)
        
        tk.Label(self.root, text="Contacto: ").pack(pady=5)
        contacto_entry = tk.Entry(self.root)
        contacto_entry.pack(pady=5)
        
        tk.Label(self.root, text="Direccion: ").pack(pady=5)
        direccion_entry = tk.Entry(self.root)
        direccion_entry.pack(pady=5)
        
        def submit_cliente():
            nombre = nombre_entry.get()
            contacto = contacto_entry.get()
            direccion = direccion_entry.get()
            registrar_cliente(nombre,contacto,direccion)
            self.registar_mascota()
            
        tk.Button(self.root, text="Registar Cliente", command=submit_cliente).pack(pady=20)
        tk.Button(self.root, text="Volver al Menu Principal", command=self.main_menu).pack(pady=20)
        
        
    def registar_mascota(self):
        self.clear_window()
        
        tk.Label(self.root, text="Registar Mascota",font=("Arial", 16)).pack(pady=10)
        
        tk.Label(self.root, text="Id Cliente: ").pack(pady=5)
        cliente_id_entry = tk.Entry(self.root)
        cliente_id_entry.pack(pady=5)
        
        tk.Label(self.root, text="Nombre Mascota: ").pack(pady=5)
        nombre_mascota_entry = tk.Entry(self.root)
        nombre_mascota_entry.pack(pady=5)

        tk.Label(self.root, text="Especie: ").pack(pady=5)
        especie_combobox = ttk.Combobox(self.root, values=["Perro","Gato","Conejo","Pajaro","Otros"])
        especie_combobox.pack(pady=5)
        
        tk.Label(self.root, text="Raza: ").pack(pady=5)
        raza_entry = tk.Entry(self.root)
        raza_entry.pack(pady=5)
        
        tk.Label(self.root, text="Edad: ").pack(pady=5)
        edad_entry = tk.Entry(self.root)
        edad_entry.pack(pady=5)
        
        def submit_mascota():
            cliente_id = int(cliente_id_entry.get())
            nombre_mascota = nombre_mascota_entry.get()
            especie = especie_combobox.get()
            raza = raza_entry.get()
            edad = edad_entry.get()
            registar_mascota(cliente_id,nombre_mascota,especie,raza,edad)
            self.registar_mascota()
            
        tk.Button(self.root, text="Registar Mascota", command=submit_mascota).pack(pady=20)
        tk.Button(self.root, text="Volver al Menu Principal", command=self.main_menu).pack(pady=20)
        
        

root = tk.Tk()
app = VeterinariaApp(root)
root.mainloop()