import logging
import time

log_string = str(time.time()) + '_final_main.log'
logging.basicConfig(filename=log_string, filemode='w', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(module)s %(levelname)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
logging.info("starting up")

print(input("press any key to start ")) # stoopid test