class HUD():
    def __init__(self, screen, name="HUD"):
        self.actions = []
        self.name = name
        self.screen = screen
        self.template = None
        self.verbose = False
        self.active = True
        self.childEntities = []

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a) 
        return a
    
    def insert_child(self, e):
        e.parent = self
        self.childEntities.append(e)
        return e