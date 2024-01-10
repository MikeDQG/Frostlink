import requester

# if testing doesn't work, try this in terminal: $env:PYTHONPATH="src/"

class Retriever():
    def __init__(self):
        self.req = requester.Requester()
        self.alarms = None
        self.values = None

    def get_values(self):
        '''getPointValue'''
        self.values = self.req.get_point_value()
        if self.values == None:
            self.req = requester.Requester()
            self.values = self.req.get_point_value()
        #self.req.logout()

    def confirm_alarms():
        '''confirm alarms'''
        alarm_requester = requester.Requester()
        try:
            alarm_requester.confirm_alarms()
        except:
            print("except")
        alarm_requester.logout()
