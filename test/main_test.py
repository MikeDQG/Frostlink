import main

def test0():
    m1 = main.Main()
    
    i = ''
    while i != 'e':
        try:
            m1.main()
        except Exception as exec:
            print(exec)

        i = input("next command (refresh - r, exit - e): ")
    
    m1.reporter.retriever.end_session()


test0()