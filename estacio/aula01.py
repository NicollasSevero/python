#Abram seu editor de código
#pasta : reserva_chaves
#arquivo: main.py 

import sqlite3
import tkinter as tk
from datetime import datetime

#criação e conexão com o banco de dados
conn = sqlite3.connect('lab_keys.db')
cursor  = conn.cursor()

#Criar as tabelas se elas não existirem
#banco de dados sqlite3 => visualizar os dados
#DB Browser
cursor.execute('''
    CREATE TABLE IF NOT EXISTS lab_keys
    (name TEXT, registration TEXT, key TEXT, date_time TEXT)
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS returned_keys
    (name TEXT, key TEXT, return_time TEXT)
    ''')

def add_professor():
    name = name_entry.get()
    registration = registration_entry.get()
    key = key_entry.get()
    date_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    cursor.execute("INSERT INTO lab_keys VALUES(?, ?, ?, ?)", 
                   (name, registration, key, date_time))
    conn.commit()

    name_entry.delete(0, tk.END)
    registration_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)

    update_list()

def remover_professor(event):
    selecionado = listbox.curselection()

    if selecionado:
        nome = listbox.get(selecionado).split(" - ")[1]
        chave = listbox.get(selecionado).split(" - ")[2]
        hora_retorno = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        cursor.execute("INSERT INTO returned_keys VALUES (?, ?, ?)", (nome, chave, hora_retorno))
        cursor.execute("DELETE FROM lab_keys WHERE name = ? AND key = ?", (nome, chave))
        conn.commit()
        update_list()
        update_returned_list()

#função para atualizar a listagem de quem pegou a chave
def update_list():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT date_time, name, key FROM lab_keys")

    for row in cursor.fetchall():
        listbox.insert(tk.END, f"{row[0]} - {row[1]} - {row[2]}")

def update_returned_list():
    returned_listbox.delete(0, tk.END)
    cursor.execute("SELECT return_time, name, key FROM returned_keys")
    for row in cursor.fetchall():
        returned_listbox.insert(tk.END, f"{row[0]} - {row[1]} - {row[2]}")



#criação da interface gráfica
root = tk.Tk()
root.title("Gerenciamento de chaves")

largura_janela=600
altura_janela=600

#Label e entrada para o nome do professor
label_name = tk.Label(root, text="Nome", font="Arial 14 bold")
label_name.grid(row=0, column=0)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

#Label e entrada para a matricula do professor
label_registration = tk.Label(root, text="Matrícula", font="Arial 14 bold")
label_registration.grid(row=1, column=0)

registration_entry = tk.Entry(root)
registration_entry.grid(row=1, column=1)

#Label e entrada para a chave da sala ou laboratório
label_key = tk.Label(root, text="lab/sala", font="Arial 14 bold")
label_key.grid(row=2, column=0)

key_entry = tk.Entry(root)
key_entry.grid(row=2, column=1)

add_button = tk.Button(root, text="Registrar", font="Arial 14 bold", command=add_professor)
add_button.grid(row=3, column=1)

#listagem para as chaves que foram pegas
header_1 = tk.Label(root, text="Hora - Nome - chave (Pegou)")
header_1.grid(row=5, column=1)

listbox = tk.Listbox(root, width=30)
listbox.grid(row=6, column=1)
listbox.bind('<Double-1>', remover_professor)

#listagem para as chaves devolvidas
header_2 = tk.Label(root, text="Hora - Nome - chave (Devolvida)")
header_2.grid(row=5, column=4)

returned_listbox = tk.Listbox(root, width=30)
returned_listbox.grid(row=6, column=4)

update_list()
update_returned_list()

#obter a largura e altura da nossa tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)

#define a posição da janela
root.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y))
#Abram seu editor de código
#pasta : reserva_chaves
#arquivo: main.py 

import sqlite3
import tkinter as tk
from datetime import datetime

#criação e conexão com o banco de dados
conn = sqlite3.connect('lab_keys.db')
cursor  = conn.cursor()

#Criar as tabelas se elas não existirem
#banco de dados sqlite3 => visualizar os dados
#DB Browser
cursor.execute('''
    CREATE TABLE IF NOT EXISTS lab_keys
    (name TEXT, registration TEXT, key TEXT, date_time TEXT)
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS returned_keys
    (name TEXT, key TEXT, return_time TEXT)
    ''')

def add_professor():
    name = name_entry.get()
    registration = registration_entry.get()
    key = key_entry.get()
    date_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    cursor.execute("INSERT INTO lab_keys VALUES(?, ?, ?, ?)", 
                   (name, registration, key, date_time))
    conn.commit()

    name_entry.delete(0, tk.END)
    registration_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)

    update_list()

def remover_professor(event):
    selecionado = listbox.curselection()

    if selecionado:
        nome = listbox.get(selecionado).split(" - ")[1]
        chave = listbox.get(selecionado).split(" - ")[2]
        hora_retorno = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        cursor.execute("INSERT INTO returned_keys VALUES (?, ?, ?)", (nome, chave, hora_retorno))
        cursor.execute("DELETE FROM lab_keys WHERE name = ? AND key = ?", (nome, chave))
        conn.commit()
        update_list()
        update_returned_list()

#função para atualizar a listagem de quem pegou a chave
def update_list():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT date_time, name, key FROM lab_keys")

    for row in cursor.fetchall():
        listbox.insert(tk.END, f"{row[0]} - {row[1]} - {row[2]}")

def update_returned_list():
    returned_listbox.delete(0, tk.END)
    cursor.execute("SELECT return_time, name, key FROM returned_keys")
    for row in cursor.fetchall():
        returned_listbox.insert(tk.END, f"{row[0]} - {row[1]} - {row[2]}")



#criação da interface gráfica
root = tk.Tk()
root.title("Gerenciamento de chaves")

largura_janela=600
altura_janela=600

#Label e entrada para o nome do professor
label_name = tk.Label(root, text="Nome", font="Arial 14 bold")
label_name.grid(row=0, column=0)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

#Label e entrada para a matricula do professor
label_registration = tk.Label(root, text="Matrícula", font="Arial 14 bold")
label_registration.grid(row=1, column=0)

registration_entry = tk.Entry(root)
registration_entry.grid(row=1, column=1)

#Label e entrada para a chave da sala ou laboratório
label_key = tk.Label(root, text="lab/sala", font="Arial 14 bold")
label_key.grid(row=2, column=0)

key_entry = tk.Entry(root)
key_entry.grid(row=2, column=1)

add_button = tk.Button(root, text="Registrar", font="Arial 14 bold", command=add_professor)
add_button.grid(row=3, column=1)

#listagem para as chaves que foram pegas
header_1 = tk.Label(root, text="Hora - Nome - chave (Pegou)")
header_1.grid(row=5, column=1)

listbox = tk.Listbox(root, width=30)
listbox.grid(row=6, column=1)
listbox.bind('<Double-1>', remover_professor)

#listagem para as chaves devolvidas
header_2 = tk.Label(root, text="Hora - Nome - chave (Devolvida)")
header_2.grid(row=5, column=4)

returned_listbox = tk.Listbox(root, width=30)
returned_listbox.grid(row=6, column=4)

update_list()
update_returned_list()

#obter a largura e altura da nossa tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)

#define a posição da janela
root.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y))

#manter a tela em funcionamento/aberta
root.mainloop()