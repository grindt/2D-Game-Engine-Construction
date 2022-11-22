class Sound():
    def __init__(self, file, volume=0.0):
        self.actions = []
        self.verbose = False
        self.name = "play_sound"
        self.template = None
        self.active = True
        self.file = file
        self.volume = volume
        self.children = []
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a) 
        return a