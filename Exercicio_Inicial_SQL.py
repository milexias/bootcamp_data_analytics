import sqlite3

Exercicio_Inicial_SQL = sqlite3.connect('dados')
cursor = Exercicio_Inicial_SQL.cursor()

## 1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

## 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
cursor.execute('INSERT INTO alunos (id,nome,idade,curso) VALUES(1, "Alexia", 25, "BI & Analytics")')
cursor.execute('INSERT INTO alunos (id,nome,idade,curso) VALUES(2, "Ricaon", 30, "Engenharia de Software")')
cursor.execute('INSERT INTO alunos (id,nome,idade,curso) VALUES(3, "Carol", 18, "Data Science")')
cursor.execute('INSERT INTO alunos (id,nome,idade,curso) VALUES(4, "Pamela", 26, "Data Science")')
cursor.execute('INSERT INTO alunos (id,nome,idade,curso) VALUES(5, "Patricia", 33, "Engenharia de Software")')
cursor.execute('INSERT INTO alunos (id,nome,idade,curso) VALUES(6, "Rodrigo", 19, "BI & Analytics")')
cursor.execute('INSERT INTO alunos (id,nome,idade,curso) VALUES(7, "Francisco", 36, "Engenharia de Software")')

## 3. Consultas Básicas - Escreva consultas SQL para realizar as seguintes tarefas:
### a) Selecionar todos os registros da tabela "alunos".
dado = cursor.execute('SELECT * FROM alunos')
for aluno in dado: 
    print(aluno)

### b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
dado = cursor.execute('SELECT nome,idade FROM alunos WHERE idade > 20')
for aluno in dado: 
    print(aluno)

### c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
dado = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia de Software" ORDER BY nome ASC')
for aluno in dado: 
    print(aluno)

## d) Contar o número total de alunos na tabela
dado = cursor.execute('SELECT COUNT(id) FROM alunos ')
for aluno in dado: 
    print(aluno)

## 4. Atualização e Remoção
### a) Atualize a idade de um aluno específico na tabela.
dado = cursor.execute('UPDATE alunos SET idade=33 WHERE nome="Ricaon"')
for aluno in dado: 
    print(aluno)

### b) Remova um aluno pelo seu ID.
dado = cursor.execute('DELETE FROM alunos WHERE id=6')
for aluno in dado: 
    print(aluno)

Exercicio_Inicial_SQL.commit()
Exercicio_Inicial_SQL.close 