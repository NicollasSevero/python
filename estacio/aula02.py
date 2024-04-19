import tkinter as tk
from tkinter import messagebox
import sqlite3

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('escola.db')
c = conn.cursor()

# Criar tabela Aluno
c.execute('''CREATE TABLE IF NOT EXISTS aluno (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                curso TEXT,
                ano_semestre TEXT)''')

# Criar tabela Professor
c.execute('''CREATE TABLE IF NOT EXISTS professor (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                disciplinas TEXT)''')

# Criar tabela Disciplina
c.execute('''CREATE TABLE IF NOT EXISTS disciplina (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                professor TEXT,
                horario TEXT,
                sala TEXT)''')

class SistemaEscola:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Escolar")
        
        self.frame = tk.Frame(root)
        self.frame.pack()

        # Botões para abrir janelas de cadastro
        self.btn_aluno = tk.Button(self.frame, text="Cadastrar Aluno", command=self.cadastrar_aluno)
        self.btn_aluno.pack()

        self.btn_professor = tk.Button(self.frame, text="Cadastrar Professor", command=self.cadastrar_professor)
        self.btn_professor.pack()

        self.btn_disciplina = tk.Button(self.frame, text="Cadastrar Disciplina", command=self.cadastrar_disciplina)
        self.btn_disciplina.pack()

    def cadastrar_aluno(self):
        # Função para cadastrar aluno
        def salvar_aluno():
            nome = entry_nome.get()
            curso = entry_curso.get()
            ano_semestre = entry_ano_semestre.get()
            c.execute("INSERT INTO aluno (nome, curso, ano_semestre) VALUES (?, ?, ?)", (nome, curso, ano_semestre))
            conn.commit()
            messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
            top.destroy()

        top = tk.Toplevel(self.root)
        top.title("Cadastrar Aluno")

        label_nome = tk.Label(top, text="Nome:")
        label_nome.grid(row=0, column=0)
        entry_nome = tk.Entry(top)
        entry_nome.grid(row=0, column=1)

        label_curso = tk.Label(top, text="Curso:")
        label_curso.grid(row=1, column=0)
        entry_curso = tk.Entry(top)
        entry_curso.grid(row=1, column=1)

        label_ano_semestre = tk.Label(top, text="Ano/Semestre:")
        label_ano_semestre.grid(row=2, column=0)
        entry_ano_semestre = tk.Entry(top)
        entry_ano_semestre.grid(row=2, column=1)

        btn_salvar = tk.Button(top, text="Salvar", command=salvar_aluno)
        btn_salvar.grid(row=3, columnspan=2)

    def cadastrar_professor(self):
        # Função para cadastrar professor
        def salvar_professor():
            nome = entry_nome.get()
            disciplinas = entry_disciplinas.get()
            c.execute("INSERT INTO professor (nome, disciplinas) VALUES (?, ?)", (nome, disciplinas))
            conn.commit()
            messagebox.showinfo("Sucesso", "Professor cadastrado com sucesso!")
            top.destroy()

        top = tk.Toplevel(self.root)
        top.title("Cadastrar Professor")

        label_nome = tk.Label(top, text="Nome:")
        label_nome.grid(row=0, column=0)
        entry_nome = tk.Entry(top)
        entry_nome.grid(row=0, column=1)

        label_disciplinas = tk.Label(top, text="Disciplinas Ministradas:")
        label_disciplinas.grid(row=1, column=0)
        entry_disciplinas = tk.Entry(top)
        entry_disciplinas.grid(row=1, column=1)

        btn_salvar = tk.Button(top, text="Salvar", command=salvar_professor)
        btn_salvar.grid(row=2, columnspan=2)

    def cadastrar_disciplina(self):
        # Função para cadastrar disciplina
        def salvar_disciplina():
            nome = entry_nome.get()
            professor = entry_professor.get()
            horario = entry_horario.get()
            sala = entry_sala.get()
            c.execute("INSERT INTO disciplina (nome, professor, horario, sala) VALUES (?, ?, ?, ?)", (nome, professor, horario, sala))
            conn.commit()
            messagebox.showinfo("Sucesso", "Disciplina cadastrada com sucesso!")
            top.destroy()

        top = tk.Toplevel(self.root)
        top.title("Cadastrar Disciplina")

        label_nome = tk.Label(top, text="Nome:")
        label_nome.grid(row=0, column=0)
        entry_nome = tk.Entry(top)
        entry_nome.grid(row=0, column=1)

        label_professor = tk.Label(top, text="Professor Responsável:")
        label_professor.grid(row=1, column=0)
        entry_professor = tk.Entry(top)
        entry_professor.grid(row=1, column=1)

        label_horario = tk.Label(top, text="Horário:")
        label_horario.grid(row=2, column=0)
        entry_horario = tk.Entry(top)
        entry_horario.grid(row=2, column=1)

        label_sala = tk.Label(top, text="Sala de Aula:")
        label_sala.grid(row=3, column=0)
        entry_sala = tk.Entry(top)
        entry_sala.grid(row=3, column=1)

        btn_salvar = tk.Button(top, text="Salvar", command=salvar_disciplina)
        btn_salvar.grid(row=4, columnspan=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaEscola(root)
<<<<<<< HEAD
    root.mainloop()
=======
    root.mainloop()
>>>>>>> b2252b4b974d2b36f7e69c4ece2d4d416e668229
