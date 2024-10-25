{{ config(materialized="view") }}

WITH dados_brutos AS (
    SELECT
        *
    FROM
        {{ source("crm_vendas_source", "vendas") }}
)

SELECT
    *
FROM
    dados_brutos