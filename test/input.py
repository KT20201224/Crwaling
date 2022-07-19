##########################################
##                                      ##
##  Crwaling temperature data           ##
##                                      ##
##  Implemented by kyoungtae kim        ##
##                                      ##
##  2022-06-29                          ##
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

###########################################

## 현재 네이버 날씨 기준으로 데이터 가져옴

def get_table():

    ## Input url 
    html = requests.get('https://weather.naver.com/today/04280101?cpName=KMA')
    data = BeautifulSoup(html.text, 'html.parser')
    
    # Error1
    if(data == None):
        print("Error1 : html data None")
        return

    section = data.findAll('div',{'class':'chart_area'})
    # Error2
    if(section == None):
        print("Error2 : secion data None")
        return
    print(section)
   
    # temp = ""
    # for i in temp_all:
    #     temp = temp + " " + i.text

    # print(temp)

def read_file():

    table = pd.read_csv('_data_.csv',encoding='UTF-8')
    
    return table
 

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

    data = read_file()

    region = data['지점명']
    time = data['일시']
    temp = data['기온(°C)']
    precipitation = data['강수량(mm)']
    wind_speed = data['풍속(m/s)']
    wind_dir = data['풍향(16방위)']
    humidity = data['습도(%)']

    region = region.tolist()
    time = time.tolist()
    temp = temp.tolist()
    precipitation = precipitation.tolist()
    wind_speed = wind_speed.tolist()
    wind_dir = wind_dir.tolist()
    humidity = humidity.tolist()

    json_body=[]
    tablename='mytable'
    fieldname='myfield'
    point={
        "measurement":tablename,
        "tags":{
            "Region":None
        },
        "fields":{
            "temperature":None,
            # "precipitation":None,
            "wind speed":None,
            "wind_dir":None,
            "humidity":None
        },
        "time":None,
    }

    
    i = 0
    while i<144:
        np=deepcopy(point)
        dt=datetime(2022,6,23,1,0,0) + timedelta(hours=i)
        np['fields']['temperature'] =  temp[i]
        # if(precipitation[i]!=None):
        #     np['fields']['precipitataion'] =  precipitation[i]
        np['fields']['wind_speed'] =  wind_speed[i]
        np['fields']['wind_dir'] =  wind_dir[i]
        np['fields']['humidity'] =  humidity[i]
        np['tags']['region'] =  region[i]
        np['time']=dt
        json_body.append(np) 
        i=i+1

    # for i in humidity:
    #     # InfluxDB is based on UTC
    #     # so it should be timed with KCT
    #     dt=datetime.now()-timedelta(hours=9)

    #     np=deepcopy(point)
    #     np['fields']['humidity']=i
    #     np['time']=dt
    #     json_body.append(np)


    # Write the data for 10 seconds on the influxDB at once
    ifdb.write_points(json_body)

    result=ifdb.query('select*from %s' %tablename)
    pprint(result.raw)

def do_test():
    # Connect to InfluxDB
    mydb = get_ifdb(db='myDB')

    # write data to mydb
    my_test(mydb)

if __name__ == '__main__':
    do_test()