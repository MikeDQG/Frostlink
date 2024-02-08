import main
import logging

def test0():
    logging.basicConfig(filename='example.log', filemode='w', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(module)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
    print(input())
    logging.info("App started")
    m1 = main.Main()
    
    i = ''
    while i != 'e':
        try:
            m1.run()
        except Exception as exec:
            print(exec)

        i = input("next command (refresh - r, exit - e): ")
    
    m1.reporter.retriever.end_session()


test0()