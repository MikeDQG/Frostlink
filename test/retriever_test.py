import retriever
import requester

# if testing doesn't work, try this in terminal: $env:PYTHONPATH="src/"

def test0():
    r1 = retriever.Retriever()
    try:
        r1.get_values()
    except Exception as exec:
        print(exec)
    
    finally:
        r1.end_session()


test0()
