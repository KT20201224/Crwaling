##########################################
##                                      ##
##  Connect InfluxDB                    ##
##                                      ##
##  Implemented by Kyoungtae Kim        ##
##                                      ##
##  Last Update : 2022-07-05            ##
##                                      ##
##########################################

import influxdb import InfluxDBClient

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