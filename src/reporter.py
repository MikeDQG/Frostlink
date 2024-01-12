import retriever
import db_object
import writer
import listener

class Reporter():

    def __init__(self):
        self.retriever = retriever.Retriever()
        self.db_object = db_object.DB_Object()
        self.writer = writer.Writer()
        self.listener = listener.Listener()
    
    def main(self):
        self.update()
        self.write()
        self.listen()
    
    def update(self):
        # get active alarms count and report it
        # retrieve data and write it
        self.retriever.get_values()
        self.db_object = self.retriever.db_send_object

    def write(self):
        self.writer.db_object = self.db_object
        self.writer.write()
    
    def listen(self):
        self.listener.listen()
        if self.listener.change != None:
            print("Incomplete code: Reporter: 31")
            """ torej tukaj moramo resetirat alarme """
            self.retriever.confirm_alarms()