class GravityForce:
    def __init__(self, name="gravity_force"):
        self.gravity = [0.0, -1.0]
        self.actions = []
        self.name = name
        self.active = True
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return

class SpringForce:
    def __init__(self, name="spring_force"):
        self.spring_constant = 1.0
        self.actions = []
        self.name = name
        self.active = True
        return
        
    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return

class DragForce:
    def __init__(self, name="drag_force"):
        self.drag_constant = 0.1
        self.actions = []
        self.name = name
        self.active = True
        return
        
    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return