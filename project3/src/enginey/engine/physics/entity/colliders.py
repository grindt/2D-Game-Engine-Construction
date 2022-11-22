class RectangleCollider:
    def __init__(self, ulc = [0.0,0.0], lrc = [100.0,100.0], name="rectangle_collider"):
        self.ulc = ulc
        self.lrc = lrc
        self.actions = []
        self.name = name
        self.active = True
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return