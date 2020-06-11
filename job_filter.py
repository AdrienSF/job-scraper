from abc import ABC, abstractmethod

class Filter(ABC):
    
    @abstractmethod
    def passes_filter(self, job):
        pass

    def filter(self, jobs: list):
        return [ job for job in jobs if self.passes_filter(job) ]



# word filters are case insensitive
class Blacklist(Filter):
        # takes a dict containing title blacklist, location blacklist description blacklist...
        def __init__(self, blacklist: dict):
            self.blacklist = blacklist

        def passes_filter(self, job: dict):
            # check if any blacklisted title is in the job title, any blacklisted location is in job['location']...
            return not any([ any([ bad_word.lower() in job[prop].lower() for bad_word in self.blacklist[prop] ]) for prop in self.blacklist ])



class Whitelist(Filter):
        # takes a dict containing title whitelist, location whitelist description whitelist...
        def __init__(self, whitelist: dict):
            self.whitelist = whitelist

        def passes_filter(self, job: dict):
            # check if any whitelisted title is in the job title, any whitelisted location is in job['location']...
            return any([ any([ good_word.lower() in job[prop].lower() for good_word in self.whitelist[prop] ]) for prop in self.whitelist ])


class StrictWhitelist(Filter):
        # takes a dict containing title whitelist, location whitelist description whitelist...
        def __init__(self, whitelist: dict):
            self.whitelist = whitelist

        def passes_filter(self, job: dict):
            # check if all whitelisted titles are in the job title, all whitelisted locations are in job['location']...
            return all([ all([ good_word.lower() in job[prop].lower() for good_word in self.whitelist[prop] ]) for prop in self.whitelist ])


class Level(Filter):
    def passes_filter(self, job: dict):
        # if a job description contains phd but not bachelor, it's not entry level
        phd_words = ['postdoc', 'post-doc', 'postgraduate', 'post-graduate', 'post graduate', 'phd', 'ph.d']
        bachelor_words = ['bachelor', 'b.sc']
        # if contains a phd word but no bachelor word
        if any([ phd_word in job['description'].lower() for phd_word in phd_words ]) and not any([ bachelor_word in job['description'] for bachelor_word in bachelor_words ]):
            return False

        # if any of the following in the title, then not entry level 
        title_blacklist = ['postdoc', 'professor', 'lecturer', 'senior', 'postgraduate', 'manager', 'mid-level', 'mid level']
        if any([ word in job['title'].lower() for word in title_blacklist ]):
            return False

        # if any of the following in the description, then not entry level 
        description_blacklist = ['senior', 'mid-level', 'mid level', 'at least 3 year', "mid-career", "late-career", "mid career", "late career"]
        if any([ word in job['description'].lower() for word in description_blacklist ]):
            return False

        return True


# normal blacklists:
# title: "intern", "co-op", "postdoc", "fellowship", "client serv", "lead", "assist", "test"
# description: "group lead", "client facing", "client-facing", "microcontrollers", "natural language", "nlp", " assembly ", " hardware ", "mobile front end", "mobile front-end", "front end mobile", "front-end mobile"


