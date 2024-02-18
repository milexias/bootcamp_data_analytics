import sqlite3

conexao = sqlite3.connect('dados')
cursor = conexao.cursor()

## 1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).
cursor.execute('DROP TABLE IF EXISTS alunos')
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

## 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
 
 # Utilizando INSERT OR IGNORE para evitar inserção de registros duplicados
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES(1, "Alexia", 25, "BI e Analytics")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES(2, "Ricaon", 30, "Engenharia de Software")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES(3, "Carol", 18, "Data Science")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES(4, "Pamela", 26, "Data Science")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES(5, "Patricia", 33, "Engenharia de Software")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES(6, "Rodrigo", 19, "BI e Analytics")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES(7, "Francisco", 36, "Engenharia de Software")')

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

conexao.commit()
conexao.close()

## 5. Criar uma Tabela e Inserir Dados

### a) Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.

cursor.execute('DROP TABLE IF EXISTS clientes')
cursor.execute('CREATE TABLE clientes (id INT PRIMARY KEY, nome TEXT, idade INT, saldo FLOAT)')

cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(1, "Pedro", 25, 1000.50)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(2, "Nathalia", 30, 500.75)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(3, "Alana", 22, 1200.50)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(4, "Heitor", 35, 1800.00)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(5, "Vitor", 31, 2500.25)')

## 6. Consultas e Funções Agregadas:

### a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
dados = cursor.execute('SELECT nome,idade FROM clientes WHERE idade > 30')
for cliente in dados: 
    print(f'O cliente {cliente} possui idade superior a 30 anos.')

### b) Calcule o saldo médio dos clientes.
dados = cursor.execute('SELECT AVG(saldo) FROM clientes')
for valor in dados: 
    print(f'O saldo médio dos clientes é de {valor}.')
    
### c) Encontre o cliente com o saldo máximo.
dados = cursor.execute('SELECT MAX(saldo), nome FROM clientes')
for valor, nome in dados: 
    print(f'O saldo maximo dos clientes é de {valor} para o cliente {nome}.')

### d) Conte quantos clientes têm saldo acima de 1000.
dados = cursor.execute('SELECT COUNT(id) FROM clientes WHERE saldo > 1000')
for contagem in dados: 
    print(f'O total de {contagem} clientes possuem saldo acima de 1000.')

## 7. Atualização e Remoção com Condições
### a) Atualize o saldo de um cliente específico.
dados = cursor.execute('UPDATE clientes SET saldo=1250.75 WHERE nome="Pedro"')
for cliente in dados: 
    print(cliente)

### b) Remova um cliente pelo seu ID.
dados = cursor.execute('DELETE FROM clientes WHERE id=2')
for cliente in dados: 
    print(cliente)

## 8. Junção de Tabelas
### a) Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real).

cursor.execute('DROP TABLE IF EXISTS compras')
cursor.execute('CREATE TABLE compras (id INT PRIMARY KEY, cliente_id INT REFERENCES clientes(id), produto TEXT, valor REAL)')

### b) Insira algumas compras associadas a clientes existentes na tabela "clientes".
    
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (1, 5, "Mouse Ergonomico", 410.50)') 
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (2, 3, "Teclado Ergonomico", 600.75)')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (3, 4, "Fone de Ouvido", 250.00)')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (4, 1, "Mouse Ergonomico", 410.50)')

### c) Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes INNER JOIN compras ON clientes.id = compras.cliente_id')
for cliente in dados: 
    print(cliente)
        
conexao.commit()
conexao.close()
