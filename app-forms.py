import sqlite3
import tkinter as tk
from tkinter import messagebox

# ==============================================================================
# 1. CONFIGURAÇÃO DO BANCO DE DADOS (SQLite)
# ==============================================================================


def inicializar_banco():
    """Cria o banco de dados e a tabela de clientes caso ainda não existam."""
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


# ==============================================================================
# 2. FUNCIONALIDADES DO SISTEMA
# ==============================================================================


def limpar_formulario():
    """Limpa todos os campos de entrada e retorna o foco para o campo Nome."""
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_nome.focus()


def salvar_cliente():
    """Valida os dados inseridos e os salva no banco de dados SQLite."""
    # O método .strip() remove espaços em branco extras no início e no fim
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    telefone = entry_telefone.get().strip()

    # Validação: Verifica se algum campo ficou vazio
    if not nome or not email or not telefone:
        messagebox.showwarning(
            "Campos Obrigatórios",
            "Por favor, preencha todos os campos (Nome, E-mail e Telefone) antes de salvar.",
        )
        return

    # Inserção no banco de dados
    try:
        conexao = sqlite3.connect("clientes.db")
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
            (nome, email, telefone),
        )

        conexao.commit()
        conexao.close()

        # Mensagem de sucesso e limpeza automática para o próximo cadastro
        messagebox.showinfo(
            "Sucesso", f"Cliente '{nome}' cadastrado com sucesso!"
        )
        limpar_formulario()

    except sqlite3.Error as erro:
        messagebox.showerror(
            "Erro no Banco de Dados",
            f"Não foi possível salvar os dados.\nErro: {erro}",
        )


# ==============================================================================
# 3. INTERFACE GRÁFICA (Tkinter)
# ==============================================================================

# Inicializa o banco antes de abrir a janela
inicializar_banco()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("380x240")
janela.resizable(False, False)
janela.configure(padx=20, pady=20)

# Título do formulário
label_titulo = tk.Label(
    janela, text="Novo Cadastro de Cliente", font=("Arial", 14, "bold")
)
label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 15))

# Campo: Nome
label_nome = tk.Label(janela, text="Nome:", font=("Arial", 10))
label_nome.grid(row=1, column=0, sticky="w", pady=5)
entry_nome = tk.Entry(janela, width=35, font=("Arial", 10))
entry_nome.grid(row=1, column=1, pady=5)

# Campo: E-mail
label_email = tk.Label(janela, text="E-mail:", font=("Arial", 10))
label_email.grid(row=2, column=0, sticky="w", pady=5)
entry_email = tk.Entry(janela, width=35, font=("Arial", 10))
entry_email.grid(row=2, column=1, pady=5)

# Campo: Telefone
label_telefone = tk.Label(janela, text="Telefone:", font=("Arial", 10))
label_telefone.grid(row=3, column=0, sticky="w", pady=5)
entry_telefone = tk.Entry(janela, width=35, font=("Arial", 10))
entry_telefone.grid(row=3, column=1, pady=5)

# Frame para agrupar os botões lado a lado
frame_botoes = tk.Frame(janela)
frame_botoes.grid(row=4, column=0, columnspan=2, pady=(20, 0))

# Botão Salvar
btn_salvar = tk.Button(
    frame_botoes,
    text="Salvar",
    command=salvar_cliente,
    width=12,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
)
btn_salvar.pack(side="left", padx=10)

# Botão Limpar
btn_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    command=limpar_formulario,
    width=12,
    bg="#f44336",
    fg="white",
    font=("Arial", 10, "bold"),
)
btn_limpar.pack(side="left", padx=10)

# Coloca o cursor piscando no primeiro campo ao abrir
entry_nome.focus()

# Inicia o loop da interface gráfica
janela.mainloop()
