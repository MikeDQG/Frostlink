import logging
import sec_log_test as sec_log_test

logging.basicConfig(filename='example.log', filemode='w', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(module)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

sec_log_test.do_smth()

'''
pyinstaller .\logger_test.py --onefile --noconsole

'''