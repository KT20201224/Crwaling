##
##  @ author : KKT
##  @ data : 2022-08-10
## 


import selenium
from selenium import webdriver


class crawl:

    def __init__(self):
        
        driver = webdriver.Chrome("/home/kt/kt/chromedriver")
        driver.get("https://www.google.com")
        print("Chrome driver start! ready to search")

        page = null

        return

    def search(self, key_word):
    
        inputElement = driver.find_element_by_name("q")
        inputElement.send_keys(key_word)
        inputElement.submit()

        self.page = driver.find_element_by_class_name("srp")

        if(not page):
            print("Error : Page not parsed")
        else:
            print("Success : page parsed")

        return

    def read_temp(page):

        temp = page.find_element_by_class_name("wob_t").text
        return temp

    def read_rainPro(page):

        rainPro = page.find_element_by_id("wob_pp").text
        return rainPro

    def read_hum(page):

        hum = page.find_element_by_id("wob_hm").text
        return hum

    def read_wind(page):

        wind = page.find_element_by_id("wob_ws").text
        return wind

    def read_location(page):

        location = page.find_element_by_class_name("wob_loc").text
        return location

    def read_time(page):

        time = page.find_element_by_class_name("wob_dts").text
        return time

    def read_png(page):

        png = page.find_element_by_class_name("wob_tci").get_attribute("src")
        return png
    
    def get_screen_shot(self, page):

        page.screenshot("screenshot")
        return

    