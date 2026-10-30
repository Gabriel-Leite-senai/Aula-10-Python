import sqlite3

def conectar():
    conexao = sqlite3.connect('contatos.db')
    c = conexao.cursor()
    
    sql='''
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT NOT NULL
    )'''

    c.execute(sql)
    conexao.commit()

    return conexao

def input_int(mensagen):
    while True:
        num = input(mensagen)
        try:
            return int(num)
        except ValueError:
            print("numero invalido")

def listar_contatos():
    conexao = conectar()
    cursor = conexao.cursor()
    tabela = cursor.execute("SELECT * FROM contatos")
    for row in tabela:
        print(f"ID: {row[0]} | Nome: {row[1]} | Telefone: {row[2]} | Email: {row[3]}")

def cadastrar_contato():
    nome = input("insira o nome do contato: ")
    telefone = input("insira o numero do contato: ")
    mail = input("insira o email do contato: ")
    conexao = conectar()
    cursor = conexao.cursor()

    sql = '''
    INSERT INTO contatos (nome, telefone, email)
    VALUES (?, ?, ?)'''
    cursor.execute(sql, (nome, telefone, mail))
    conexao.commit()
    cursor.close()

def alterar_contato():
    id_contato = input_int("insira o id do contado que você deseja alterar: ")
    conexao = conectar()
    cursor = conexao.cursor()

    while True:
        print("1 - nome")
        print("2 - telefone")
        print("3 - email")
        opt = input("Qual o campo que você deseja alterar: ")
        if opt == "1":
            campo = "nome"
            break
        elif opt == "2":
            campo = "telefone"
            break
        elif opt == "3":
            campo = "email"
            break
        else:
            print("opção invalida")
    novo_valor = input("insira o novo valor: ")

    sql = """
    UPDATE contatos SET telefone = ? WHERE id LIKE ?
    """
    cursor.execute(sql, (campo, novo_valor, id_contato))



def remover_contato():
    print("4")

def menu():
    while True:
        print("Contatos")
        print("1 - listar contatos")
        print("2 - cadastrar contato")
        print("3 - alterar contato")
        print("4 - remover contato")
        print("0 - sair")

        opt = input("Insira a opção: ")

        if opt == "1":
            listar_contatos()
        elif opt == "2":
            cadastrar_contato()
        elif opt == "3":
            alterar_contato()
        elif opt == "4":
            remover_contato()
        elif opt == "0":
            print("Saindo...")
            exit()

menu()