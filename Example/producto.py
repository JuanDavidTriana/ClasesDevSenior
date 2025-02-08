import tkinter as tk
from tkinter import messagebox

productos = {
    1: {"nombre": "Mazana", "precio": 1.5, "stock":100},
    2: {"nombre": "Pera", "precio": 2, "stock":100},
    3: {"nombre": "Sandia", "precio": 3, "stock":100}
}

historial_ventas = []

def obtener_productos(id_producto):
    return productos.get(id_producto,None)

def agregar_producto():
    
    try:
        id_producto = int()
    
        if producto:
            if cantidad <= producto["stock"]:
                historial_ventas.append({producto})
    except:
        print('An exception occurred')
        
def actualizar_lista():
    lista_productos.delete(0, tk.END)
    for id_producto,dato in productos.items():
        lista_productos.insert(tk.END, f"{id_producto}: {dato['nombre']} - ${dato['precio']} - Stock: {dato['stock']}")
    
root = tk.Tk()
root.title("Tienda")

frame = tk.Frame(root)
frame.pack(padx=10)

lista_productos = tk.Listbox(frame,width=50)
lista_productos.pack()
actualizar_lista()

frame_inputs = tk.Frame(root)
frame_inputs.pack(padx=10)

tk.Label(frame_inputs, text=("ID PRODUCTO:")).grid(row=0,column=0)
entre_id = tk.Entry(frame_inputs)
entre_id.grid(row=0, column=1)

root.mainloop()
