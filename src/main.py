import reporter
import logging


class Main():
    def __init__(self):
        #logging.basicConfig(filename='./src/logs/example.log', filemode='w', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
        #logging.basicConfig(filename='example.log', filemode='w', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
        logging.debug("Main initialized")
        self.reporter = reporter.Reporter()
        self.run()

    def run(self):
        self.reporter.main()

'''
m = Main()
m.run()'''