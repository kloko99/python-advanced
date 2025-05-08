"""
Datenbank Verbdindung Beispiel
"""
class DB:
    def connect(self):
        self.__establish_connection()  # __ verhindert, dass establish_connection von Control aufgerufen wird
    
    def __establish_connection(self):
        print("Connect to DB")


class Control(DB):
    def __init__(self):
        self.establish_connection()

    def establish_connection(self):
        print("Connect to Controller")


db = Control()
db.connect()  # connect do DB aufgerufen wird?