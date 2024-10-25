{{ config(materialized="view") }}

WITH fonte AS (
    SELECT
        "email",
        "data",
        "valor",
        "quantidade",
        "produto"
    FROM
        {{ ref("bronze_vendas") }}
),

dados_transformados AS (
    SELECT
        DATE("data") AS "data",
        "email" AS "vendedor",
        "produto",
        "quantidade",
        "valor"
    FROM
        fonte
    WHERE
        "valor" > 0
        AND "valor" < 10000
        AND "data" <= CURRENT_DATE
)

SELECT
    *
FROM
    dados_transformados