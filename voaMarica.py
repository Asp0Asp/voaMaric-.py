from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Toplevel
import sqlite3

janela = Tk()
janela.geometry("310x400")
janela.title("VoaMaricá")
janela.resizable(width=FALSE, height=FALSE)

def criarTab_usu():
    conecao = sqlite3.connect("cadUsu.db")
    cursor = conecao.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios "
                   "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
                   "nome TEXT, "
                   "senha TEXT)")
    conecao.commit()
    conecao.close()

def cadUsuario():
    nome = entryNome.get()
    senha = entrySenha.get()

    conecao = sqlite3.connect("cadastrar.db")
    cursor = conecao.cursor()
    cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, senha))
    conecao.commit()
    conecao.close()

    messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")

def Login():
    nome = entryNome.get()
    senha = entrySenha.get()

    conecao = sqlite3.connect("cadastrar.db")
    cursor = conecao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nome=? AND senha=?", (nome, senha))
    usuario = cursor.fetchone()
    conecao.close()

    if usuario is not None:
        messagebox.showinfo("Login", "Login efetuado com sucesso!")
    else:
        messagebox.showerror("Login", "Nome de usuário ou senha incorretos!")

#para Cad numa tabela novos voos
def cadTabVoos():
    conecao = sqlite3.connect("cadVoos.db")
    cursor = conecao.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS voos "
                   "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
                   "origem TEXT, destino TEXT, "
                   "data TEXT, "
                   "hora TEXT)")
    conecao.commit()
    conecao.close()

#para configura o dirFrame
def cadVoo():
    origem = entryOrigem.get()
    destino = entryDestino.get()
    data = entryData.get()
    hora = entryHora.get()

    conecao = sqlite3.connect("cadVoos.db")
    cursor = conecao.cursor()
    cursor.execute("INSERT INTO voos (origem, destino, data, hora) VALUES (?, ?, ?, ?)",
                   (origem, destino, data, hora))
    conecao.commit()
    conecao.close()

    messagebox.showinfo("Cadastro de Voos", "Voo cadastrado com sucesso!")


# Função para excluir um voo
def excluir_voo():
    numero = entryNumero.get()

    conecao = sqlite3.connect("cadastro_voos.db")
    cursor = conecao.cursor()
    cursor.execute("DELETE FROM voos WHERE numero=?", (numero,))
    conecao.commit()
    conecao.close()

    messagebox.showinfo("Exclusão de Voo", "Voo excluído com sucesso!")

# Função para alterar um voo
def alterar_voo():
    numero_antigo = entryNumero.get()
    numero_novo = entryNumero.get()

    conecao = sqlite3.connect("cadastro_voos.db")
    cursor = conecao.cursor()
    cursor.execute("UPDATE voos SET numero=? WHERE numero=?", (numero_novo, numero_antigo))
    conecao.commit()
    conecao.close()

    messagebox.showinfo("Alteração de Voo", "Voo alterado com sucesso!")

# Função para visualizar os voos cadastrados
def visualizar_voos():
    conecao = sqlite3.connect("cadastro_voos.db")
    cursor = conecao.cursor()
    cursor.execute("SELECT numero FROM voos")
    voos = cursor.fetchall()
    conecao.close()

    messagebox.showinfo("Voos Cadastrados", "Voos: " + ", ".join([voo[0] for voo in voos]))


#criaçao frame esquerda e o que será colocado nessa parte do frame
esqFrame = Frame(janela, width=140, height=400, bg='PowderBlue', relief='raise')
esqFrame.pack(side=LEFT)



labelNome = Label(esqFrame, text="Nome de Usuário*:", bg='PowderBlue')
labelNome.place(x=5, y=50)
entryNome = Entry(esqFrame)
entryNome.place(x=5, y=70)

labelSenha = Label(esqFrame, text="Senha*:", bg='PowderBlue')
labelSenha.place(x=5, y=95)
entrySenha = Entry(esqFrame, show="*" )
entrySenha.place(x=5, y=115)

botaoCadastrar = Button(janela, text="Cadastrar", command=cadUsuario)
botaoCadastrar.place(x=5, y=140)

botaoLogin = Button(janela, text="Login", command=Login)
botaoLogin.place(x=5, y=168)


#criação do frame direito e mas conf que ficaram desse lado do frame
dirFrame = Frame(janela, width=150, height=400, bg='PowderBlue', relief='raise')
dirFrame.pack(side=RIGHT)

labelOrigem = Label(dirFrame, text="Origem:", bg='PowderBlue')
labelOrigem.place(x=18, y=50)
entryOrigem = Entry(dirFrame)
entryOrigem.place(x=18, y=70)

labelDestino = Label(dirFrame, text="Destino:", bg='PowderBlue')
labelDestino.place(x=18, y=95)
entryDestino = Entry(dirFrame)
entryDestino.place(x=18, y=115)

labelData = Label(dirFrame, text="Data:", bg='PowderBlue')
labelData.place(x=18, y=135)
entryData = Entry(dirFrame)
entryData.place(x=18, y=155)

labelHora = Label(dirFrame, text="Hora:", bg='PowderBlue')
labelHora.place(x=18, y=175)
entryHora = Entry(dirFrame)
entryHora.place(x=18, y=195)

labelNumero = Label(dirFrame, text="Número do Voo:", bg='PowderBlue')
labelNumero.place(x=18, y=218)
entryNumero = Entry(dirFrame)
entryNumero.place(x=18, y=246)

botaoCadastrar = Button(dirFrame, text="Cadastrar Voo", command=cadVoo)
botaoCadastrar.place(x=18, y=274)

botao_excluir = Button(dirFrame, text="Excluir Voo", command=excluir_voo)
botao_excluir.place(x=18, y=302)

botao_alterar = Button(dirFrame, text="Alterar Voo", command=alterar_voo)
botao_alterar.place(x=18, y=330)

botao_visualizar = Button(dirFrame, text="Visualizar Voos", command=visualizar_voos)
botao_visualizar.place(x=18, y=358)

janela.mainloop()