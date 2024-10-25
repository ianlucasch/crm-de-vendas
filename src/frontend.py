import streamlit as st
from contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError
from database import salvar_no_postgres

def main():
    """
    Função para criar o frontend do CRM de Vendas.
    """
    st.title("CRM De Vendas - Frontend Simples")
    email = st.text_input("Email do vendedor")
    produto = st.selectbox("Selecione o produto", options=["FlowDisk com Gemini", "FlowDisk com ChatGPT", "FlowDisk com Llama 3.0"])
    data = st.date_input("Data da venda", datetime.now())
    hora = st.time_input("Hora da venda", value=time(9, 0))
    quantidade = st.number_input("Unidades vendidas", min_value=1, step=1)
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")

    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data, hora)
            venda = Vendas(
                email=email,
                data=data_hora,
                valor=valor,
                quantidade=quantidade,
                produto=produto,
            )
            st.write(venda)
            salvar_no_postgres(venda)
        except ValidationError as exc:
            st.error(f"Erro: {exc}")

if __name__ == "__main__":
    main()