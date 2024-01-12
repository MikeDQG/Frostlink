

class DB_Object():
    def __init__(self):
        self.handshake = 0
        self.message = None
        self.change_message = 0
        self.capacity = 0.0
        self.temp1 = 0.0
        self.temp2 = 0.0
        self.temp3 = 0.0
        self.temp4 = 0.0
        self.active_alarm_count = 0
        self.alarm_name = None
        self.list = []
    
    def to_list(self):
        self.list.append(self.message)
        self.list.append(self.capacity)
        self.list.append(self.temp1)
        self.list.append(self.temp2)
        self.list.append(self.temp3)
        self.list.append(self.temp4)
        self.list.append(self.active_alarm_count)
        self.list.append(self.alarm_name)