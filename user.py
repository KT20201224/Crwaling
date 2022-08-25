class user():

    def __init__(self):
        self.usr_name = 'user'
        self.region = 'korea'

    def change_usr_name(self, name):
        self.usr_name = name
        

    def change_region(self, region):
        self.region = region

    def print_usr_name(self):
        print(self.usr_name)

    def print_region(self):
        print(self.region)