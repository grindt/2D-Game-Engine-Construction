class Letter():
    def __init__(self, fontSize, letter, color=(255,255,255), location=(0,0)):
        self.actions = []
        self.fontSize = fontSize
        self.letter = letter
        self.location = location
        self.color = color
        self.active = True
        self.children = []
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a) 
        return a
