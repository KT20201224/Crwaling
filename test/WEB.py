from selenium import webdriver
import selenium
import time
import requests

## Input driver location
def make_page():
    ### chrome driver location
    location = "/home/kt/kt/chromedriver"

    ### default web url
    url = "https://www.google.com"

    page = webdriver.Chrome(location)
    page.get(url)

    return page


def new_google_tab(page):

    url = "https://wwww.google.com"
    page.execute_script('window.open(url);')

def search(page):
    
    ### keyword want to search
    key_word = "문경 날씨"

    inputElement = page.find_element_by_name("q")
    inputElement.send_keys(key_word)
    inputElement.submit()

## read table
def read_data(page):

    data = page.find_element_by_class_name("nawv0d")
    
    return data

def get_temp(page):
    data = read_data(page)
    temp = page.find_element_by_class_name("wob_t").text
    print("=======================================")
    print("temp : " + temp)
    print("=======================================")

    return temp

def get_rainy(page):
    data = read_data(page)
    rainy = page.find_element_by_id("wob_pp").text
    print("=======================================")
    print("rainy : " + rainy)
    print("=======================================")
    
    return rainy

def get_humidity(page):
    data = read_data(page)
    humidity = page.find_element_by_id("wob_hm").text
    print("=======================================")
    print("humidity : " + humidity)
    print("=======================================")

def get_wind(page):
    data = read_data(page)
    data2 = page.find_element_by_class_name("wob_hw")
    
    wind_dir = data2.find_element_by_tag_name("img")
    wind_dir = wind_dir.get_attribute("src")
    print("=======================================")
    print("wind_dir_url : " + wind_dir)
    print("=======================================")


def get_url(page):

    print("current URL : " + page.current_url)

    return page.current_url

def close_page(page):

    page.close()

def close_tab(page):

    page.quit()

def wait(page):
    time = 5 # seconds
    page.implicitly_wait(time_to_wait = time)

def run():

    page = make_page()
    ### keyword want to search
    search(page)
    get_temp(page)
    get_rainy(page)
    get_humidity(page)
    get_wind(page)
