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
            print ('\n-- ✅ Login Efetuado com Sucesso! ✅ --\n')
            print (f'Bem-vindo de volta {resultado_login [1]}.\n')
            break

        else:
            tentativas -= 1
            if tentativas > 0:
                print ('\n❌ Usuário ou senha incorretos! ❌\n')
                print (f'{tentativas} Tentativas restantes.\n')
            else:
                print('\nVocê excedeu o número de tentativas. Finalizando programa...\n')
                exit()

def cadastrar_funcionario (cursor):
    print ('\n--- CADASTRO DE FUNCIONÁRIO ---\n')
    print ('Para começar, preencha as informações do funcionário abaixo: \n')
    primeiro_nome = str(input('Primeiro nome: '))
    sobrenome = str(input('Sobrenome: '))
    nome_completo = (f'{primeiro_nome} {sobrenome}')

    cpf = str(input('CPF: ')).strip()
    dt_admissao = str(input('Data de Admissão (aaaa-mm-dd): '))
    salario = float(input('Salário: '))

    print ('\n- Endereço -')
    estado = str(input('Estado: '))
    cidade = str(input('Cidade: '))
    bairro = str(input('Bairro: '))
    rua = str(input('Rua: '))
    numero = str(input('Número: '))
    complemento = str(input('Complemento (opcional): ')).strip()

    if complemento == '':
        complemento =  None

    if complemento: 
        endereco = (f'{rua} {complemento} {numero}, {bairro} - {cidade}, {estado}')    
    else: 
        endereco = (f'{rua} {numero}, {bairro} - {cidade}, {estado}')    
        
    senha = str(input('\nCrie uma senha para login do funcionário: '))

    senha_confirmacao = os.getenv('SENHA_CONFIRMACAO')

    print (f'Para continuar com o cadastro do funcionário, confirme os dados abaixo:\n')
    print (f'Nome completo: {nome_completo}')
    print (f'CPF: {cpf}')
    print (f'Data de admissão: {dt_admissao}')
    print (f'Salário: {salario}')
    print (f'Endereço: {endereco}')

    tentativas_confirmacao = 3

    while tentativas_confirmacao > 0 :

        print (f'\n{tentativas_confirmacao} Tentativa(s) Restante(s).')

        confirmacao_dados = str(input('\nSeus dados estão corretos? (Para confirmar, digite a senha de administração): '))

        if confirmacao_dados == senha_confirmacao:
            cursor.execute (
                """ 
                INSERT INTO endereco 
                    (rua, numero, bairro, cidade, estado, complemento)
                VALUES 
                    (%s, %s, %s, %s, %s, %s)
                RETURNING id_endereco
                """,

                (rua, numero, bairro, cidade, estado, complemento)
            )

            id_endereco = cursor.fetchone()[0]
            
            cursor.execute (
                """
                INSERT INTO funcionario
                    (cpf, primeiro_nome, sobrenome, dt_admissao, salario, id_endereco, senha)
                VALUES 
                    (%s, %s, %s, %s, %s, %s, %s)
                RETURNING matricula_funcional
                """,
                (cpf, primeiro_nome, sobrenome, dt_admissao, salario, id_endereco, senha)
            )

            matricula_funcional = cursor.fetchone()[0]

            print('\n✅ Dados Verificados com Sucesso ✅')
        
            print('\nQual será a função do funcionário?\n')
            print ('[ 1 ] Professor')
            print ('[ 2 ] Coordenador')

            tipo_funcionario = int(input('\nDigite uma opção (1 ou 2): '))

            if tipo_funcionario == 1:

                tipo_funcionario = 'Professor'

                print('\n- Cadastro de Professor -\n')

                titulacao = str(input('Titulação: ')).strip().capitalize()
                area_atuacao = str(input('Área de atuação: ')).strip().capitalize()

                cursor.execute (
                    """
                    INSERT INTO professor 
                        (matricula_funcional, titulacao, area_atuacao)
                    VALUES
                        (%s, %s, %s)
                    """,

                    (matricula_funcional, titulacao, area_atuacao,)
                )

            elif tipo_funcionario == 2:

                tipo_funcionario = 'Coordenador'
                
                print ('\n- Cadastro de Coordenador -\n')

                print('Curso de Coordenação: ')

                print('[ 1 ] Engenharia de Software')
                print('[ 2 ] Ciência da Computação')
                print('[ 3 ] Sistemas de Informação')
                print('[ 4 ] Banco de Dados')
                print('[ 5 ] Análise e Desenvolvimento de Sistemas')

                curso_coordenacao = int(input('\nDigite o número do curso: '))

                cursos = {
                    1: 'Engenharia de Software',
                    2: 'Ciência da Computação',
                    3: 'Sistemas de Informação',
                    4: 'Banco de Dados',
                    5: 'Análise e Desenvolvimento de Sistemas'
                }

                while curso_coordenacao not in cursos: 
                    print('\nOpção de curso inválida.')
                    curso_coordenacao = int(input('\nDigite novamente o número do curso: '))

                tempo_coordenacao = 0

                cursor.execute (
                    """
                    INSERT INTO coordenador
                        (matricula_funcional, cod_curso, tempo_coordenacao_meses)
                    VALUES
                        (%s, %s, %s)
                    """,

                    (matricula_funcional, curso_coordenacao, tempo_coordenacao)
                )

            else:
                print('Opção Inválida.')

            connect_sisacad.commit()

            print (f'\n--- ✅ {nome_completo} agora é um {tipo_funcionario} registrado na Universidade ✅ ---\n')   
            print ('Segue abaixo as informações para login do funcionário na plataforma: ')
            print (f'Matrícula funcional: {matricula_funcional}')
            print (f'Senha do Funcionário: {senha}\n')

            break

        elif confirmacao_dados != senha_confirmacao:
            tentativas_confirmacao -= 1
            if tentativas_confirmacao > 0:
                erro_cadastro = str(input('\n❌ Senha de confirmação incorreta. ❌\nExiste algum erro no cadastro? (s/n): '))
                if erro_cadastro == 'n':
                    print ('\nTente novamente digitar sua senha.\n')
                elif erro_cadastro == 's':
                    print ('\n❌ Erro no cadastro. Reinicie o processo de cadastro. ❌\n')
                    exit ()
                else:
                    print ('\n Opção Inválida. Encerrando programa...\n')
                    exit ()
            else:
                print ('Você excedeu o número de tentativas. Encerrando Programa...')

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



