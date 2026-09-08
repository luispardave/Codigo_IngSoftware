import tkinter as tk

root = tk.Tk()
root.title("Ventana Principal")
root.geometry("800x700")

#Etiquetas
label = tk.Label(root, text="Etiqueta", bg="orange", fg="black")
label.pack(pady=10)

#Botones
button = tk.Button(root, text="Botón", bg="green", fg="white")
button.pack(pady=10)


root.mainloop()

