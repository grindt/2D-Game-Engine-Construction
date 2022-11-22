class positionSolveAction:
    def __init__(self):
        self.types = ["physics"]
        self.entity_state = None
        self.dt = 1.0
        self.name = "position_solve_action"
        self.children = []
    
    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self):
        if self.condition_to_act():
            for i in range(0,len(self.entity_state.position)):
                if self.entity_state.active_particle[i]:
                    self.entity_state.position[i][0] = self.entity_state.position[i][0] + self.dt * self.entity_state.velocity[i][0]
                    self.entity_state.position[i][1] = self.entity_state.position[i][1] + self.dt * self.entity_state.velocity[i][1]
            for c in self.children:
                c.act(self.entity_state)
        return

class velocitySolveAction:
    def __init__(self):
        self.types = ["physics"]
        self.entity_state = None
        self.dt = 1.0
        self.name = "velocity_solve_action"
        self.children = []
    
    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self):
        if self.condition_to_act():
            for i in range(0,len(self.entity_state.acceleration)):
                if self.entity_state.active_particle[i]:
                    self.entity_state.acceleration[i][0] = 0.0
                    self.entity_state.acceleration[i][1] = 0.0
            
            for c in self.children:
                c.act(self.entity_state)

            for i in range(0,len(self.entity_state.velocity)):
                if self.entity_state.active_particle[i]:
                    self.entity_state.velocity[i][0] = self.entity_state.velocity[i][0] + self.dt * self.entity_state.acceleration[i][0]
                    self.entity_state.velocity[i][1] = self.entity_state.velocity[i][1] + self.dt * self.entity_state.acceleration[i][1]
        return

class EulerSolveAction:
    def __init__(self):
        self.types = ["physics"]
        self.entity_state = None
        self.dt = 1.0
        self.name = "euler_solve_action"
        self.children = []
    
    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if len(self.children) < 2:
            return False
        return True

    def act(self):
        if self.condition_to_act():
            self.children[0].dt = float(self.dt)
            self.children[1].dt = float(self.dt)
            self.children[0].act()
            self.children[1].act()

            for c in self.children[2:]:
                c.act()
        return

class LeapFrogSolveAction:
    def __init__(self):
        self.types = ["physics"]
        self.entity_state = None
        self.dt = 1.0
        self.name = "leap_frog_solve_action"
        self.children = []
    
    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if len(self.children) < 2:
            return False
        return True

    def act(self):
        if self.condition_to_act():
            self.children[0].dt = self.dt*0.5
            self.children[1].dt = self.dt
            self.children[0].act()
            self.children[1].act()
            self.children[0].act()

            for c in self.children[2:]:
                c.act()
        return