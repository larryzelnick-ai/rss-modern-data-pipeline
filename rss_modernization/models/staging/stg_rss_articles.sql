select
    title,
    published,
    link,
    summary
from read_csv_auto('data/rss_raw.csv')
