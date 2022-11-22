class GravityForceAction:
    def __init__(self):
        self.types = ["physics"]
        self.entity_state = None
        self.name = "gravity_force_action"
        self.children = []
    
    def condition_to_act(self, data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if data == None:
            return False
        return True

    def act(self, data):
        if self.condition_to_act(data):
            for i in range(0,len(data.acceleration)):
                data.acceleration[i][0] = data.acceleration[i][0] + self.entity_state.gravity[0]
                data.acceleration[i][1] = data.acceleration[i][1] + self.entity_state.gravity[1]
        for c in self.children:
            c.act(data)
        return

class SpringForceAction:
    def __init__(self):
        self.types = ["physics"]
        self.entity_state = None
        self.name = "spring_force_action"
        self.children = []
    
    def condition_to_act(self, data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if data == None:
            return False
        return True

    def act(self, data):
        if self.condition_to_act(data):
            total_mass = 0.0
            center_of_mass = [0.0, 0.0]
            for i in range(0,len(data.acceleration)):
                if data.active_particle[i] and data.sactive_particle[i]:
                    total_mass = total_mass + data.mass[i]
                    center_of_mass[0] = center_of_mass[0] + data.mass[i] * data.position[i][0]
                    center_of_mass[1] = center_of_mass[1] + data.mass[i] * data.position[i][1]
            center_of_mass[0] = center_of_mass[0]/total_mass
            center_of_mass[1] = center_of_mass[1]/total_mass

            for i in range(0,len(data.acceleration)):
                if data.active_particle[i] and data.sactive_particle[i]:
                    accel = [0.0, 0.0]
                    accel[0] = (center_of_mass[0] - data.position[i][0]) * self.entity_state.spring_constant / data.mass[i]
                    accel[1] = (center_of_mass[1] - data.position[i][1]) * self.entity_state.spring_constant / data.mass[i]

                    data.acceleration[i][0] = data.acceleration[i][0] + accel[0]
                    data.acceleration[i][1] = data.acceleration[i][1] + accel[1]
        for c in self.children:
            c.act(data)
        return

class DragForceAction:
    def __init__(self):
        self.types = ["physics"]
        self.entity_state = None
        self.name = "drag_force_action"
        self.children = []
    
    def condition_to_act(self, data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if data == None:
            return False
        return True

    def act(self, data):
        if self.condition_to_act(data):
            for i in range(0,len(data.acceleration)):
                if data.active_particle[i]:
                    data.acceleration[i][0] = data.acceleration[i][0] - data.velocity[i][0] * self.entity_state.drag_constant
                    data.acceleration[i][1] = data.acceleration[i][1] - data.velocity[i][1] * self.entity_state.drag_constant
        for c in self.children:
            c.act(data)

        return