import WEB
import influx_db
import time
import schedule
import os
import web_crwaling
from datetime import datetime, timedelta
import time
from copy import deepcopy
from pprint import pprint

def run():
    mydb = influx_db.get_ifdb(db='kt')

    schedule.every(1).hours.do(input_db,mydb)

    while True:
        schedule.run_pending()
        time.sleep(1)
    

def input_db(mydb):
    page = web_crwaling.search()

    temp = web_crwaling.read_temp(page)
    rain_pro = web_crwaling.read_rainPro(page)[:-1]
    hum = web_crwaling.read_hum(page)[:-1]
    wind = web_crwaling.read_wind(page)[:-3]
    location = web_crwaling.read_location(page)
    date = web_crwaling.read_time(page)
    png = web_crwaling.read_png(page)

    print()
    print('===========================')
    print('           data')
    print('===========================')
    print("temp : ", temp, "°C")
    print("rainPro : ", rain_pro, "%")
    print("hum : ", hum, "%")
    print("wind : ", wind, "m/s")
    print("location : ", location)
    print("time : ", date)
    print("png : ", png)
    print('===========================')

    json_body=[]
    tablename="weather"

    point={
        "measurement":tablename,
        "tags":{
            "location":location,
            "crwal_time":date
        },
        "fields":{
            "temp":int(temp),
            "rain_prob":int(rain_pro),
            "humid":int(hum),
            "wind":int(wind),
            "URL":png

        },
        "time":None,
    }

    dt=datetime.now()-timedelta(hours=9)

    np=deepcopy(point)
    np['time']=dt
    json_body.append(np)

    mydb.write_points(json_body)

    print()
    print('===========================')
    print("   data input success!!")
    print('===========================')

    web_crwaling.close()



if __name__ == '__main__':
    
    run()

