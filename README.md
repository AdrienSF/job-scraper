# job-scraper
This project was built to scrape and filter job offers from Indeed and google job search. I chose to scrape Indeed and google jobs because the combination of these two seems to result in a relatively comprehensive coverage of the global IT job market, although I may add more sources in the future. Unfortunately spiders are forbidden on google job search (and scraping is infeasible due to it's design) so I devised a firefox extension that scrapes jobs from google job search and saves them to localstorage. Jobs are stored as json dict objects.

I created this project because I wanted to have more control over filtering/querrying jobs. I find job boards are laking in querry selectors and filters, and I've found it especially difficult to querry based on experience level (senior, mid level, entry level). Indeed US supports querries by experience level, but a large proportion of their results for "entry level" jobs for some reason expect applicants with significant experience. Ideally, I would have done this project with APIs, but I have yet to find a job board that offers an API for personal use (only corporate use).

As I am currently looking for jobs globally, the great volume of potential jobs is prohibitive to manual consideration. This project includes some filtering scripts who's primary purpose is to remove jobs I am not likely to be interested in, and jobs that are not entry level.

## Project status
Scrapers complete, filters in progress.

## Installation
You can clone or download this project, and run it after installing the scrapy python library.

## usage
This project was made with only my personal needs in mind, so some code will need to be edited to scrape for different jobs.

To scrape Indeed, run the spider called Indeed. The scrapy documentation details how to run a spider. jobscraper/spiders/Indeed_spider.py contains a variable called start_urls which is set to a list of urls of Indeed querries that interest me. The spider will scrape all results of the Indeed querries in this list.

To scrape google job search, prepare a list of urls corresponding to the google job search results you want to scrape. Then (make sure you have no google tabs open) go to firefox's about:debbuging page, select 'this firefox' and 'load temporary add-on'. Finally, open all of the prepared urls and job information will be saved to localstorage.

To use the filtering scripts, run main.py. To change the blacklist/ whitelist filters, edit the contents of blacklist.json and whitelist.json.
