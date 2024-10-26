{% docs __overview__ %}

# Projeto DBT Core para CRM de Vendas

Este projeto utiliza DBT (Data Build Tool) para gerenciar e transformar dados de um sistema de CRM de Vendas. O objetivo é criar um pipeline de dados robusto e eficiente que trata e organiza os dados de vendas para análise.

## Estrutura de diretórios

```plaintext
├── models
│   ├── bronze
│   │   ├── bronze_vendas.sql
│   │   └── schema.yml
│   ├── gold
│   │   ├── gold_vendas_por_produto.sql
│   │   ├── gold_vendas_por_vendedor.sql
│   │   └── schema.yml
│   ├── silver
│   │   ├── schema.yml
│   │   └── silver_vendas.sql
│   └── sources.yml
└── dbt_project.yml
```

## Estrutura do projeto

### 1. Models

Os models definem as transformações dos dados usando SQL. Eles são divididos em três camadas principais: bronze, silver e gold.

#### Bronze

A camada bronze é responsável por carregar os dados brutos para que posteriormente sejam transformados.

- **bronze_vendas.sql**: Carrega os dados brutos da tabela vendas.

#### Silver

A camada silver é responsável por limpar e transformar os dados antes que eles sejam carregados nas tabelas finais de análise.

- **silver_vendas.sql**: Recebe os dados da view bronze_vendas e faz as devidas transformações.

#### Gold

A camada gold é onde os dados finais de análise são armazenados. Eles são baseados nos dados transformados pela camada silver.

- **gold_vendas_por_produto.sql**: Integra os dados da view silver_vendas, criando um modelo de dados de vendas por produto para análise final.
- **gold_vendas_por_vendedor.sql**: Integra os dados da view silver_vendas, criando um modelo de dados de vendas por vendedor para análise final.

### 2. Sources

Os sources são as tabelas ou arquivos de origem dos dados que o DBT utiliza para realizar as transformações.

## Executando o projeto

### Requisitos

- Python 3.12.3
- PostgreSQL
- DBT

### Passos para execução

1. Clone o repositório localmente:
   ```bash
   git clone https://github.com/ianlucasch/crm-de-vendas.git
   ```


2. Acesse a pasta do projeto:
   ```bash
   cd crm-de-vendas
   ```


3. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate
   ```


4. Instale o DBT:
   ```bash
   pip install dbt-postgres
   ```


5. Crie um novo projeto DBT:
   ```bash
   dbt init dbt_crm_vendas
   cd dbt_crm_vendas
   ```


6. Configure a conexão com PostgreSQL:

   Configure o arquivo `profiles.yml` com suas variáveis de ambiente para conectar o DBT ao PostgreSQL. O arquivo deve estar no diretório `~/.dbt/` ou no diretório especificado pela variável de ambiente `DBT_PROFILES_DIR`.

   Exemplo de `profiles.yml`:
   ```yaml
   dbt_crm_vendas:
      outputs:
         dev:
            dbname: <DB_NAME>
            host: <DB_HOST>
            pass: <DB_PASS>
            port: <DB_PORT>
            schema: public
            threads: 1
            type: postgres
            user: <DB_USER>
      target: dev
   ```


7. Verifique o estado do projeto:
   ```bash
   dbt debug
   ```


8. Execute as transformações do DBT:
   ```bash
   dbt run
   ```

{% enddocs %}