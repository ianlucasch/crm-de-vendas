from enum import Enum
from datetime import datetime
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt

class ProdutoEnum(str, Enum):
    """
    Modelo de produtos.
    """
    produto1 = "FlowDisk com Gemini"
    produto2 = "FlowDisk com ChatGPT"
    produto3 = "FlowDisk com Llama 3.0"

class Vendas(BaseModel):
    """
    Modelo de dados para vendas.

    Args:
        email (EmailStr): Email do vendedor
        data (datetime): Data da venda
        valor (PositiveFloat): Valor da venda
        quantidade (PositiveInt): Unidades vendidas
        produto (ProdutoEnum): Nome do produto vendido
    """
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum