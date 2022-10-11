from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import codecs
from unidecode import unidecode
from sign_in import driver as driver

# Store lists, initializing multiple lists
name, position, location, getlinklist = ([] for i in range(4))
filteredname, filteredposition, filteredlocation, filteredgetlinklist = ([] for j in range(4))
jobtitlesen, searchmore = ([] for k in range(2))
num_of_people = 10

class home():
    # This function gets all the data from Resized_data.txt and does the search
    def searchmorelink(self, t):
        self.t = t
        # Finding the search bar by XPATH
        search_ = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
        # Make sure to include encoding in case the text has French or other non-English letters
        openfile = open("Resized_data.txt", encoding="utf-8")
        tkeyword = openfile.readlines()
        self.keyword = tkeyword[self.t].lower().strip()
        self.unikeyword = unidecode(self.keyword.strip())
        search_.send_keys(self.keyword)
        driver.maximize_window()
        search_.send_keys(Keys.RETURN)
        sleep(3)
        # We are only interested in search results of people, not companies nor posts or others
        # Sometimes, the filter "People" on linkedIn would either be in the first or second index
        # Make sure python gets that right and handles any exception raised
        try:
           driver.execute_script("document.getElementsByClassName('artdeco-pill artdeco-pill--slate artdeco-pill--choice artdeco-pill--2 search-reusables__filter-pill-button search-reusables__filter-pill-button')[0].click();")
        except Exception:
            driver.execute_script("document.getElementsByClassName('artdeco-pill artdeco-pill--slate artdeco-pill--choice artdeco-pill--2 search-reusables__filter-pill-button search-reusables__filter-pill-button')[1].click();")
        sleep(2)
    # This function looks for names, position, locations and LinkedIn URLS
    # And it stores them accordingly
    def page(self):
        sleep(2)
        # Get access to the html of the page
        soup = BeautifulSoup(driver.page_source, "html.parser")
        # I always start from the top and I'll go deeper eventually
        # Start from the body where you could access pretty much everything of the page source
        body = soup.find("body")
        main = body.find("main", {"id": "main"})
        # Finds the location of the profile names and stores them
        for divclass in main.find_all("span", {"class": "entity-result__title-text t-16"}):
            try:
                # If it couldn't find y, then there would be an error.
                # This is specifically targeted to fetch LinkedIn members that I don't have connection with
                divclass.find_all("span", {"dir": "ltr"})[0].text.strip()
                for xx in divclass.find_all("span", {"dir": "ltr"}):
                    try:
                        getnames = xx.find_all("span")[0].text.strip()
                        name.append(getnames)
                    except Exception:
                        pass
            # There are some errors to handle
            # E.g :
            # 1. If there is no name in the profile
            # 2. If the profile is someone who you don't have a connection to, it'll appear as a " LinkedIn member"
            except Exception:
                name.append("Linkedin member")
            # Get the URLs of each LinkedIn profile
            try:
                a = divclass.find("a", href=True)
                if a.text:
                    getlinklist.append(a['href'])
            except Exception:
                pass
        # The number of people appearing on a page is 10 or less
        # If it's less then, handle the error as "pass" which will ignore it
        for main in body.find_all("main", {"id": "main"}):
            for i in range(0, num_of_people):
                try:
                    getposition = main.find_all("div", {"class": "entity-result__primary-subtitle t-14 t-black t-normal"})[i].text.strip()
                    position.append(getposition)
                except AttributeError:
                    pass
                try:
                    getlocation = main.find_all("div", {"class": "entity-result__secondary-subtitle t-14 t-normal"})[i].text.strip()
                    location.append(getlocation)
                except AttributeError:
                    pass
        sleep(3)
    # When printing, put in mind that, we only need profiles related to the specified job titles
    def printdata(self, w, x, y, z):
        sleep(1)
        for t in range(0, len(w)):
            try:
                print(t+1, ".", w[t], x[t], y[t], z[t])
                # We don't need the LinkedIn member as we don't have their UNIQUE URLs
                # Make sure we don't miss profiles due to uppercase and lowercase issue
                # We only need profiles with position related to the given list...refer to Resized_data.txt
                # So, change every position to lowercase and see if there are matches
                lowered = x[t].lower()
                unilowered_ = unidecode(lowered)
                if ((unilowered_.find(self.unikeyword) != -1) and (w[t] != "Linkedin member")):
                    with codecs.open("Job_titles.txt", 'r', encoding='utf-8') as job:
                        readl = job.readlines()
                        for kk in range(len(readl)):
                            jobtfr = readl[kk].lower().strip()
                            jobten = unidecode(jobtfr).lower().strip()
                            _unilowered_ = unidecode(lowered)
                            if ((_unilowered_.find(jobten) != -1)):
                                filteredname.append(w[t]), filteredposition.append(x[t]), filteredlocation.append(y[t]), filteredgetlinklist.append(z[t])
                                print("...................", w[t], x[t], y[t], z[t])
                            else:
                                pass
                else:
                    pass
            except IndexError:
                pass





