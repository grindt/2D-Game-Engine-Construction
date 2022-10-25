import datetime

class Timer():
    def __init__(self, name="timer"):
        self.actions = []
        self.name = name
        self.startTime = None
        self.currentTime = None
        self.template = None
        self.verbose = False
        self.active = False

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a) 
        return a

    def tick(self):
        self.currentTime = datetime.datetime.now()
        return

    def elapsed_time(self):
        if self.active:
            return self.currentTime - self.startTime
        return 0