import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def conectar_banco():
    connect_sisacad = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    return connect_sisacad

def fazer_login(cursor):
    print ('\n--- LOGIN ---\n')

    tentativas = 3

    while tentativas > 0:
        matricula_funcional = int(input('Matrícula Funcional: '))
        senha = str(input('Senha: '))

        cursor.execute (
            """
            SELECT matricula_funcional, primeiro_nome FROM funcionario WHERE matricula_funcional = %s AND senha = %s;
            """,

            (matricula_funcional, senha)
        )

        resultado_login = cursor.fetchone()

        if resultado_login:
            print ('-- Login Efetuado com Sucesso! --\n')
            print (f'Bem-vindo de volta {resultado_login [1]}.\n')
            break

        else:
            tentativas -= 1
            if tentativas > 0:
                print ('\nUsuário ou senha incorretos. Tente novamente!\n')
                print (f'{tentativas} Tentativas restantes.\n')
            else:
                print('\nVocê excedeu o número de tentativas. Finalizando programa...\n')
                exit()

def cadastrar_funcionario (cursor):
    print ('--- CADASTRO DE FUNCIONÁRIO ---\n')
    print ('Para começar, digite as informações do funcionário abaixo: \n')

connect_sisacad = conectar_banco()
cursor = connect_sisacad.cursor()

print('\n--- Sistema de Cadastro de Funcionários ---\n')

print('Bem-Vindo! Para começar, o que você quer fazer? \n')

opcao = int(input(
    '[ 1 ] Fazer Login\n'
    '[ 2 ] Cadastrar um funcionário\n\n'
    'Digite sua resposta aqui (1 ou 2): '
))

if opcao == 1:
    fazer_login(cursor)

elif opcao == 2:
    cadastrar_funcionario(cursor)

else:
    print('\nOpção Inválida.\n')
    exit()



