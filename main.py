import database

import module
from switch import switch
from user import user
from database import database
from crawl import crawl
import os


def clear():
    os.system('clear')

if __name__=='__main__':

    user = user()
    switch = switch()
    
    
    while(True):

        name = input('please Input your name : ')
        user.change_usr_name(name)

        region = input('region you want to search : ')
        user.change_region(region)
        clear()
    
        print('=================================')
        print('Hello ' + user.usr_name + "!!")
        print('you are finding ' + user.region + ' weather')
        print('=================================')
        
        while(True):
            check = input('Type ( y / n ) : ')

            if(check == "y" or check == 'yes' or check == 'Y' or check == 'Yes' or check == 'YES'):
                switch.on()
                break
            elif(check == 'n' or check == 'no' or check == 'N' or check == 'No' or check == 'NO'):
                switch.off()
                break

        if(switch.check()):
            clear()
            break    

    db = database()
    clear()
    
    cr = crawl()
    cr.search()
