from sign_in import driver
from __home import home, name, position, location, getlinklist
from time import sleep
from selenium.webdriver.common.by import By

# Scrolldown scrolls by clicking next until the specified page
# Goes through Resized_data lists
# In fact, instead of a user entering interval of pages, we could click until the button is disabled
# and Python knows that is the dead-end of the list.
# However, don't forget also LinkedIn search results are based on "Relevance" where you don't need to go until the end
# of a page of one search result. Technically it's possible but I have not used that methodology in this code but I have
# commented just the logic in case you'd like to do it that way.
def scrolldown():
    pgs = int(input("Enter the number of pages you'd like to scrape per search result :"))
    key_terms = int(input("Enter the number of key-words you'd like to search on LinkedIn : "))
    print("___...___")
    x = home()
    for pagesx in range(0, key_terms):
        driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input').clear()
        x.searchmorelink(pagesx)
        sleep(1)
        for pagesy in range(0, pgs):
            try:
                x.page()
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                next_button = driver.find_element(By.CLASS_NAME, "artdeco-pagination__button--next")
                next_button.click()
            except Exception:
                pass
        # Feed the stored data
        x.printdata(name, position, location, getlinklist)

# The idea is to Click "Next" until the next button is disabled and that is the end of the page for any key term searches on LinkedIn
# Use "While True":
#if 'disabled' in next_button.get_attribute('class'):
    #break
#else:
    #next_button.click()


