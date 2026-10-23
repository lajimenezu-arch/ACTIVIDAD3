import tkinter as tk
from tkinter import messagebox

class VentanaPrincipal:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Ejercicio 8.2 - Componentes")
        self.root.geometry("380x250")
        self._construir_gui()

    def _construir_gui(self) -> None:
        tk.Label(self.root, text="Nombre del Estudiante:").pack(pady=(15, 2))
        self.txt_nombre = tk.Entry(self.root, width=35)
        self.txt_nombre.pack(pady=2)

        tk.Label(self.root, text="Edad:").pack(pady=(10, 2))
        self.txt_edad = tk.Entry(self.root, width=35)
        self.txt_edad.pack(pady=2)

        btn_procesar = tk.Button(self.root, text="Registrar", command=self.procesar_datos)
        btn_procesar.pack(pady=15)

        self.lbl_resultado = tk.Label(self.root, text="")
        self.lbl_resultado.pack(pady=5)

    def procesar_datos(self) -> None:
        nombre = self.txt_nombre.get().strip()
        edad_str = self.txt_edad.get().strip()
        if nombre and edad_str.isdigit():
            self.lbl_resultado.config(text=f"Estudiante {nombre} registrado con éxito.")
        else:
            messagebox.showerror("Error", "Ingrese datos válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()
