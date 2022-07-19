


from selenium import webdriver
import selenium

global dr

def close():
    global dr
    dr.quit()

def search():
    global dr
    dr = webdriver.Chrome("/home/kt/kt/chromedriver")
    dr.get("https://www.google.com")

    """ search 문경 날씨 """
    inputElement = dr.find_element_by_name("q")
    inputElement.send_keys("문경 날씨")
    inputElement.submit()

    table = dr.find_element_by_class_name("nawv0d")

    return table


def read_temp(table):
    temp = table.find_element_by_class_name("wob_t").text
    return temp

def read_rainPro(table):
    rainPro = table.find_element_by_id("wob_pp").text
    return rainPro

def read_hum(table):
    hum = table.find_element_by_id("wob_hm").text
    return hum

def read_wind(table):
    wind = table.find_element_by_id("wob_ws").text
    return wind

def read_location(table):
    location = table.find_element_by_class_name("wob_loc").text
    return location

def read_time(table):
    time = table.find_element_by_class_name("wob_dts").text
    return time

def read_png(table):
    png = table.find_element_by_class_name("wob_tci").get_attribute("src")
    return png