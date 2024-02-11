import main
import logging
import time
 
seconds = time.time()
t = time.time()


def test0():
    print(input("press any key to start ")) # stoopid test
    logging.basicConfig(filename='final_test_1.log', filemode='w', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(module)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
    
    logging.info("App started")
    #m1 = main.Main()
    
    try:
        #m1.run()
        print("Smth")
    except Exception as exec:
        print(exec)
            
    #m1.reporter.retriever.end_session()
    
    print(input("press any key to close")) # stoopid test #2

#test0()

relative_time = 300
t = time.time()
STEPPER = 3
TOTAL_TIME = time.time() + relative_time
last_time = time.time()
t = time.time()
print(t, last_time, relative_time, STEPPER, TOTAL_TIME)

while t < TOTAL_TIME:
    if (t - last_time) > STEPPER:
        test0()
        last_time = t
    t = time.time()