class Rectangle():
    def __init__(self, bounds=(0,0,0,0), color=(128, 128, 128), name="rectangle"):
        self.actions = []
        self.bounds = bounds
        self.color = color
        self.name = name
        self.template = None
        self.verbose = False
        self.active = True
        self.children = []
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a) 
        return a

