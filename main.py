import json
import job_filter

def save_jobs(jobs: list, file_name: str):
    with open(file_name, 'w') as f:
        for job in jobs:
            f.write(job['url'] + '\n')

# load lists
with open('blacklist.json') as f:
    blacklist = json.load(f)
with open('whitelist.json') as f:
    whitelist = json.load(f)


# make filter objects
blacklist_filter = job_filter.Blacklist(blacklist)
whitelist_filter = job_filter.Whitelist(whitelist)
strict_whitelist_filter = job_filter.StrictWhitelist(whitelist)
level_filter = job_filter.Level()

filter_list = [blacklist_filter, level_filter, whitelist_filter, strict_whitelist_filter]

# load jobs
with open('all_jobs.jl') as f:
    jobs = [ json.loads(line) for line in f ]
print(str(len(jobs)) + ' total')

# iteratively filter and ask to print filtered jobs to a file
for jfilter in filter_list:
    jobs = jfilter.filter(jobs)
    print(str(len(jobs)) + ' after ' + str(type(jfilter)))
    file_name = input('enter a filename to save job urls, enter nothing to skip: ')
    if file_name:
        save_jobs(jobs, file_name)

