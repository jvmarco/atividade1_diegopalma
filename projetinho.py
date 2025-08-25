import tkinter as tk
from tkinter import messagebox

def calcular_bissextos():
    try:
        ano_final = int(entry_ano_final.get())
        ano_ini = 2000
        lista_anos = list(range(ano_ini, ano_final + 1))
        ano_bissexto = 0

        for ano in lista_anos:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                ano_bissexto += 1

        resultado = f"Entre 2000 e {ano_final}, há {ano_bissexto} anos bissextos."
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora de Anos Bissextos")
janela.geometry("300x150")

# Rótulo e campo de entrada
label = tk.Label(janela, text="Digite o ano final:")
label.pack(pady=10)

entry_ano_final = tk.Entry(janela)
entry_ano_final.pack()

# Botão para calcular
botao = tk.Button(janela, text="Calcular", command=calcular_bissextos)
botao.pack(pady=10)

# Iniciar a interface
janela.mainloop()