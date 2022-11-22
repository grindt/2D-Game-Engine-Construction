### 
###  Entities 
### 
 
def make_success_counter(msg):
    import enginey.engine.utility.entity.successCounter as sCnt
    return sCnt.SuccessCounter(msg)

def make_total_counter(msg):
    import enginey.engine.utility.entity.totalCounter as tCnt
    return tCnt.TotalCounter(msg)

def make_timer():
    import enginey.engine.utility.entity.timer as tim
    return tim.Timer()

### 
### Actions 
### 

def make_activate():
    import enginey.engine.utility.action.activate as act
    return act.Activate()

def make_alarm(allotedTime):
    import enginey.engine.utility.action.alarm as alrm
    return alrm.Alarm(allotedTime)

def make_deactivate():
    import enginey.engine.utility.action.deactivate as dAct
    return dAct.Deactivate()

def make_increment():
    import enginey.engine.utility.action.increment as inc
    return inc.Increment()

def make_start():
    import enginey.engine.utility.action.start as strt
    return strt.Start()

def make_update():
    import enginey.engine.utility.action.update as upd
    return upd.Update()