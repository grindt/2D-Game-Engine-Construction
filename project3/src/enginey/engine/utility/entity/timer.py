import time

class Timer():
    def __init__(self, name="timer"):
        self.actions = []
        self.name = name
        self.startTime = 0
        self.currentTime = 0
        self.template = None
        self.verbose = False
        self.active = True
        self.children = []
        self.alarmChild = []

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a) 
        return a

    def tick(self):
        self.currentTime = round(time.time()*1000)
        return

    def elapsed_time(self):
        if self.active:
            return self.currentTime - self.startTime
        return 0

    def alarm_triggered(self):
        print("triggered")
        for c in self.alarmChild:
            c.active = True
        self.actions.pop(0)
