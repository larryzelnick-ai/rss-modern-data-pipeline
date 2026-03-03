{{ config(
    materialized='incremental',
    unique_key='link'
) }}

with source_data as (

    select
        title,
        published as published_date,
        link,
        summary,
        source_feed
    from {{ ref('rss_raw_seed') }}

),

max_dates as (

    select max(published_date) as max_published_date
    from {{ this }}

)

select *
from source_data

{% if is_incremental() %}
where published_date > (
    select coalesce(max_published_date, '1900-01-01')
    from max_dates
)
{% endif %}
