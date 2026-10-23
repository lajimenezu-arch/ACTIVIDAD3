import tkinter as tk
from tkinter import messagebox

class CalculadoraIMC:
    def __init__(self, peso: float, estatura: float) -> None:
        self.peso = peso
        self.estatura = estatura

    def calcular_imc(self) -> float:
        return self.peso / (self.estatura ** 2)

    def obtener_diagnostico(self) -> str:
        imc = self.calcular_imc()
        if imc < 18.5: return "Bajo peso"
        elif imc < 25.0: return "Peso normal"
        elif imc < 30.0: return "Sobrepeso"
        else: return "Obesidad"

class VentanaEventos:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Ejercicio 8.3 - Eventos")
        self.root.geometry("350x250")
        
        tk.Label(self.root, text="Peso (kg):").pack(pady=2)
        self.txt_peso = tk.Entry(self.root)
        self.txt_peso.pack(pady=2)

        tk.Label(self.root, text="Estatura (m):").pack(pady=2)
        self.txt_estatura = tk.Entry(self.root)
        self.txt_estatura.pack(pady=2)

        btn = tk.Button(self.root, text="Calcular", command=self.al_hacer_clic)
        btn.pack(pady=10)
        self.root.bind('<Return>', self.al_hacer_clic)

        self.lbl_res = tk.Label(self.root, text="IMC: -")
        self.lbl_res.pack()

    def al_hacer_clic(self, event=None) -> None:
        try:
            p = float(self.txt_peso.get())
            e = float(self.txt_estatura.get())
            calc = CalculadoraIMC(p, e)
            self.lbl_res.config(text=f"IMC: {calc.calcular_imc():.2f} ({calc.obtener_diagnostico()})")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaEventos(root)
    root.mainloop()
