class SuccessCounter():
    def __init__(self, msg, name="SuccessCounter"):
        self.actions = []
        self.name = name
        self.counter = 0
        self.message = msg
        self.template = None
        self.verbose = False
        self.active = True
        self.children = []

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a) 
        return a