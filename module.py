import database
from database import database
import module
from setting import user
import os


    

def set_user():

    name = input("what is your name : ")
    user = user(name)
    
    os.system('clear')


if __name__ == '__main__':
    
    set_user()

    print(user.name)

    mydb = database()
    mydb.get_ifdb()