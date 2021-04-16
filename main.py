# Setup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time



PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.youlikehits.com/")

username = ""
password = ""
print(driver.title)


search = driver.find_element_by_link_text("Login")
search = driver.find_element_by_partial_link_text('Logi')
search.send_keys(Keys.RETURN)

time.sleep(5)

# login
print("Login in")
search = driver.find_element_by_id("username")
search.send_keys(username)
search = driver.find_element_by_id("password")
search.send_keys(password)

search = driver.find_element_by_xpath('//*[@id="bodybg"]/table[2]/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[2]/td/center/form/table/tbody/tr[3]/td/span/input').click()

pointsMade = 0





rtweet = 0
tweet = 0
tweetLikes = 0


time.sleep(5)

# points botting
start = True
while(start):
    # Going to start of page
    # driver.get("https://www.youlikehits.com/")
    driver.back()
    driver.back()
    time.sleep(2)
    print("So far where there rtweet: ", rtweet, " atempts made")
    print("So far where there tweet: ", tweet, " atempts made")
    print("So far where there tweet Likes: ", tweetLikes, " atempts made")
    print("Starting script! ")





    # RTweets
    try:
        # clicking on Earn points
        search = driver.find_element_by_xpath('//*[@id="primary_nav_wrap"]/ul/li[2]/a').click()

        time.sleep(5)

        # clicking on Twitter Retweets
        search = driver.find_element_by_xpath('//*[@id="diggdiv"]/div/img').click()
        time.sleep(3)
        # Rtweets
        print("Trying")
        driver.get("https://www.youlikehits.com/retweets.php")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src^='retweetrender.php']")))
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Confirm"))).click()
        print("Making points Click from rtweets")
        rtweet = rtweet + 1
        time.sleep(10)
    except NoSuchAttributeException:
        print("Element not found!")
        continue
    except:
        print("Something is wrong with Rtweets!")



    # Tweets
    try:
        print("Trying to just tweet instand")
        # Going back to start of page
        driver.get("https://www.youlikehits.com/")
        time.sleep(2)

        # clicking on Earn points
        search = driver.find_element_by_xpath('//*[@id="primary_nav_wrap"]/ul/li[2]/a').click()


        # Tweeting
        search = driver.find_elements_by_class_name("freeDrawer-item-content")
        search = driver.find_element_by_xpath('/html/body/div/table[2]/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[2]/td/center/div[2]/div/img').click()
        time.sleep(5)
        driver.get("https://www.youlikehits.com/tweets.php")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src^='tweetrender.php']")))
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Confirm"))).click()
        print("Making points Click from tweeting")
        tweet = tweet + 1
        time.sleep(10)
    except:
        print("Something is wrong with Tweets!")





    # Tweet Likes
    try:
        print("Trying to just tweet Likes instand")
        # Going back to start of page
        driver.get("https://www.youlikehits.com/")
        time.sleep(2)

        # clicking on Earn points
        search = driver.find_element_by_xpath('//*[@id="primary_nav_wrap"]/ul/li[2]/a').click()

        # Tweet Likes
        search = driver.find_elements_by_class_name("socialicon")
        search = driver.find_element_by_xpath('/html/body/div/table[2]/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[2]/td/center/div[3]/div/img').click()
        time.sleep(5)
        driver.get("https://www.youlikehits.com/favtweets.php")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src^='favtweetrender.php']")))
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Confirm"))).click()
        print("Making points Click from tweet Likes")
        tweetLikes = tweetLikes + 1
        time.sleep(10)
    except:
        print("Something is wrong with Tweets!")

# driver.quit()
