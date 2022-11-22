class BasicButton():
    def __init__(self, msg, screen, bounds=(0,0,0,0), color=(128, 128, 128), name="button"):
        self.actions = []
        self.bounds = bounds
        self.color = color
        self.name = name
        self.message = msg
        self.screen = screen
        self.template = None
        self.verbose = False
        self.active = True
        self.children = []
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a) 
        return a

    def insert_children(self, c):
        c.parent = self
        self.children.append(c)
        return c

    def is_inside(self, pos):
        if pos[0] < self.bounds[0]:
            return False
        if pos[0] > self.bounds[2] + self.bounds[0]:
            return False
        if pos[1] < self.bounds[1]:
            return False
        if pos[1] > self.bounds[3] + self.bounds[1]:
            return False
        return True