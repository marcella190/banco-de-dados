import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

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
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    telefone = entry_telefone.get().strip()

    if not nome or not email or not telefone:
        messagebox.showwarning(
            "Campos Obrigatórios",
            "Por favor, preencha todos os campos (Nome, E-mail e Telefone) antes de salvar.",
        )
        return

    try:
        conexao = sqlite3.connect("clientes.db")
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
            (nome, email, telefone),
        )

        conexao.commit()
        conexao.close()

        messagebox.showinfo(
            "Sucesso", f"Cliente '{nome}' cadastrado com sucesso!"
        )
        limpar_formulario()

    except sqlite3.Error as erro:
        messagebox.showerror(
            "Erro no Banco de Dados",
            f"Não foi possível salvar os dados.\nErro: {erro}",
        )


def visualizar_clientes():
    """Abre uma nova janela exibindo todos os clientes cadastrados em uma tabela."""
    # Consulta os dados no banco antes de montar a tela
    try:
        conexao = sqlite3.connect("clientes.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, email, telefone FROM clientes")
        registros = cursor.fetchall()
        conexao.close()
    except sqlite3.Error as erro:
        messagebox.showerror(
            "Erro no Banco de Dados",
            f"Não foi possível consultar os clientes.\nErro: {erro}",
        )
        return

    # Cria uma janela secundária vinculada à janela principal
    janela_lista = tk.Toplevel(janela)
    janela_lista.title("Clientes Cadastrados")
    janela_lista.geometry("620x350")
    janela_lista.configure(padx=15, pady=15)

    # Garante que a janela fique em foco
    janela_lista.grab_set()

    label_subtitulo = tk.Label(
        janela_lista,
        text="Lista de Clientes Cadastrados",
        font=("Arial", 13, "bold"),
    )
    label_subtitulo.pack(pady=(0, 10))

    # Frame para organizar a tabela e a barra de rolagem
    frame_tabela = tk.Frame(janela_lista)
    frame_tabela.pack(fill="both", expand=True)

    # Configuração da Tabela (Treeview)
    colunas = ("id", "nome", "email", "telefone")
    tabela = ttk.Treeview(
        frame_tabela, columns=colunas, show="headings", height=10
    )

    # Cabeçalhos das colunas
    tabela.heading("id", text="ID")
    tabela.heading("nome", text="Nome")
    tabela.heading("email", text="E-mail")
    tabela.heading("telefone", text="Telefone")

    # Largura e alinhamento das colunas
    tabela.column("id", width=45, anchor="center")
    tabela.column("nome", width=200, anchor="w")
    tabela.column("email", width=200, anchor="w")
    tabela.column("telefone", width=120, anchor="center")

    # Barra de rolagem vertical
    scrollbar = ttk.Scrollbar(
        frame_tabela, orient="vertical", command=tabela.yview
    )
    tabela.configure(yscrollcommand=scrollbar.set)

    tabela.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Insere cada linha retornada do SQLite na tabela
    for cliente in registros:
        tabela.insert("", tk.END, values=cliente)

    # Botão para fechar a janela secundária
    btn_fechar = tk.Button(
        janela_lista,
        text="Fechar",
        command=janela_lista.destroy,
        width=12,
        font=("Arial", 10),
    )
    btn_fechar.pack(pady=(12, 0))


# ==============================================================================
# 3. INTERFACE GRÁFICA PRINCIPAL (Tkinter)
# ==============================================================================

inicializar_banco()

janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("430x250")
janela.resizable(False, False)
janela.configure(padx=20, pady=20)

label_titulo = tk.Label(
    janela, text="Novo Cadastro de Cliente", font=("Arial", 14, "bold")
)
label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 15))

# Campo: Nome
label_nome = tk.Label(janela, text="Nome:", font=("Arial", 10))
label_nome.grid(row=1, column=0, sticky="w", pady=5)
entry_nome = tk.Entry(janela, width=40, font=("Arial", 10))
entry_nome.grid(row=1, column=1, pady=5)

# Campo: E-mail
label_email = tk.Label(janela, text="E-mail:", font=("Arial", 10))
label_email.grid(row=2, column=0, sticky="w", pady=5)
entry_email = tk.Entry(janela, width=40, font=("Arial", 10))
entry_email.grid(row=2, column=1, pady=5)

# Campo: Telefone
label_telefone = tk.Label(janela, text="Telefone:", font=("Arial", 10))
label_telefone.grid(row=3, column=0, sticky="w", pady=5)
entry_telefone = tk.Entry(janela, width=40, font=("Arial", 10))
entry_telefone.grid(row=3, column=1, pady=5)

# Frame para os 3 botões de ação
frame_botoes = tk.Frame(janela)
frame_botoes.grid(row=4, column=0, columnspan=2, pady=(20, 0))

btn_salvar = tk.Button(
    frame_botoes,
    text="Salvar",
    command=salvar_cliente,
    width=11,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
)
btn_salvar.pack(side="left", padx=5)

btn_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    command=limpar_formulario,
    width=11,
    bg="#f44336",
    fg="white",
    font=("Arial", 10, "bold"),
)
btn_limpar.pack(side="left", padx=5)

btn_visualizar = tk.Button(
    frame_botoes,
    text="Visualizar Clientes",
    command=visualizar_clientes,
    width=16,
    bg="#2196F3",
    fg="white",
    font=("Arial", 10, "bold"),
)
btn_visualizar.pack(side="left", padx=5)

entry_nome.focus()
janela.mainloop()

