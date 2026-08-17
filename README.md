# 🎓 Sistema Acadêmico Universitário (SISACAD) — Universidade PortfólioHUB

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![Database](https://img.shields.io/badge/Database-PostgreSQL-blue)
![Backend](https://img.shields.io/badge/Backend-Python-green)
![BI](https://img.shields.io/badge/Future-PowerBI-orange)

Este repositório contém o desenvolvimento completo do SISACAD (Sistema Acadêmico Universitário), projetado como meu primeiro projeto de portfólio durante o primeiro semestre de Engenharia de Software.

O projeto contempla as etapas de modelagem de banco de dados e implementação física em PostgreSQL, além do desenvolvimento inicial de uma aplicação em Python integrada ao banco de dados. A aplicação permite realizar operações como autenticação e cadastro de alunos e funcionários, utilizando Python e psycopg2 para comunicação com o PostgreSQL.

O principal objetivo é aplicar, de forma prática, conceitos fundamentais de bancos de dados relacionais (OLTP), garantindo integridade, consistência, redução de redundâncias e aderência às boas práticas de modelagem.

**Observação:** Este projeto foi desenvolvido com apoio das ferramentas de Inteligência Artificial OpenAI ChatGPT, ClaudeAI e Google Gemini como recursos complementares de estudo, revisão e documentação.

---

## 📖 Sobre o Projeto

A Universidade PortfólioHUB enfrentava dificuldades no gerenciamento das informações acadêmicas de seus alunos, professores, coordenadores, cursos, disciplinas e turmas.

Diversos processos eram realizados de forma descentralizada, dificultando:

O controle de matrículas;
O gerenciamento da oferta de disciplinas;
A organização das turmas;
O acompanhamento do desempenho dos alunos;
A geração de relatórios acadêmicos.

Para solucionar esse problema, foi projetado um banco de dados centralizado capaz de gerenciar toda a estrutura acadêmica da instituição.

- Alunos
- Funcionários
- Professores
- Coordenadores
- Cursos
- Disciplinas
- Turmas
- Matrículas
- Notas
- Frequências

Além disso, o projeto foi estruturado para permitir futuras integrações com sistemas de análise de dados e aplicações web.

---

## 🎯 Objetivos do Sistema

- Gerenciar alunos e funcionários da universidade
- Controlar cursos e suas grades curriculares
- Registrar professores e coordenadores
- Organizar turmas ofertadas por semestre
- Controlar matrículas dos alunos
- Armazenar notas e frequências
- Garantir integridade referencial
- Possibilitar consultas e relatórios acadêmicos
- Servir de base para futuras integrações com APIs e dashboards

---

## 🏛️ Regras de Negócio

### Alunos

- Um aluno pertence a apenas um curso.
- Um curso pode possuir vários alunos (1:N).
- Um aluno pode realizar diversas matrículas ao longo de sua trajetória acadêmica.

---

### Cursos e Disciplinas

- Um curso pode possuir várias disciplinas.
- Uma disciplina pode pertencer a vários cursos (N:M).

---

### Turmas

- Uma disciplina pode gerar várias turmas em semestres diferentes.
- Uma turma pertence a apenas uma disciplina de origem (1:N).

---

### Professores

- Um professor pode lecionar várias disciplinas.
- Uma disciplina pode ser lecionada por vários professores (N:M).
- Um professor pode ministrar várias turmas.

---

### Coordenadores

- Um coordenador é responsável por um único curso.
- Cada curso possui um coordenador responsável (1:1).

---

### Matrículas

- Uma matrícula está vinculada a um aluno e a uma turma.
- Cada matrícula armazena:
 - Data da matrícula;
 - Nota final;
 - Frequência.

---

## 🧩 Conceitos de Modelagem Aplicados

### Especialização / Generalização

```
    Funcionário
      |
  ┌───┴────────┐
Professor  Coordenador

```

#### Características

- Especialização Parcial
- Especialização Sobreposta

Isso significa que:

- Um funcionário não deve obrigatoriamente pertencer a pelo menos uma especialização.
- Um funcionário pode exercer simultaneamente os papéis de Professor e Coordenador.

---

### Entidade Associativa

#### Matrícula

Responsável por representar o relacionamento entre:

```
Aluno ↔ Turma

```

Além disso, armazena atributos próprios:

- Nota;
- Frequência;
- Data da matrícula.

---

### Atributos Compostos

#### Nome

```
Nome
├── Primeiro Nome
└── Sobrenome
```

#### Endereco

```
Endereco
├── Rua
├── Número
├── Bairro
├── Cidade
└── Estado
```

---

### Atributos Multivalorados

Os endereços de e-mail foram modelados em entidades independentes:

- email_aluno
- email_funcionario

permitindo que um usuário possua múltiplos e-mails sem violar a Primeira Forma Normal (1FN).

---

## 🗂️ Estrutura Lógica do Banco de Dados

### ALUNO

- matricula (PK)
- cpf
- primeiro_nome
- sobrenome
- dt_nascimento
- cod_curso (FK)
- id_endereco (FK)

### FUNCIONARIO

- matricula_funcional (PK)
- cpf
- primeiro_nome
- sobrenome
- dt_admissao
- salario
- id_endereco (FK)

### PROFESSOR

- matricula_funcional (PK/FK)
- titulacao
- area_atuacao

### COORDENADOR

- matricula_funcional (PK/FK)
- cod_curso (FK/UNIQUE)
- tempo_coordenacao_meses

### CURSO

- cod_curso (PK)
- nome_curso
- carga_horaria

### DISCIPLINA

- cod_disciplina (PK)
- nome
- creditos

### TURMA

- cod_turma (PK)
- semestre
- turno
- capacidade
- cod_disciplina (FK)
- matricula_funcional (FK)

### MATRICULA

- id_matricula (PK)
- matricula (FK)
- cod_turma (FK)
- dt_matricula
- nota
- frequencia

### ENDERECO

- id_endereco (PK)
- rua
- numero
- bairro
- cidade
- estado

### EMAIL_ALUNO

- matricula (PK / FK)
- nome_email (PK)

### EMAIL_FUNCIONARIO

- matricula_funcional (PK / FK)
- nome_email (PK)

### PROFESSOR_DISCIPLINA

- matricula_funcional (FK)
- cod_disciplina (FK)

### CURSO_DISCIPLINA

- cod_disciplina (FK)
- cod_curso (FK)

### Resumo da Base de Dados

Atualmente o banco de dados possui:

- 50 endereços
- 5 cursos
- 30 disciplinas
- 20 funcionários
- 10 professores
- 5 coordenadores
- 100 alunos
- 100 e-mails de alunos
- 20 e-mails de funcionários
- 30 turmas
- 150 matrículas
- Relacionamentos N:M entre cursos e disciplinas
- Relacionamentos N:M entre professores e disciplinas

---

## 🔒 Regras de Integridade Implementadas

O banco foi desenvolvido utilizando restrições para garantir a consistência dos dados.

Foram implementadas:

- Chaves Primárias (PRIMARY KEY)
- Chaves Estrangeiras (FOREIGN KEY)
- Restrições UNIQUE
- Restrições CHECK
- Valores DEFAULT
- Integridade Referencial entre todas as entidades

Exemplos de validações:

- Nota entre 0 e 10
- Frequência entre 0% e 100%
- Salário maior que zero
- Turno limitado a Matutino, Vespertino ou Noturno
- Impedimento de matrícula duplicada na mesma turma


---

## 📊 Modelo Conceitual

O modelo conceitual representa a visão de negócio do sistema utilizando a abordagem Modelo-Entidade-Relacionamento (MER).

Ele contempla:

- Entidades;
- Relacionamentos;
- Cardinalidades;
- Especialização;
- Atributos compostos;
- Atributos multivalorados;
- Entidade associativa.

![Modelo Conceitual](./Modelo%20Conceitual%20-%20SISACAD.png)

---

## 🏗️ Modelo Lógico

O modelo lógico traduz o modelo conceitual para o modelo relacional.

Nesta etapa foram definidos:

- Chaves Primárias (PK);
- Chaves Estrangeiras (FK);
- Resolução de relacionamentos N:M;
- Estrutura das tabelas;
- Implementação da especialização.

![Modelo Lógico](./Modelo%20Logico%20-%20SISACAD.png)

---

## 🏛️ Arquitetura do Projeto

```
┌─────────────┐
│ PostgreSQL  │
└──────┬──────┘
       │
       ▼
┌────────────────┐
│ Python         │
│ psycopg2       │
└──────┬─────────┘
       │
       ▼
┌────────────────┐
│ API / Backend  │
│ FastAPI        │
└──────┬─────────┘
       │
       ▼
 ┌─────────────┐
 │  Power BI   │
 └─────────────┘
```

---

## 🛠️ Tecnologias Utilizadas e Planejadas

### Modelagem

- brModelo

### Banco de Dados

- PostgreSQL
- pgAdmin 4

### Backend

- Python
- psycopg2
- python-dotenv

### Backend (Planejado)

- FastAPI
- SQLAlchemy

### Business Intelligence (Futuro)

- Power BI

---

## 🐍 Aplicação Python

O projeto conta atualmente com uma aplicação Python integrada diretamente ao banco de dados PostgreSQL utilizando `psycopg2`.

A aplicação permite realizar operações de cadastro e autenticação de usuários do sistema.

### Funcionalidades implementadas

#### Cadastro de Alunos
- Cadastro de dados pessoais;
- Seleção do curso;
- Cadastro de endereço;
- Criação de usuário e senha;
- Confirmação dos dados antes da inserção;
- Geração automática da matrícula;
- Associação automática do aluno ao endereço cadastrado;
- Login do aluno.

#### Cadastro de Funcionários
- Cadastro de dados pessoais;
- Cadastro de data de admissão;
- Cadastro de salário;
- Cadastro de endereço;
- Campo de complemento opcional;
- Criação de senha;
- Confirmação dos dados antes da inserção;
- Geração automática da matrícula funcional;
- Associação automática do funcionário ao endereço cadastrado;
- Definição do tipo de funcionário:
- Professor;
- Coordenador.

---

### Estrutura

```
python/
├── cadastro-aluno.py
└── cadastro-funcionario.py
```

---

## 📦 Dados para Testes

O banco foi populado com dados fictícios para permitir a realização de consultas SQL e testes de integridade.

Atualmente o projeto possui registros para:

- Endereços
- Cursos
- Disciplinas
- Funcionários
- Professores
- Coordenadores
- Alunos
- E-mails
- Turmas
- Matrículas
- Relacionamentos entre cursos, disciplinas e professores

---

## 🔎 Consultas SQL Implementadas

Até o momento foram desenvolvidas consultas envolvendo diferentes níveis de complexidade, incluindo:

- Consultas básicas utilizando SELECT, WHERE e ORDER BY;
- Consultas com INNER JOIN entre múltiplas tabelas;
- Agrupamentos com GROUP BY;
- Funções de agregação (COUNT, AVG, SUM, MAX e MIN);
- Filtragem de grupos utilizando HAVING.

As consultas implementadas permitem gerar relatórios acadêmicos, estatísticas e indicadores sobre alunos, cursos, disciplinas, professores, turmas e matrículas, servindo como base para os futuros dashboards em Power BI.

---

## 📌 Status do Projeto

### Versão Atual: v0.3

#### Concluído:

- [x] Levantamento das regras de negócio
- [x] Modelagem Conceitual (MER)
- [x] Modelagem Lógica
- [x] Documentação inicial
- [x] Modelo Físico SQL
- [x] Implementação das restrições de integridade (CHECK, UNIQUE e DEFAULT)
- [x] Criação das tabelas associativas
- [x] População do banco com dados fictícios consistentes
- [x] Implementação das chaves primárias e estrangeiras
- [x] Consultas SQL básicas (SELECT, WHERE e ORDER BY)
- [x] Consultas com INNER JOIN
- [x] Consultas utilizando GROUP BY
- [x] Funções de agregação (COUNT, AVG, SUM, MAX e MIN)
- [x] Consultas utilizando HAVING
- [x] Estrutura inicial da aplicação Python
- [x] Integração Python + PostgreSQL
- [x] Configuração de variáveis de ambiente
- [x] Cadastro de alunos em Python
- [x] Login de alunos
- [x] Cadastro de funcionários em Python
- [x] Login de funcionários
- [x] Especialização de funcionários em Professor ou Coordenador
- [x] Recuperação automática de IDs gerados pelo PostgreSQL

#### Próxima fase:

- [ ] Validação dos dados de entrada
- [ ] Tratamento de exceções da aplicação
- [ ] Organização da aplicação em módulos
- [ ] API Python com FastAPI
- [ ] Consultas SQL avançadas
- [ ] Dashboard Power BI

—

## 🚀 Próximas Etapas

### Consultas SQL

- [x] Consultas básicas (SELECT, WHERE e ORDER BY)
- [x] INNER JOIN entre múltiplas tabelas
- [x] Agrupamentos utilizando GROUP BY
- [x] Funções de agregação
- [x] Consultas utilizando HAVING
- [ ] Consultas avançadas (CASE, CTE, SUBQUERY e Window Functions)
      
---

### Dashboard Power BI

- [ ] Quantidade de alunos por curso
- [ ] Evolução das matrículas
- [ ] Taxa de aprovação
- [ ] Média por disciplina
- [ ] Indicadores acadêmicos

---

### API Python

Exemplos de endpoints planejados:

```
GET /alunos
GET /cursos
GET /disciplinas
GET /turmas

POST /matriculas

GET /relatorios/aprovacao
GET /relatorios/notas
```

---

## 💡 Competências Desenvolvidas

Durante o desenvolvimento deste projeto foram aplicados conceitos de:

- Modelagem Conceitual (DER)
- Modelagem Lógica
- Banco de Dados Relacional
- Normalização
- Integridade Referencial
- Entidade Associativa
- Cardinalidades
- Generalização e Especialização
- Relacionamentos N:M
- PostgreSQL
- Análise de Requisitos
- Integridade de Dados
- Constraints SQL
- PostgreSQL
- SQL DDL
- SQL DML
- SQL DQL
- INNER JOIN
- GROUP BY
- HAVING
- Funções de Agregação
- Modelagem OLTP

---

## 📚 Aprendizados

Este projeto permitiu compreender como transformar regras de negócio em estruturas relacionais eficientes, aplicando conceitos fundamentais de Banco de Dados que servirão como base para projetos futuros envolvendo SQL, Engenharia de Dados, Business Intelligence e Desenvolvimento Backend. Também foram desenvolvidas consultas SQL voltadas à geração de relatórios gerenciais e indicadores acadêmicos, utilizando junções entre tabelas, agrupamentos e funções de agregação, preparando a base para análises em Business Intelligence. Este projeto também permitiu consolidar conhecimentos sobre modelagem de bancos de dados relacionais, normalização, integridade referencial, implementação física em PostgreSQL e manipulação de dados utilizando SQL. Além da modelagem conceitual e lógica, foram aplicadas restrições de integridade, inserção de dados consistentes e preparação da base para futuras consultas analíticas, integração com APIs em Python e construção de dashboards em Power BI. O projeto representa uma evolução prática no aprendizado de Banco de Dados, Engenharia de Software e fundamentos para atuação em Engenharia de Dados.

---

## 🤖 Uso de Inteligência Artificial no Desenvolvimento

Durante o desenvolvimento deste projeto, ferramentas de Inteligência Artificial foram utilizadas como apoio ao aprendizado, pesquisa e validação de conceitos, sem substituir o processo de análise, modelagem e implementação realizado pelo autor.

### Ferramentas Utilizadas

#### OpenAI ChatGPT
Utilizado para:
- Esclarecimento de conceitos de Banco de Dados
- Revisão da modelagem conceitual e lógica
- Discussão sobre cardinalidades e relacionamentos
- Apoio na documentação do projeto
- Sugestões de melhorias para o README
- Esclarecimento de conceitos de SQL e normalização
- Apoio na elaboração de desafios práticos de SQL para fixação do conteúdo
- Revisão da sintaxe e boas práticas de consultas SQL
- Discussão sobre estratégias de modelagem física e integridade de dados
- Apoio na organização da evolução do projeto e documentação técnica 

#### Google Gemini
Utilizado para:
- Pesquisa complementar de conceitos acadêmicos;
- Comparação de abordagens de modelagem;
- Apoio na estruturação da documentação;
- Revisão textual e validação de descrições do projeto.
- Apoio complementar na pesquisa de conceitos relacionados a Banco de Dados e SQL

### Forma de Utilização

As ferramentas de Inteligência Artificial foram utilizadas como apoio ao estudo e desenvolvimento do projeto, principalmente para:

- Esclarecimento de dúvidas conceituais;
- Revisão técnica de consultas SQL e modelagem;
- Discussão de alternativas de implementação;
- Organização e documentação do projeto;
- Sugestão de desafios práticos para consolidação do aprendizado.

Todas as implementações foram realizadas manualmente, sendo as sugestões analisadas e adaptadas conforme os requisitos do projeto.

### Responsabilidade sobre o Projeto
Todas as decisões de modelagem, regras de negócio, estrutura do banco de dados e evolução do projeto foram analisadas, adaptadas e implementadas pelo autor.
As ferramentas de IA foram utilizadas como assistentes de aprendizagem e produtividade, desempenhando papel semelhante ao de materiais de consulta, documentação técnica e tutoriais.
O objetivo foi potencializar o aprendizado prático em Engenharia de Software, Banco de Dados, SQL e análise de sistemas, mantendo a compreensão integral dos conceitos aplicados. As consultas SQL, a modelagem do banco de dados, as restrições de integridade e a documentação foram continuamente revisadas e ajustadas pelo autor durante o desenvolvimento, utilizando a IA como ferramenta de apoio técnico e de aprendizagem, e não como substituta da compreensão dos conceitos.

---

## 📈 Estatísticas do Projeto

Atualmente o projeto contém aproximadamente:

- 12 tabelas
- Mais de 400 registros
- Relacionamentos 1:1, 1:N e N:M
- Especialização (Generalização)
- Entidade Associativa
- Atributos Compostos
- Atributos Multivalorados
- Banco desenvolvido em PostgreSQL
- Mais de 40 consultas SQL desenvolvidas
- Consultas envolvendo até 4 tabelas em uma única instrução
- Relatórios utilizando GROUP BY, HAVING e funções de agregação
- Aplicação Python integrada ao PostgreSQL
- 2 módulos Python
- Autenticação de usuários
- Cadastro de alunos e funcionários

---

## 👨‍💻 Autor

### Nathan Luiz Almeida Vieira

Estudante de Engenharia de Software | Futuro Engenheiro de Dados e Desenvolvedor Backend

---

### GitHub

<p align="Left">
 </a>
  <a href="https://github.com/nathan-almeidadev"><img width="15px" alt="GitHub" title="GitHub" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg"/>  [github.com/nathan-almeidadev]
   
### LinkedIn 

<p align="Left">
 </a>
  <a href="https://www.linkedin.com/in/nathan-almeidavieira/"><img width="15px" alt="LinkedIn" title="LinkedIn" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linkedin/linkedin-original.svg"/>  [linkedin.com/in/nathan-almeidavieira]

---

⭐ Caso tenha gostado do projeto, fique à vontade para acompanhar a evolução.
