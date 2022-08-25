##
##  @author KKT
##  @date 2022-08-03
##

from influxdb import InfluxDBClient
from datetime import datetime, timedelta
import time
import requests

class database:
    
    def __init__(self, db='myDB', host='localhost', port=8086, user='root', passwd='root'):
        # Create an object include information for connect to the influxDB
        self.client = InfluxDBClient(host, port, user, passwd, db)
    
        try:
            # Try to Create database
            self.client.create_database(db)

            # If you can create databasse or have a database
            # there is no problem connecting to the ifnluxDB
            print('Connection Successful')
            print('===========================')
            print('      connection info')
            print('===========================')
            print('host : ', host)
            print('port : ', port)
            print('username : ', user)
            print('database : ', db)
    
        except:
            # Generate error if you can't create database (can't connect to ifdb)
            print('Connection Failed')
            pass


