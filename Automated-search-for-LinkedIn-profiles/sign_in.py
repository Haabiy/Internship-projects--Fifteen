from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

# Chose Chrome as my web browser
driver = webdriver.Chrome(ChromeDriverManager().install())
def signin():
    # Find the location by ID where the email section, do the same for password and logging
    url = "https://www.linkedin.com/login"
    driver.get(url)
    email = driver.find_element(By.ID, ("username"))
    password = driver.find_element(By.ID, ("password"))
    driver.find_element(By.CLASS_NAME, ("login__form_action_container"))

    # Make sure the boxes are empty first
    email.clear()
    password.clear()

    # Enter your email and password on the first and second line of Authentication.txt file
    # Index = 0 for your email and Index = 1 for your password
    authenticate = open("Authentication.txt")
    credential = authenticate.readlines()
    myemail = credential[0]
    mypassword = credential[1]

    # Enter on both sections
    email.send_keys(myemail)
    password.send_keys(mypassword)
    sleep(1)
    # Sometimes, LinkedIn lauches a security verification, so make sure
    # you login first and hit enter afterwards
    print("___...___")
    input("Hit 'Enter' if you're on your Homepage : ")

