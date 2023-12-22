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
    '''press button'''
    r3 = requester.Requester()
    r3    