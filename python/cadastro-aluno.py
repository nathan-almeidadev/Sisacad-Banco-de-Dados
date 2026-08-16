import os
import psycopg2
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

def conectar_banco():
    connect_sisacad = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    return connect_sisacad

def fazer_login (cursor):
    print ('\n--- LOGIN ---\n') 

    tentativas = 3

    while tentativas > 0:
        print (f'{tentativas} Tentativa(s) restante(s).\n')
        usuario_login = str(input("Usuário: "))
        senha_login = str(input("Senha: "))

        cursor.execute(
            """
            SELECT usuario, primeiro_nome FROM aluno WHERE usuario = %s AND senha = %s;
            """,

            (usuario_login, senha_login)
        )

        resultado_login = cursor.fetchone()

        if resultado_login:

            print ('\n--- LOGIN EFETUADO COM SUCESSO ✅ ---')
            print (f'Bem-vindo de volta, {resultado_login[1]}!\n')
            break
        else:
            tentativas = tentativas - 1
            if tentativas > 0:
                print ('\n--- Usuário ou senha incorretos ❌ ---')
                print(f'Tente novamente.\n')
            else: 
                print ('\nVocê excedeu o número de tentativas.\n')
                exit ()

connect_sisacad = conectar_banco()
cursor = connect_sisacad.cursor()

print ("\nSISTEMA DE MATRÍCULA - SISACAD")

opcao = int(input("\n[ 1 ] Já sou matriculado (Fazer login)\n[ 2 ] Quero me matricular (Fazer matrícula)\n\n"))

if opcao == 1:
    fazer_login(cursor)

elif opcao == 2:

    print ("\n--- EFETUAR MATRÍCULA ---\n")

    print ("Para começar o processo de matricula, preencha os campos abaixo com seus dados: \n")

    primeiro_nome = str(input('Primeiro nome: '))
    sobrenome = str(input('Sobrenome: '))
    
    nome_completo = (f'{primeiro_nome} {sobrenome}')

    cpf = str(input('CPF (Apenas os números): '))
    dt_nascimento = str (input('Data de nascimento (aaaa-mm-dd): '))

    print('\nEm qual curso você deseja se matricular?')

    print('[ 1 ] Engenharia de Software')
    print('[ 2 ] Ciência da Computação')
    print('[ 3 ] Sistemas de Informação')
    print('[ 4 ] Banco de Dados')
    print('[ 5 ] Análise e Desenvolvimento de Sistemas')

    curso = int(input('\nDigite o número do curso: '))

    cursos = {
        1: 'Engenharia de Software',
        2: 'Ciência da Computação',
        3: 'Sistemas de Informação',
        4: 'Banco de Dados',
        5: 'Análise e Desenvolvimento de Sistemas'
    }

    while curso not in cursos: 
        print('\nOpção de curso inválida.')
        curso = int(input('\nDigite novamente o número do curso: '))

    nome_curso = cursos[curso]

    print ('\n--- Endereço ---')

    estado = str(input('Estado (DF, SP...): '))
    cidade = str(input('Cidade: '))
    bairro = str(input('Bairro: '))
    rua = str(input('Rua: '))
    numero = int(input('Número: '))

    endereco = (f'{rua} {numero}, {bairro} - {cidade}, {estado}')

    senha = str(input('\nCrie uma senha: '))

    usuario = (f'{primeiro_nome.lower().strip().split()[0]}.{sobrenome.lower().strip().split()[0]}')

    print (f'Para continuar com sua matrícula, confirme seus dados abaixo:\n')
    print (f'Nome completo: {nome_completo}')
    print (f'CPF: {cpf}')
    print (f'Data de nascimento: {dt_nascimento}')
    print (f'Curso: {nome_curso}')
    print (f'Endereço: {endereco}')

    tentativas_confirmacao = 3

    while tentativas_confirmacao > 0 :

        print (f'\n{tentativas_confirmacao} Tentativa(s) Restante(s).')

        confirmacao_dados = str(input('\nSeus dados estão corretos? (Para confirmar, digite sua senha): '))

        if confirmacao_dados == senha:
            print (f'\n--- Parabéns {primeiro_nome}! Você está matriculado no curso {nome_curso} ---')   
            print (f'Seu usuário para efetuar login é: {usuario}\n')

            cursor.execute (
                """ 
                INSERT INTO endereco 
                    (id_endereco, rua, numero, bairro, cidade, estado)
                VALUES 
                    (%s, %s, %s, %s, %s, %s)
                """,

                (52, rua, numero, bairro, cidade, estado)
            )

            cursor.execute (
                """
                INSERT INTO aluno 
                    (matricula, cpf, primeiro_nome, sobrenome, dt_nascimento, cod_curso, id_endereco, usuario, senha)
                VALUES 
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,

                (2026102, cpf, primeiro_nome, sobrenome, dt_nascimento, curso, 52, usuario, senha)
            )

            connect_sisacad.commit()

            break

        else:
            tentativas_confirmacao -= 1
            if tentativas_confirmacao > 0:
                erro_cadastro = str(input('\nSenha de confirmação incorreta. Você encontrou algum erro em seu cadastro? (s/n)'))
                if erro_cadastro == 'n':
                    print ('\nTente novamente digitar sua senha.\n')
                elif erro_cadastro == 's':
                    print ('\nErro no cadastro. Reinicie o processo de matrícula.\n')
                    exit ()
                else:
                    print ('\n Opção Inválida. Encerrando programa...\n')
                    exit ()
            else:
                print ('Você excedeu o número de tentativas. Encerrando Programa...')
            

else:
   print('\nOpção Inválida.\n')