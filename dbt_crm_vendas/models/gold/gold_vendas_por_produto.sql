{{ config(materialized="view") }}

WITH vendas_por_produto AS (
    SELECT
        "data",
        "produto",
        SUM("valor") AS "valor_total",
        SUM("quantidade") AS "quantidade_total",
        COUNT(*) AS "total_vendas"
    FROM
        {{ ref("silver_vendas") }}
    WHERE
        "data" >= CURRENT_DATE - INTERVAL '6 days'
    GROUP BY
        "data", "produto"
)

SELECT
    "data",
    "produto",
    "total_vendas",
    "quantidade_total",
    "valor_total"
FROM
    vendas_por_produto
ORDER BY
    "data" ASC, "produto" ASC