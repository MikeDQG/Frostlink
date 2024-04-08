import retriever
import writer
import listener
import logging

class Reporter():

    def __init__(self, retrieverInstance, writerInstance, listenerInstance):
        self.retrieverInstance = retrieverInstance
        self.writerInstance = writerInstance
        self.listenerInstance = listenerInstance
        logging.debug("Reporter initialized")
    
    def main(self):
        self.write(self.update())
        #self.listen()
    
    def update(self):
        logging.info("updating")
        return self.retrieverInstance.get_values()

    def write(self, write_tuple):
        logging.info("writing")
        self.writerInstance.write(write_tuple)
    
    def listen(self):
        self.listenerInstance.listen()
        if self.listenerInstance.confirm_alarms != None:
            print("Incomplete code: Reporter: 31")
            """ torej tukaj moramo resetirat alarme """
            self.retrieverInstance.confirm_alarms()