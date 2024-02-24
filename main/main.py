import mysql.connector
import time

while True:
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Asking@123',
        database='bd_crud',
    )

    cursor = conexao.cursor()
    print('\033[34m CADASTRO DE USUARIO\033[m')
    print('*****MENU*****\n')
    select = int(input('[1] Cadastrar novo usuario\n[2] Ver usuarios cadastrados\n[3] Editar usuario ja existente\n[4] Apagar usuario\n[5] Sair\n\033[34mDigite o comando escolhido: \033[m'))

    if select == 1:
        # Creat
        nome = input('Digite seu nome: ').upper()
        idade = int(input('Digite sua idade: '))

        comando = 'INSERT INTO usuarios (nome_usuario, idade_usuario) VALUES (%s, %s)'
        valores = (nome, idade)

        cursor.execute(comando, valores)
        conexao.commit()
        time.sleep(1)
        print("\033[32m Dados inseridos com sucesso!\033[m")

    elif select == 2:
        # READ
        comando = 'SELECT * FROM usuarios'
        cursor.execute(comando)
        resulta = cursor.fetchall()
        for i in resulta:
            print('{} - Nome: {} || Idade: {}'.format(i[0], i[1], i[2]))

    elif select == 3:
        # UPDATE
        usuario = input('Digite o nome de usuário cadastrado: ').upper()
        novo_usuario = input('Digite o novo nome: ').upper()
        comando = 'SELECT * FROM usuarios WHERE nome_usuario = %s'
        dados = (usuario,)
        cursor.execute(comando, dados)
        resultado = cursor.fetchall()
        if resultado:
            comando = 'UPDATE usuarios SET nome_usuario = %s WHERE nome_usuario = %s'
            dados = (novo_usuario, usuario)
            cursor.execute(comando, dados)
            conexao.commit()
            time.sleep(1)
            print("\033[32mDados inseridos com sucesso!\033[m")
        else:
            print('\033[31mUsuário não encontrado\033[m')

    elif select == 4:
        # DELETE
        usuario = input('Digite o nome de usuário a ser apagado: ').upper()
        comando = 'SELECT * FROM usuarios WHERE nome_usuario = %s'
        dados = (usuario,)
        cursor.execute(comando, dados)
        resultado = cursor.fetchall()
        if resulta:
            comando = 'DELETE FROM usuarios WHERE nome_usuario = %s'
            dados = (usuario,)
            cursor.execute(comando, dados)
            conexao.commit()
            time.sleep(1)
            print("\033[32mUsuário apagado com sucesso!\033[m")
        else:
            print('\033[31mUsuário não encontrado\033[m')

    else:
        cursor.close()
        conexao.close()
        break
