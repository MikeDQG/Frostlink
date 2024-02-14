
import logging
import reporter
'''
import time
'''

class Main():
    def __init__(self):
        print(input("press any key to start ")) # stoopid test
        #logging.basicConfig(filename='./src/logs/example.log', filemode='w', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
        logging.basicConfig(filename='final_main_1.log', filemode='w', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(module)s %(levelname)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
        logging.info("starting up")
        self.reporter = reporter.Reporter()
        logging.debug("Main initialized")
        self.reporter.retriever.end_session()
        '''try:
            self.run()
        except KeyboardInterrupt as KI:
            logging.exception(KI)
            self.reporter.retriever.end_session()

    def run(self):      # timer logic
        relative_time = 30
        t = time.time()
        STEPPER = 3
        TOTAL_TIME = time.time() + relative_time
        last_time = time.time()
        t = time.time()
        #print(t, last_time, relative_time, STEPPER, TOTAL_TIME)

        while t < TOTAL_TIME:
            if (t - last_time) > STEPPER:
                self._run()
                last_time = t
            t = time.time()
        
        print(input("press any key to close")) # stoopid test #2


    def _run(self):     # run main program
        try:
            print("joke")
            logging.info("joke")
            self.reporter.main()
        except Exception as e:
            logging.exception(e)
            self.reporter.retriever.end_session()
'''

m = Main()