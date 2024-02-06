import logging

class Listener():
    def __init__(self):
        self.confirm_alarms = None
        logging.debug("Listener initialized")

    def listen(self):
        print("Listener listen")