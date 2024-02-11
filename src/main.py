import reporter
import logging
import time


class Main():
    def __init__(self):
        #logging.basicConfig(filename='./src/logs/example.log', filemode='w', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
        logging.basicConfig(filename='final_test_1.log', filemode='w', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(module)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
        self.reporter = reporter.Reporter()
        logging.debug("Main initialized")
        #print(input("press any key to start ")) # stoopid test
        try:
            self.run()
        except KeyboardInterrupt as KI:
            logging.exception(KI)
            self.reporter.retriever.end_session()

    def run(self):      # timer logic
        relative_time = 300
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


    def _run(self):     # run main program
        try:
            #print("joke")
            self.reporter.main()
        except Exception as e:
            logging.exception(e)


m = Main()