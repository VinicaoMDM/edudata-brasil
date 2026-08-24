# Ambiente de desenvolvimento

Este documento descreve os requisitos e procedimentos necessários para executar o EduData Brasil em ambiente local.

## 1. Pré-requisitos

O projeto utiliza:

- Python 3.14+
- PostgreSQL 18+
- Git
- PowerShell no Windows

## 2. Clonar o projeto

```powershell
git clone https://github.com/VinicaoMDM/edudata-brasil.git
cd edudata-brasil
```
## 3. Criar ambiente virtual

```powershell
python -m venv .venv
```
Validar a instalação:
```powershell
python --version
python -m pip --version
```

## 4. Instalar dependências

Atualizar o pip:
```powershell
python -m pip install --upgrade pip
```
Instalar as dependências do projeto:
```powershell
python -m pip install -r requirements.txt
```
## 5. PostgreSQL

O PostgreSQL deve estar instalado e o servidor deve estar em execução.

Validar:
```powershell
pg_isready
```
O resultado esperado é semelhante a:

5432 - accepting connections

## 6. Banco de dados

Criar o banco de dados:
```powershell
psql -U postgres
```
Dentro do PostgreSQL:
```SQL
CREATE DATABASE edudata;
```
Sair:
```
\q
```
Conectar ao banco:
```powershell
psql -U postgres -d edudata
```
## 7. Encoding

O projeto utiliza UTF-8 para preservar corretamente caracteres da língua portuguesa.

No PowerShell:
```powershell
chcp 65001
$env:PGCLIENTENCODING="UTF8"
```
Validar no PostgreSQL:
```SQL
SHOW server_encoding;
SHOW client_encoding;
```
Ambos devem retornar:

UTF8


## 8. Variáveis de ambiente

Copiar o arquivo de exemplo:
```powershell
Copy-Item .env.example .env
```
O arquivo `.env` contém configurações locais do banco de dados e não deve ser versionado no Git.

O arquivo `.env.example` serve como referência para configuração do ambiente.

## 9. Estrutura principal
```text
edudata-brasil/
│
├── data/
│   ├── raw/
│   ├── staging/
│   └── processed/
│
├── docs/
│
├── notebooks/
│
├── sql/
│
├── src/
│   ├── extraction/
│   ├── transformation/
│   ├── loading/
│   └── analysis/
│
├── tests/
│
├── .env.example
├── requirements.txt
└── README.md
```
## 10. Princípio de reprodutibilidade

O projeto deve evitar dependências de configurações específicas de um computador.

Configurações locais devem ser mantidas no `.env`, enquanto configurações necessárias para reprodução do projeto devem ser documentadas e versionadas.

O objetivo é permitir que outro desenvolvedor consiga configurar o ambiente e executar o projeto seguindo apenas a documentação versionada no repositório.
