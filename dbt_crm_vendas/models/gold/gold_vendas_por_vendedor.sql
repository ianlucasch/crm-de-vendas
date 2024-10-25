{{ config(materialized="view") }}

WITH vendas_por_vendedor AS (
    SELECT
        "data",
        "vendedor",
        SUM("valor") AS "valor_total",
        SUM("quantidade") AS "quantidade_total",
        COUNT(*) AS "total_vendas"
    FROM
        {{ ref("silver_vendas") }}
    WHERE
        "data" >= CURRENT_DATE - INTERVAL '6 days'
    GROUP BY
        "data", "vendedor"
)

SELECT
    "data",
    "vendedor",
    "total_vendas",
    "quantidade_total",
    "valor_total"
FROM
    vendas_por_vendedor
ORDER BY
    "data" ASC, "vendedor" ASC