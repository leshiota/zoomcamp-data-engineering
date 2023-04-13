{{ config(materialized='view') }}

select 
*
from {{ source('staging','rides') }}
limit 100