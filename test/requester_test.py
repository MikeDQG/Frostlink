import requester

# if testing doesn't work, try this in terminal: $env:PYTHONPATH="src/"

def test0():
    '''get data from the table'''
    r1 = requester.Requester()
    r1.monitoring()
    r1.navigate()
    r1.monitoring()
    r1.navigate2()
    r1.monitoring()
    r1.get_temps()
    r1.logout()

def test1():
    '''getPointValue'''
    r2 = requester.Requester()
    r2.get_point_value()
    r2.logout()

def test2():
    '''confirm alarms'''
    r3 = requester.Requester()
    try:
        r3.confirm_alarms()
    except:
        print("except")
    r3.logout()

def test3():
    '''getPointValue'''
    r2 = requester.Requester()
    print(r2.get_alarms())
    r2.logout()

test3()