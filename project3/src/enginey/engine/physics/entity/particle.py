class Particle:
    def __init__(self, name="particle"):
        self.position = []
        self.velocity = []
        self.acceleration = []
        self.mass = []
        self.active_particle = []
        self.sactive_particle = []
        self.actions = []
        self.children = []
        self.name = name
        self.active = True
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return
    
    def add_particle(self, p, v, m):
        self.position.append(p)
        self.velocity.append(v)
        self.acceleration.append([0.0,0.0])
        self.mass.append(m)
        self.active_particle.append(True)
        self.sactive_particle.append(True)