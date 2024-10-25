import os
import psycopg2
import streamlit as st
from psycopg2 import sql
from contrato import Vendas
from dotenv import load_dotenv

load_dotenv(".env")

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = os.getenv("DB_PORT")

def salvar_no_postgres(dados: Vendas):
    """
    Função para criar a tabela vendas e salvar os dados no banco de dados PostgreSQL.
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        cursor = conn.cursor()

        create_table = sql.SQL(
            "CREATE TABLE IF NOT EXISTS vendas (id SERIAL PRIMARY KEY, email VARCHAR(255) NOT NULL, data TIMESTAMP NOT NULL, valor NUMERIC NOT NULL, quantidade INTEGER NOT NULL, produto VARCHAR(50) NOT NULL)"
        )
        cursor.execute(create_table)

        insert_query = sql.SQL(
            "INSERT INTO vendas (email, data, valor, quantidade, produto) VALUES (%s, %s, %s, %s, %s)"
        )
        cursor.execute(insert_query, (
            dados.email,
            dados.data,
            dados.valor,
            dados.quantidade,
            dados.produto.value,
        ))

        conn.commit()
        cursor.close()
        conn.close()
        st.success("Dados salvos com sucesso no banco de dados!")
    except Exception as exc:
        st.error(f"Erro ao salvar no banco de dados: {exc}")