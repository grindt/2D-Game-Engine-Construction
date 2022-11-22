class PickPositionAction:
    def __init__(self, index):
        self.types = ["position"]
        self.particle_index = index
        self.entity_state = None
        self.name = "pick_position_action"
        self.children = []

    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if self.particle_index >= len(self.entity_state.position):
            return False
        if self.entity_state.active_particle[self.particle_index] == False:
            return False
        return True

    def act(self):
        if self.condition_to_act():
            new_data = list(self.entity_state.position[self.particle_index])
            for c in self.children:
                c.act(new_data)
        return

class PutPositionAction:
    def __init__(self, index):
        self.types = ["position"]
        self.particle_index = index
        self.entity_state = None
        self.name = "put_position_action"
        self.children = []

    def condition_to_act(self, data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if len(data) != 2:
            return False
        return True

    def act(self, data):
        if self.condition_to_act(data):
            self.entity_state.location = tuple(data)
            for c in self.children:
                c.act(data)
        return