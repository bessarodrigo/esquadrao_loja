#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import locale
import re


# In[19]:


# Passo 1: gerar o DataFrame

# Definir o locale para Português do Brasil (pt_BR)
locale.setlocale(locale.LC_NUMERIC, 'pt_BR.UTF-8')

# Caminho do arquivo Excel
excel_file = r'C:/Caminho/Para/Sua/Pasta'

# Leitura do arquivo Excel e seleção das colunas desejadas
df = pd.read_excel(excel_file, sheet_name='Sheet1', usecols=['Data', 'Valor', 'Status', 'Info. Compl'])

# Exibir as primeiras linhas do DataFrame
print(df.head())

# Exibir os tipos de dados originais
print(df.dtypes)


# In[20]:


# Passo 2: Renomear e ajustar os tipos de dados
# Renomear as colunas
df.rename(columns={
    'Data': 'data',
    'Valor': 'valor',
    'Status': 'status',
    'Info. Compl': 'info_compl'
}, inplace=True)

# Função para converter valor para float
def convert_valor(valor):
    # Remover pontos que são separadores de milhar
    valor = re.sub(r'\.(?=\d{3})', '', valor)
    # Substituir vírgulas por pontos
    valor = valor.replace(',', '.')
    return float(valor)

# Aplicar a função de conversão na coluna 'valor'
df['valor'] = df['valor'].astype(str).apply(convert_valor)

# Converter a coluna 'data' para Timestamp
try:
    df['data'] = pd.to_datetime(df['data'])
except ValueError as e:
    print(f"Não foi possível converter a coluna 'data' para Timestamp: {e}")

# Exibir as primeiras linhas do DataFrame após as correções
print(df.head(10))

# Exibir os tipos de dados após as alterações
print(df.dtypes)


# In[21]:


# Passo 3: Inserir dados no banco de dados PostgreSQL
try:
    # Definir a string de conexão com o banco de dados PostgreSQL
    postgres_str = 'postgresql://user:password@localhost:5432/esquadrao'

    # Criar uma conexão com o banco de dados
    engine = create_engine(postgres_str)

    with engine.connect() as connection:
        print("Conexão com o banco de dados estabelecida com sucesso!")

        # Nome do esquema e da tabela no banco de dados
        schema_name = 'seu_schema'
        table_name = 'sua_tabela'

        # Exibir as colunas da tabela no banco de dados
        query = f"""
        SELECT column_name 
        FROM information_schema.columns 
        WHERE table_schema = '{schema_name}' AND table_name = '{table_name}';
        """
        result = connection.execute(query)
        columns_in_db = [row[0] for row in result]
        print("Colunas no banco de dados:", columns_in_db)

        # Remover a coluna 'id_venda' do banco de dados das colunas do DataFrame, se necessário
        if 'id_venda' in columns_in_db:
            columns_in_db.remove('id_venda')

        # Verificar se as colunas do DataFrame correspondem agora às colunas no banco de dados
        if set(df.columns) != set(columns_in_db):
            print("Aviso: As colunas do DataFrame não correspondem exatamente às colunas no banco de dados após as correções.")
            print("Colunas do DataFrame:", df.columns)
            print("Colunas no banco de dados (sem ID):", columns_in_db)

        # Limpar a tabela no banco de dados
        clear_table_query = f"TRUNCATE TABLE {schema_name}.{table_name};"
        connection.execute(clear_table_query)
        print(f"Tabela {schema_name}.{table_name} limpa com sucesso!")

        # Inserir os dados no banco de dados especificando o esquema
        df.to_sql(table_name, engine, schema=schema_name, if_exists='append', index=False)
        print("Dados inseridos no banco de dados com sucesso!")

except OperationalError as oe:
    print(f"Erro de conexão com o banco de dados: {oe}")
except Exception as e:
    print(f"Erro ao inserir dados no banco de dados: {e}")

