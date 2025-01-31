import tkinter as tk

def convertir():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        resultado.config(text=f"Resultado: {fahrenheit:.2f}°F")
    except:
        resultado.config(text="Ingrese un numero valido")

#Configuracion de la ventana
ventana = tk.Tk()
ventana.title("Conversor de Temperatura")
ventana.geometry("300x200")

# Widgets
tk.Label(ventana, text="Ingrese temperatura en °C:").pack(pady=5)
entry = tk.Entry(ventana)
entry.pack(pady=5)

tk.Button(ventana, text="Convertir", command=convertir).pack(pady=5)
resultado = tk.Label(ventana, text="Resultado: ")
resultado.pack(pady=5)

ventana.mainloop()