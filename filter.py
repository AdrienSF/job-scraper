from abc import ABC, abstractmethod

class Filter(ABC):
 
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def passes_filter(self, job):
        pass

    def filter(self, jobs: list):
        return [ job in jobs if passes_filter(job) ]




class Blacklist(Filter):
    
        def __init__(self, blacklist: list):
            self.blacklist = blacklist
        super().__init__()

        def passes_filter(self, job):
            return any... in self.blacklist


class whitelist(Filter):
    pass


class Strict_Whitelist(Filter):
    pass


class Level(Filter):
    pass # ????? mystery how to do this one