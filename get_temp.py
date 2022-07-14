#######################################
##
##  Crwaling temperature data
##  
##  Implemented by kyoungtae kim
##  
##  2022-06-29
##
#######################################

from datetime import datetime, timedelta
import time
from influxdb import InfluxDBClient
from copy import deepcopy
from bs4 import BeautifulSoup
from pprint import pprint
import requests
import numpy as np

def get_temp():
    ## url for crwaling data
    # 웹페이지 요청을 하는 코드이다. 특정 url을 적으면 웹피이지에 대한 소스코드들을 볼 수 있다.
    html = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%AC%B8%EA%B2%BD%EC%8B%9C+%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hrYBndp0YihsscP%2Fy%2FhssssstxZ-461001')

    ## parsing data
    # 파이썬에서 보기 좋게, 다루기 쉽게 파싱작업을 거쳐야 각 요소에 접근이 쉬워진다.
    # 이것을 도와주는게 beautifulsoup4 모듈이다.
    data = BeautifulSoup(html.text, 'html.parser')

    ## cut data
    # 데이터를 위에 날씨 부분만 자름
    section = data.find('div', {'class':'weather_graph_box'})

    find_temp = section.findAll('span',{'class':'num'})

    for i in find_temp:
        temp = i.text
    
########################################################################################################################


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

def my_test(ifdb):
    # save points in the json_body
    json_body=[]
    tablename='mytable'
    fieldname='myfield'
    point={
        "measurement":tablename,
        "tags":{
            "country":"South Korea",
            "Region":"Munkyoung"
        },
        "fields":{
            # initailize data to zero
            "temp":0
        },
        "time":None,
    }

    ########################################################
    ## url for crwaling data
    # 웹페이지 요청을 하는 코드이다. 특정 url을 적으면 웹피이지에 대한 소스코드들을 볼 수 있다.
    html = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%AC%B8%EA%B2%BD%EC%8B%9C+%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hrYBndp0YihsscP%2Fy%2FhssssstxZ-461001')

    ## parsing data
    # 파이썬에서 보기 좋게, 다루기 쉽게 파싱작업을 거쳐야 각 요소에 접근이 쉬워진다.
    # 이것을 도와주는게 beautifulsoup4 모듈이다.
    data = BeautifulSoup(html.text, 'html.parser')
    
    ## cut data
    # 데이터를 위에 날씨 부분만 자름
    section = data.find('div', {'class':'weather_graph_box'})

    find_temp = section.findAll('span',{'class':'num'})
    print(find_temp)
    temp =""

    for i in find_temp:
        temp = temp + " " +(i.text)[:2]
    
    temp = temp.split()

    print(type(temp))

   
    

    # temp = find_temp.text
    # temp = temp.split('\n')
    # print(temp)
    count = 1

    ########################################################
    for i in temp:
        # InfluxDB is based on UTC
        # so it should be timed with KCT
        dt=datetime(2022, 6, 28, 10, 10, 10) + timedelta(hours=count)

        count = count+1
        np=deepcopy(point)
        np['fields']['temp']=i
        np['time']=dt 
        json_body.append(np)

        # wait a second

    # Write the data for 10 seconds on the influxDB at once
    ifdb.write_points(json_body)

    result=ifdb.query('select*from %s' %tablename)
    #pprint(result.raw)

def do_test():

    # Connect to InfluxDB
    mydb = get_ifdb(db='myDB')

    # write data to mydb
    my_test(mydb)

if __name__ == '__main__':
    do_test()
