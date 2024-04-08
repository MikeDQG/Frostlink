
import logging
import reporter
import retriever
import writer
import requester
import time
import listener

listenerInstance = listener.Listener()
writerInstance = writer.Writer()
requesterInstance = requester.Requester()
retrieverInstance = retriever.Retriever(requesterInstance=requesterInstance)
reporterInstance = reporter.Reporter(retrieverInstance=retrieverInstance, writerInstance=writerInstance, listenerInstance=listenerInstance)

def init():
    log_string = str(time.time()) + '_deep_fix.log' #'_final_main.log'
    logging.basicConfig(filename=log_string, filemode='w', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(module)s %(levelname)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
    logging.info("starting up")
    print("Press 'ctrl + C' to end")
    logging.debug("Main initialized")
    try:
        run()
    except KeyboardInterrupt as KI:
        logging.error(KI)
        raise KeyboardInterrupt
    except Exception as e:
        logging.error(e)
    finally:
        retrieverInstance.end_session()


def run():
    relative_time = 11                  # popravi to, brez tega v koncni verziji
    t = time.time()
    STEPPER = 3
    TOTAL_TIME = time.time() + relative_time
    last_time = time.time()
    t = time.time()

    while True:
        if (t - last_time) > STEPPER:
            reporterInstance.main()
            last_time = t
        t = time.time()
    

init()
run()