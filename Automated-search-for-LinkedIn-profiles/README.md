

# Automated search for profile names on LinkedIn

Have you ever thought about searching for profiles on LinkedIn and extract information out of it? Well, this repository is made for you !

If you think about it, when you look for profiles manually, you follow the steps below.

`Step 1 : Log into your LinkedIn account`

`step 2 : Type the name of the person on the search bar`

`step 3 : Write down the information you would like to extract`

Now, I want you to imagine you doing the same process for thousands of people, it's ofcourse tiresome and quite tedious work to do. Right?

Here in this repository, I have written the script to automate the exact same process to retrieve data frpm LinkedIn.

***Prerequistes***

`1. In the Authentication.txt file, make sure you put your email and password you use to log into your LinkedIn account`

`2. In the profiles.txt file, list out the names of the people you would like to search on LinkedIn`

E.g : The start looks like this;

![image](https://user-images.githubusercontent.com/76060198/167104904-e0af0a6b-ee6b-47d7-aa5c-56f9e5cd142e.png)

*Enter the number of pages you'd like to scrape per search result :*

![image](https://user-images.githubusercontent.com/76060198/167131193-39aee699-751c-4acb-b82c-1774b39f2743.png)

*Enter the number of key-words you'd like to search on LinkedIn :* this is the number of people you have on your list

`Of course not all search results have exactly the same number of pages but just type upto which page you'd like to go on and if there are search results that are
less or more than the number of pages you specified, the error will be ignored`

***`NB : You may be wondering why not go up to the end of the page for each search result? Well, technically, yes it's possible.`***

```How ?```

``` 
While True:
 
    # Unless the next button on LinkedIn is disabled, it will keep going
    
    if 'disabled' in next_button.get_attribute('class'):
        break
    else:
        next_button.click()
```

![#c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) However you have to also keep in mind that, LinkedIn search results are sorted by based on ***RELEVANCE.*** The people that are displayed on your primary pages are the ones
closer to you and your connections. So, that's why, I didn't need to search for the names through all the pages. 

`Finally, you will have the final extracted file in the same directory as your python script named as LinkedIn_xx. And you can of course change the *path* whenever you want`

`What the code does :`

https://user-images.githubusercontent.com/76060198/167689176-fdd0dc6f-8e14-429d-933f-14f16ee04c4b.mp4

`You may have noticed some duplicates, dont worry, there is a section of code to edit those out and export the lists in LinkedIn_xx.csv file`

`Behind the scenes :`

https://user-images.githubusercontent.com/76060198/167691850-a3470597-b1df-419b-92fd-1a4d1ddf9a4d.mp4

`Final output` : https://github.com/Haabiy/Search_for_profile_names/blob/5ef882afa2f0ac63f66bb6dd237b3b0371f7f70d/LinkedIn_xx.csv

*Data Analysis*

![image](https://user-images.githubusercontent.com/76060198/168495284-a5be14db-2c08-4c3c-a139-d53df393d05a.png)

![image](https://user-images.githubusercontent.com/76060198/168495310-c486ad6f-22c3-4fb1-8105-3e63ee465eb9.png)

![image](https://user-images.githubusercontent.com/76060198/168495331-59e293bf-3c08-4fc2-9886-58172e2e07a7.png)

![image](https://user-images.githubusercontent.com/76060198/168495368-0b773562-2ea4-405f-b4fa-e61554cf1799.png)

![image](https://user-images.githubusercontent.com/76060198/168576303-f6cbde19-4b7e-4ff1-9296-eadd4c50b8d3.png)

![image](https://user-images.githubusercontent.com/76060198/168495595-a90537c8-f8f0-4206-a003-e62987f0f342.png)

`Make sure 'Authentication' and 'profiles' are text files !`











