# 🎓 Sistema Acadêmico Universitário (SISACAD) — Universidade PortfólioHUB

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![Database](https://img.shields.io/badge/Database-PostgreSQL-blue)
![Backend](https://img.shields.io/badge/Future-Python-green)
![BI](https://img.shields.io/badge/Future-PowerBI-orange)

Este repositório contém o desenvolvimento completo do SISACAD (Sistema Acadêmico Universitário), projetado como meu primeiro projeto de portfólio durante o primeiro semestre de Engenharia de Software.

O projeto contempla todas as etapas de modelagem de banco de dados, desde a compreensão das regras de negócio até a construção dos modelos conceitual e lógico, servindo como base para futuras implementações físicas em SQL, integração com APIs em Python e análises em Power BI.

O principal objetivo é aplicar, de forma prática, conceitos fundamentais de bancos de dados relacionais (OLTP), garantindo integridade, consistência, redução de redundâncias e aderência às boas práticas de modelagem.

**Observação:** Este projeto foi desenvolvido com apoio das ferramentas de Inteligência Artificial OpenAI ChatGPT e Google Gemini como recursos complementares de estudo, revisão e documentação.

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
├── Casa
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

### PROFESSOR

- matricula_funcional (PK/FK)
- titulacao
- area_atuacao

### COORDENADOR

- matricula_funcional (PK/FK)
- cod_curso (FK/UNIQUE)
- tempo_coordenacao

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

- id_email (PK)
- matricula (FK)
- email

### EMAIL_FUNCIONARIO

- id_email (PK)
- matricula_funcional (FK)
- email

### PROFESSOR_DISCIPLINA

- matricula_funcional (FK)
- cod_disciplina (FK)

### DISCIPLINA_CURSO

- cod_disciplina (FK)
- cod_curso (FK)

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

## 🏛️ Arquitetura Planejada

```
┌─────────────┐
│ PostgreSQL  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Python API  │
│ FastAPI     │
└──────┬──────┘
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

### Backend (Futuro)

- Python
- FastAPI
- Flask
- SQLAlchemy

### Business Intelligence (Futuro)

- Power BI

---

## 📌 Status do Projeto

### Versão Atual: v0.1

#### Concluído:

- [x] Levantamento das regras de negócio
- [x] Modelagem Conceitual (MER)
- [x] Modelagem Lógica
- [x] Documentação inicial

#### Em desenvolvimento:

- [ ] Modelo Físico SQL
- [ ] Inserção de dados fictícios
- [ ] Consultas SQL
- [ ] Dashboard Power BI
- [ ] API Python

—

## 🚀 Próximas Etapas

### Banco de Dados Físico

- [ ] Criar script schema.sql
- [ ] Definir constraints
- [ ] Implementar chaves estrangeiras
- [ ] Criar índices

---

### População de Dados

- [ ] Criar seed.sql
- [ ] Gerar dados fictícios
- [ ] Simular ambiente acadêmico

---

### Consultas SQL

- [ ] Alunos por curso
- [ ] Disciplinas por curso
- [ ] Professores por disciplina
- [ ] Histórico acadêmico do aluno
- [ ] Média de notas por disciplina
- [ ] Taxa de aprovação
- [ ] Ranking de alunos por curso

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
- SQL
- PostgreSQL
- Análise de Requisitos

---

## 📚 Aprendizados

Este projeto permitiu compreender como transformar regras de negócio em estruturas relacionais eficientes, aplicando conceitos fundamentais de Banco de Dados que servirão como base para projetos futuros envolvendo SQL, Engenharia de Dados, Business Intelligence e Desenvolvimento Backend.

---

## 🤖 Utilização de Inteligência Artificial
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

#### Google Gemini
Utilizado para:
- Pesquisa complementar de conceitos acadêmicos;
- Comparação de abordagens de modelagem;
- Apoio na estruturação da documentação;
- Revisão textual e validação de descrições do projeto.
### Responsabilidade sobre o Projeto
Todas as decisões de modelagem, regras de negócio, estrutura do banco de dados e evolução do projeto foram analisadas, adaptadas e implementadas pelo autor.
As ferramentas de IA foram utilizadas como assistentes de aprendizagem e produtividade, desempenhando papel semelhante ao de materiais de consulta, documentação técnica e tutoriais.
O objetivo foi potencializar o aprendizado prático em Engenharia de Software, Banco de Dados, SQL e análise de sistemas, mantendo a compreensão integral dos conceitos aplicados.

---

## 👨‍💻 Autor

### Nathan Luiz Almeida Vieira

Estudante de Engenharia de Software | Futuro Engenheiro de Dados e Desenvolvedor Backend

---

### GitHub

[github.com/nathan-almeidadev](https://github.com/nathan-almeidadev)

### LinkedIn

[linkedin.com/in/nathan-almeidavieira](https://www.linkedin.com/in/nathan-almeidavieira/)

---

⭐ Caso tenha gostado do projeto, fique à vontade para acompanhar a evolução.
