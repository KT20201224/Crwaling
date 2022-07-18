from selenium import webdriver
import selenium
import time

## Input driver location
def google():

    location = "/home/kt/kt/chromedriver"
    url = "https://www.google.com"

    global page = webdriver.Chrome(location)
    page.get(url)


def new_google_tab():

    url = "https://wwww.google.com"
    page.execute_script('window.open(url);')

def search():

    key_word = "문경 날씨"

    inputElement = page.find_element_by_name("q")
    inputElement.sendkeys(key_word)
    inputElement.submit()

def getMKdata():

    data = page.find_element_by_class_name("nawv0d")
    data = data.text

    return data

def get_url():

    print("current URL : " + page.current_url)

    return page.current_url

def close_page():

    page.close()

def close_tab():

    page.quit()

def wait():
    time = 5 # seconds
    page.implicitly_wait(time_to_wait = time)
