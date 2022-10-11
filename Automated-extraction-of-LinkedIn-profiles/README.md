***Source :*** https://www.francemobilites.fr/cartographie-laureats#velo-cc

***File :*** [Laureats AAP 1 a 3 pour publiFM.xlsx](https://github.com/Haabiy/LinkedIn_profile_extraction/files/8638861/Laureats.AAP.1.a.3.pour.publiFM.2.xlsx)

# LinkedIn profile extraction
*Final exported file* : [Laureats.pdf](https://github.com/Haabiy/LinkedIn_profile_extraction/files/8601720/Laureats.pdf)


The idea of this project is to automate contact-info-collection process on LinkedIn making use of Python libraries( Selenium and Beautifulsoup)

***Prerequisites***
1. In the *Authentication.txt* file, make sure you put your email and password you use to log into your LinkedIn account
2. In the *Resized_data.txt* file, add key-words that you'd like to search on LinkedIn
3. In the *Job_titles.txt* file, put some job positions that you are interested in searching

***E.g : the start looks like***

![image](https://user-images.githubusercontent.com/76060198/167104904-e0af0a6b-ee6b-47d7-aa5c-56f9e5cd142e.png)

*Enter the number of pages you'd like to scrape per search result :*

![image](https://user-images.githubusercontent.com/76060198/167131193-39aee699-751c-4acb-b82c-1774b39f2743.png)

*Enter the number of key-words you'd like to search on LinkedIn :* have a look at ***Resized_data.txt***

***The whole process looks like :***

https://user-images.githubusercontent.com/76060198/167107190-72459703-29b0-4e9a-93fc-a5f9b62fe3b2.mp4

***You may have noticed some duplicates, dont worry, there is a section of code to edit those out and export the lists in LinkedIn_xx.csv file***

***Like this in this example :*** [LinkedIn_xx.csv](https://github.com/Haabiy/LinkedIn_profile_extraction/files/8639082/LinkedIn_xx.csv)

***Behind the scenes : sample***

https://user-images.githubusercontent.com/76060198/167112334-752eb4dd-4e0b-4151-a127-726a8764c479.mp4

`Final output`

![image](https://user-images.githubusercontent.com/76060198/167960692-785e2120-a6e0-4ad9-8fde-fd208f60ba19.png)

`Make sure Authentication, Data, Resized_data, and Job_titles are text files !`






