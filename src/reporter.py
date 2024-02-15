import retriever
import writer
import listener
import logging

class Reporter():

    def __init__(self):
        self.retriever = retriever.Retriever()
        self.writer = writer.Writer()
        self.listener = listener.Listener()
        logging.debug("Reporter initialized")
    
    def main(self):
        #self.update()
        self.write(self.update())
        #self.listen()
    
    def update(self):
        # get active alarms count and report it
        # retrieve data and write it
        logging.info("updating")
        return self.retriever.get_values()
        #print('values retrieved')

    def write(self, write_tuple):
        logging.info("writing")
        self.writer.write(write_tuple)
    
    def listen(self):
        self.listener.listen()
        if self.listener.confirm_alarms != None:
            print("Incomplete code: Reporter: 31")
            """ torej tukaj moramo resetirat alarme """
            self.retriever.confirm_alarms()