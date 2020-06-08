# job-scraper
Scrapes and filters job offers from various sites.


plan:

- scrape target configurations -> save to json

- load json -> pass through keyword filter
- secondary (stricter) keyword filter (skip option)             (json of keywords for each filter)
- keyword search (any keyword) (skip option)
- strict keyword search (all keywords) (skip option)

- filter out non entry-level how? machine learning?!??
    - level-filter classes: keyword_level_filter, ml_level_filter...?

- save links to file