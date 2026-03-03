{{ config(
    materialized='table'
) }}

select
    date_trunc('day', strptime(published_date, '%a, %d %b %Y %H:%M:%S %z')) as date_day
from {{ ref('stg_rss_articles') }}
group by 1
order by 1
