import db_object

class Writer():
    def __init__(self):
        self.db_object = db_object.DB_Object()
        print("Writer init")

    def write(self):
        self.db_object.to_list()
        print("Writer write ", self.db_object.list)

        self.db_object.list = []