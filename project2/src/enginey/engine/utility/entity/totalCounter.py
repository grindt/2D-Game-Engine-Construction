class TotalCounter():
    def __init__(self, msg, name="TotalCounter"):
        self.actions = []
        self.name = name
        self.counter = 0
        self.message = msg
        self.template = None
        self.verbose = False
        self.active = True

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a) 
        return a