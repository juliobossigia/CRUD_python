import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='**********',
    database='bd_crud',
)

cursor = conexao.cursor()

#Creat
nome = input('Digite seu nome: ')  # Não é necessário converter para string, input já retorna string
idade = int(input('Digite sua idade: '))

comando = 'INSERT INTO usuarios (nome_usuario, idade_usuario) VALUES (%s, %s)'  # Usando parâmetros
valores = (nome, idade)  # Tupla com os valores a serem inseridos

cursor.execute(comando, valores)  # Executa o comando com os valores
conexao.commit()

print("Dados inseridos com sucesso!")


#READ
comando='SELECT * FROM usuarios'
resulta=cursor.fetchall()#vai ler o bd
print(resulta)

#UPDATE
comando='UPDATE usuarios SET nome_usuario = {} WHERE idade_usuario = {}'
cursor.execute(comando)
conexao.commit()

#DELETE
comando='DELETE FROM usuarios WHERE nome_usuario = {}'
cursor.execute(comando)
conexao.commit()

cursor.close()  # Fecha o cursor
conexao.close()  # Fecha a conexão


