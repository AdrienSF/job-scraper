import scrapy


class Indeed(scrapy.Spider):
    name = "indeed"
    start_urls = [
        # indeed US
        # 'https://www.indeed.com/jobs?q=machine+learning&jt=fulltime&explvl=entry_level&l=CA',
        # 'https://www.indeed.com/jobs?q=software+engineer&jt=fulltime&explvl=entry_level&l=CA',
        # 'https://www.indeed.com/jobs?q=machine+learning&jt=fulltime&explvl=entry_level&l=MA',
        # 'https://www.indeed.com/jobs?q=software+engineer&jt=fulltime&explvl=entry_level&l=MA',
        # # # indeed FR
        # 'https://www.indeed.fr/emplois?q=software+engineer&jt=fulltime&explvl=entry_level',
        'https://www.indeed.fr/emplois?q=machine+learning&jt=fulltime&explvl=entry_level'
        # # indeed CH
        # 'https://www.indeed.ch/Stellen?q=software+engineer&l=GE&jt=fulltime&explvl=entry_level',
        # 'https://www.indeed.ch/Stellen?q=machine+learning&l=GE&jt=fulltime&explvl=entry_level'
    ]

    def parse(self, response):
        # for some reason (perhaps by design) going to the next page like this is not reliable. 
        # Could stop before all pages are visited.
        next_page = response.xpath('//a[@aria-label="Next"]/@href').get() #+ response.xpath('//a[@aria-label="Next"]/@data-pp').get()
        if next_page == None: # next button in french
            next_page = response.xpath('//a[@aria-label="Suivant"]/@href').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


        job_pages = response.xpath('//a[@data-tn-element="jobTitle"]/@href').getall()
        if job_pages: # in this case there are job pages to crawl
            for job in job_pages:
                yield response.follow(job, callback=self.parse)
        else:
            subtitle = response.xpath('//div[@class="jobsearch-InlineCompanyRating icl-u-xs-mt--xs  jobsearch-DesktopStickyContainer-companyrating"]').css('div::text').getall()
            employer = response.xpath('//a[@target="_blank"]/text()').get()
            if employer == None:
                employer = subtitle[0]
            # in this case we are already on a job page and we want to extract data
            yield {
                'title': response.xpath('//h3/text()').get(),
                'url': response.request.url,
                'location': subtitle[-1],
                'employer': employer,
                'description': response.xpath('//div[@id="jobDescriptionText"]').get()
            }


#with open('some.jl') as f:
    # return [ json.loads(line) for line in f]






