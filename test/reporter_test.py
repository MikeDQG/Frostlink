import reporter
import retriever
import requester

# if testing doesn't work, try this in terminal: $env:PYTHONPATH="src/"

def test0():
    rep1 = reporter.Reporter()
    
    i = ''
    while i != 'e':
        try:
            rep1.main()
        except Exception as exec:
            print(exec)

        i = input("next command (refresh - r, exit - e): ")
    
    rep1.retriever.end_session()


test0()