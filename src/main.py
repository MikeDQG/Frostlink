
import logging
import reporter
import time


class Main():
    def __init__(self):
        log_string = str(time.time()) + '_final_main.log'
        logging.basicConfig(filename=log_string, filemode='w', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(module)s %(levelname)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
        logging.info("starting up")
        print("Press 'ctrl + C' to end")
        self.reporter = reporter.Reporter()
        logging.debug("Main initialized")
        try:
            self.run()
        except KeyboardInterrupt as KI:
            logging.error(KI)
            raise KeyboardInterrupt
        except Exception as e:
            logging.error(e)
        finally:
            self.reporter.retriever.end_session()

    def run(self):
        relative_time = 11
        t = time.time()
        STEPPER = 3
        TOTAL_TIME = time.time() + relative_time
        last_time = time.time()
        t = time.time()

        while True:
            if (t - last_time) > STEPPER:
                self._run()
                last_time = t
            t = time.time()
        
        
    def _run(self):
        try:
            self.reporter.main()
        except KeyboardInterrupt as KI:
            logging.exception(KI)
            raise KeyboardInterrupt

while True:
    try:
        m = Main()
    except KeyboardInterrupt as ki:
        break