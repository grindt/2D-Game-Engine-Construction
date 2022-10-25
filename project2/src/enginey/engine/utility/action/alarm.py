class Alarm():
    def __init__(self, allotedTime):
        self.types = ["event"]
        self.entity_state = None
        self.verbose = False
        self.name = "alarm"
        self.allotedTime = allotedTime
        self.children = []
        return

    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == True:
            return False
        if self.entity_state.elapsed_time() < self.allotedTime:
            return False
        return True

    def act(self):
        if self.condition_to_act():
            for child in self.children:
                child.act()
        if self.verbose:
            print(self.name + " for " + self.entity_state.name)
        self.entity_state.actions.remove(self)
        return