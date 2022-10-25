class HUD():
    def __init__(self, screen, name="HUD"):
        self.actions = []
        self.name = name
        self.screen = screen
        self.template = None
        self.verbose = False
        self.active = True
        self.children = []

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a) 
        return a
    
    def insert_child(self, e):
        e.parent = self
        self.children.append(e)
        return e