class Circle():
    def __init__(self, radius, color=(255, 255, 255), location=(0,0), name="circle"):
        self.actions = []
        self.radius = radius
        self.location = location
        self.color = color
        self.name = name
        self.template = None
        self.verbose = False
        self.active = True
        self.active_particle = []
        self.children = []

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a) 
        return a
