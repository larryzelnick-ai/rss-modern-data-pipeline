{{ config(
    materialized='table'
) }}

select
    title,
    link,
    published_date,
    source_feed,
    strptime(published_date, '%a, %d %b %Y %H:%M:%S %z')::timestamp
from {{ ref('stg_rss_articles') }}
