import reporter
import retriever
import requester

# if testing doesn't work, try this in terminal: $env:PYTHONPATH="src/"

def test0():
    rep1 = reporter.Reporter()
    try:
        rep1.main()
        rep1.main()
        rep1.main()
        rep1.main()
        rep1.main()
        rep1.main()
        rep1.main()
        rep1.main()
    except Exception as exec:
        print(exec)
    
    finally:
        rep1.retriever.end_session()


test0()