class HUD():
    def __init__(self, screenSize, name="HUD"):
        self.actions = []
        self.name = name
        self.screenSize = screenSize
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