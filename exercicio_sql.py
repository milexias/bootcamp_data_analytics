import sqlite3

def conectar_banco_dados():
    return sqlite3.connect('dados')
conexao = conectar_banco_dados()

# 1. Criar a tabela
def criar_tabela_estudantes(conexao):
    cursor = conexao.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS estudantes(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')
    conexao.commit()
criar_tabela_estudantes(conexao)

# 1. Inserir registros
def inserir_estudantes(conexao):
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO estudantes (id,nome,idade,curso) VALUES(1, "Alexia", 25, "BI & Analytics")')
    cursor.execute('INSERT INTO estudantes (id,nome,idade,curso) VALUES(2, "Ricaon", 30, "Engenharia de Software")')
    cursor.execute('INSERT INTO estudantes (id,nome,idade,curso) VALUES(3, "Carol", 18, "Data Science")')
    cursor.execute('INSERT INTO estudantes (id,nome,idade,curso) VALUES(4, "Pamela", 26, "Data Science")')
    cursor.execute('INSERT INTO estudantes (id,nome,idade,curso) VALUES(5, "Patricia", 33, "Engenharia de Software")')
    cursor.execute('INSERT INTO estudantes (id,nome,idade,curso) VALUES(6, "Rodrigo", 19, "BI & Analytics")')
    cursor.execute('INSERT INTO estudantes (id,nome,idade,curso) VALUES(7, "Francisco", 36, "Engenharia de Software")')
    conexao.commit()
inserir_estudantes(conexao)

# 3. Consultas Básicas
def selecionar_todos_estudantes(conexao):
    cursor = conexao.cursor()
    resultado = cursor.execute('SELECT * FROM estudantes').fetchall()
    return resultado
print("Todos os alunos:")
print(selecionar_todos_estudantes(conexao))

def selecionar_estudantes_mais_20_anos(conexao):
    cursor = conexao.cursor()
    resultado = cursor.execute('SELECT nome,idade FROM estudantes WHERE idade > 20').fetchall()
    return resultado
print("\nAlunos com mais de 20 anos:")
print(selecionar_estudantes_mais_20_anos(conexao))

def selecionar_estudantes_engenharia_ordem_alfabetica(conexao):
    cursor = conexao.cursor()
    resultado = cursor.execute('SELECT * FROM estudantes WHERE curso="Engenharia de Software" ORDER BY nome ASC').fetchall()
    return resultado
print("\nAlunos de Engenharia em ordem alfabética:")
print(selecionar_estudantes_engenharia_ordem_alfabetica(conexao))

def contar_total_estudantes(conexao):
    cursor = conexao.cursor()
    resultado = cursor.execute('SELECT COUNT(id) FROM estudantes').fetchall()
    return resultado
print("\nNúmero total de alunos:")
print(contar_total_estudantes(conexao))

   # 4. Atualização e Remoção
    # Atualizar a idade de um aluno específico
def atualizar_idade_estudantes(conexao, nome_estudantes, nova_idade):
    cursor = conexao.cursor()
    cursor.execute(f'UPDATE estudantes SET idade={nova_idade} WHERE nome="{nome_estudantes}"')
    conexao.commit()
  
atualizar_idade_estudantes(conexao, "Ricaon", 33)
print("\nAlunos após a atualização de idade de Ricaon:")
print(selecionar_todos_estudantes(conexao))

    # Remover um aluno pelo seu ID
def remover_estudantes_por_id(conexao, id_estudantes):
    cursor = conexao.cursor()
    cursor.execute(f'DELETE FROM estudantes WHERE id={id_estudantes}')
    conexao.commit()
remover_estudantes_por_id(conexao, 6)
print("\nAlunos após a remoção de Rodrigo:")
print(selecionar_todos_estudantes(conexao))

conexao = conectar_banco_dados()
conexao.close()

