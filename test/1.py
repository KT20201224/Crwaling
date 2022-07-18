##########################################
##                                      ##
##  Data Crwaling                       ##
##                                      ##
##  Implemented by Kyoungtae Kim        ##
##                                      ##
##  Last Update : 2022-07-05            ##
##                                      ##
##########################################

from datetime import datetime, timedelta
import time
from influxdb import InfluxDBClient
from copy import deepcopy
from bs4 import BeautifulSoup
from pprint import pprint
import requests
import pandas as pd
import schedule
from selenium import webdriver
import selenium

###########################################
##  get Database
###########################################
def get_ifdb(db, host='localhost', port=8086, user='root', passwd='root'):
    # Create an object include information for connect to the influxDB
    client = InfluxDBClient(host, port, user, passwd, db)

    try:
        # Try to Create database
        client.create_database(db)

        # If you can create databasse or have a database
        # there is no problem connecting to the ifnluxDB
        print('Connection Successful')
        print('===========================')
        print('    connection info')
        print('===========================')
        print('host : ', host)
        print('port : ', port)
        print('username : ', user)
        print('database : ', db)
    
    except:
        # Generate error if you can't create database (can't connect to ifdb)
        print('Connection Failed')
        pass

    return client

def test_schedule():
    now = datetime.now()

###########################################
##  run every "time"
###########################################
def run(time):

    schedule.every(time).seconds.do(test_schedule)

    while True:
        schedule.run_pending()
        time.sleep(time)

###########################################
##  data mining
###########################################
def get_data():
    dr = webdriver.Chrome("/home/kt/kt/chromedriver")
    dr.get("https://www.google.com")
    #time.sleep(1)

    inputElement = dr.find_element_by_name("q")
    #time.sleep(1)

    inputElement.send_keys("문경 날씨")
    #time.sleep(1)

    inputElement.submit()
    #time.sleep(1)

    continue_link = dr.find_element_by_class_name("nawv0d")
    #time.sleep(1)
    
    preturn = continue_link.text
    print(preturn)
    dr.quit()

    return preturn

###########################################
##  data cleansing
###########################################
def cleansing_data():
    data = get_data()
    preturn = data.splitlines(True)
    
    return preturn[0:7]

###########################################
##  cut string auto
###########################################
def cut_str(str, cut):
    
    index = str.find('cut')
    print(type(str))
    # str = str[0:index]
    print(str[:-5])
        

###########################################
##  input data to db
###########################################
def input(ifdb):
    json_body=[]
    tablename='mytable'

    data = cleansing_data()

    print(data)
    temp = data[0]
    rain_pro = data[1]
    humid = data[2]
    wind = data[3]
    region = data[4]
    date = data[5]
    short = data[6]

#########################임시임시임시임시#############################
    temp = temp[0:-5]
    rain_pro = rain_pro[6:-2]
    humid = humid[4:-2]
    wind = wind[4:-4]
    region = region[0:-1]
    date = date[0:-1]
    short = short[0:-1]
#########################임시임시임시임시#############################
    print(temp)
    print(rain_pro)
    print(humid)
    print(wind)
    print(region)
    print(date)
    print(short)

    point={
        "measurement":tablename,
        "tags":{
            "Region":region,
            "Short":short
        },
        "fields":{
            # initailize data to zero
            "temp":int(temp),
            "rain_prob":int(rain_pro),
            "humid":int(humid),
            "wind":int(wind)
            "URL":https://ssl.gstatic.com/onebox/weather/64/partly_cloudy.png

        },
        "time":None,
    }

    # InfluxDB is based on UTC
    # so it should be timed with KCT
    dt=datetime.now()-timedelta(hours=9)

    np=deepcopy(point)
    np['time']=dt
    json_body.append(np)

    
    # # Write the data for 10 seconds on the influxDB at once
    ifdb.write_points(json_body)

    result=ifdb.query('select*from %s' %tablename)
    pprint(result.raw)


# def do_test():
#     # Connect to InfluxDB
#     # mydb = get_ifdb(db='myDB')
#     # print(type(mydb))
#     # test_schedule()

if __name__ == '__main__':
    # do_test()
    # run()
    # mydb = get_ifdb(db='myDB')

    # schedule.every(30).minutes.do(input,mydb)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    get_data()
    