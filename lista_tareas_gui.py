import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Lista para guardar las tareas
        self.tareas = []

        # Campo de entrada de texto
        self.entrada = tk.Entry(root, width=40)
        self.entrada.pack(pady=10)
        self.entrada.bind("<Return>", self.agregar_tarea)  # Evento al presionar Enter

        # Botones
        boton_agregar = tk.Button(root, text="Añadir Tarea", width=20, command=self.agregar_tarea)
        boton_agregar.pack(pady=5)

        boton_completar = tk.Button(root, text="Marcar como Completada", width=20, command=self.marcar_completada)
        boton_completar.pack(pady=5)

        boton_eliminar = tk.Button(root, text="Eliminar Tarea", width=20, command=self.eliminar_tarea)
        boton_eliminar.pack(pady=5)

        # Listbox para mostrar las tareas
        self.lista_tareas = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.lista_tareas.pack(pady=10)
        self.lista_tareas.bind("<Double-Button-1>", lambda event: self.marcar_completada())  # Doble clic para completar

    def agregar_tarea(self, event=None):
        tarea = self.entrada.get().strip()
        if tarea:
            self.tareas.append({"texto": tarea, "completada": False})
            self.actualizar_lista()
            self.entrada.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Por favor ingresa una tarea.")

    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            index = seleccion[0]
            self.tareas[index]["completada"] = not self.tareas[index]["completada"]
            self.actualizar_lista()
        else:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para marcar como completada.")

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            index = seleccion[0]
            del self.tareas[index]
            self.actualizar_lista()
        else:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para eliminar.")

    def actualizar_lista(self):
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            texto = tarea["texto"]
            if tarea["completada"]:
                texto += " ✔️"
            self.lista_tareas.insert(tk.END, texto)

# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
