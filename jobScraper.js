
function appendToJobs(job) {
  if (localStorage.jobs){
    jobs = JSON.parse(localStorage.jobs);
  }else{
    jobs = [];
  }
  jobs.push(job);
  localStorage.jobs = JSON.stringify(jobs);
}


async function scrape(){
  // load jobs ----------------
  console.log("jobScraper loaded");
  await new Promise(r => setTimeout(r, 5000));
  console.log('waited 5 sec for page to load');
  // scroll down in search results to load them all
  jobScroller = document.getElementsByClassName('zxU94d gws-plugins-horizon-jobs__tl-lvc')[0];

  lastLength = 0;
  jobCards = document.getElementsByClassName('hide-focus-ring gws-plugins-horizon-jobs__tl-lif');
  while (lastLength != jobCards.length){
    lastLength = jobCards.length
    jobScroller.scrollBy(0, 10000); //scroll down a lot
    // sleep, wait for jobcards to load
    await new Promise(r => setTimeout(r, 2000));
    jobCards = document.getElementsByClassName('hide-focus-ring gws-plugins-horizon-jobs__tl-lif');
    console.log('jobcards last loaded: ' + lastLength + ' | jobcards loaded: ' + jobCards.length);
  }
  console.log('loaded jobcards');
  // loaded jobs --------------

  // get job info
  console.log('extracting job info...');
  titles = [];
  urls = [];
  locations = [];
  descriptions = [];
  employers = [];
  titleParents = document.getElementsByClassName('KLsYvd');
  for (let index = 0; index < titleParents.length; index++) {
    titles.push(titleParents[index].textContent);
  }

  locationParents = document.getElementsByClassName('tJ9zfc');
  for (let index = 0; index < locationParents.length; index++) {
    employers.push(locationParents[index].children[0].innerHTML);
    locations.push(locationParents[index].children[1].innerHTML);
  }

  descriptionElements = document.getElementsByClassName('HBvzbc');
  for (let index = 0; index < descriptionElements.length; index++) {
    descriptions.push(descriptionElements[index].textContent);
    urls.push(descriptionElements[index].baseURI);
  }

  for (let index = 0; index < titles.length; index++) {
    message = titles[index] + " | " + employers[index] + " | " + locations[index] + " | " + urls[index] + "\n\n";
    console.log(message);
    job = {
      'title': titles[index],
      'url': urls[index],
      'location': locations[index],
      'employer': employers[index],
      'description': descriptions[index]
    };

    appendToJobs(job);
  }

  console.log('scraped: ' + titles.length + ' jobs');
  console.log('done');

}



scrape();
/* google job searches who's results I want to export:
https://www.google.com/search?q=entry+level+software+engineer+MA+USA&ibp=htl;jobs&rciv=jb&sa=X&ved=2ahUKEwiRo5XnjfTpAhUKDmMBHSw4CKcQiJcCKAF6BAgKEAw#fpstate=tldetail&htivrt=jobs&htidocid=-wLssMYfWO29T_bqAAAAAA%3D%3D
https://www.google.com/search?q=entry+level+software+engineer+CA+USA&ibp=htl;jobs&rciv=jb&sa=X&ved=2ahUKEwiRo5XnjfTpAhUKDmMBHSw4CKcQiJcCKAF6BAgKEAw#fpstate=tldetail&htivrt=jobs&htidocid=-wLssMYfWO29T_bqAAAAAA%3D%3D
https://www.google.com/search?q=entry+level+software+engineer+France&ibp=htl;jobs&rciv=jb&sa=X&ved=2ahUKEwiRo5XnjfTpAhUKDmMBHSw4CKcQiJcCKAF6BAgKEAw#fpstate=tldetail&htivrt=jobs&htichips=employment_type:FULLTIME&htischips=employment_type;FULLTIME&htidocid=XLhYc7fHY7CKyB-TAAAAAA%3D%3D
https://www.google.com/search?q=entry+level+software+engineer+Geneva&ibp=htl;jobs&rciv=jb&sa=X&ved=2ahUKEwiRo5XnjfTpAhUKDmMBHSw4CKcQiJcCKAF6BAgKEAw#fpstate=tldetail&htivrt=jobs&htichips=employment_type:FULLTIME&htischips=employment_type;FULLTIME&htidocid=69TfUAqurr6B46teAAAAAA%3D%3D

https://www.google.com/search?q=entry+level+machine+learning+MA+USA&ibp=htl;jobs&rciv=jb&sa=X&ved=2ahUKEwiRo5XnjfTpAhUKDmMBHSw4CKcQiJcCKAF6BAgKEAw#fpstate=tldetail&htivrt=jobs&htidocid=-wLssMYfWO29T_bqAAAAAA%3D%3D
https://www.google.com/search?q=entry+level+machine+learning+CA+USA&ibp=htl;jobs&rciv=jb&sa=X&ved=2ahUKEwiRo5XnjfTpAhUKDmMBHSw4CKcQiJcCKAF6BAgKEAw#fpstate=tldetail&htivrt=jobs&htidocid=-wLssMYfWO29T_bqAAAAAA%3D%3D
https://www.google.com/search?q=entry+level+machine+learning+France&ibp=htl;jobs&rciv=jb&sa=X&ved=2ahUKEwiRo5XnjfTpAhUKDmMBHSw4CKcQiJcCKAF6BAgKEAw#fpstate=tldetail&htivrt=jobs&htichips=employment_type:FULLTIME&htischips=employment_type;FULLTIME&htidocid=XLhYc7fHY7CKyB-TAAAAAA%3D%3D
https://www.google.com/search?q=entry+level+machine+learning+Geneva&ibp=htl;jobs&rciv=jb&sa=X&ved=2ahUKEwiRo5XnjfTpAhUKDmMBHSw4CKcQiJcCKAF6BAgKEAw#fpstate=tldetail&htivrt=jobs&htichips=employment_type:FULLTIME&htischips=employment_type;FULLTIME&htidocid=69TfUAqurr6B46teAAAAAA%3D%3D
*/