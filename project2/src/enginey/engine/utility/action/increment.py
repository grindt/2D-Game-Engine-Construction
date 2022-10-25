class Increment():
    def __init__(self):
        self.types = None
        self.entity_state = None
        self.verbose = False
        self.name = "increment"
        return

    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self, *args):
        if self.condition_to_act():
            self.entity_state.counter = self.entity_state.counter + 1
        if self.verbose:
            print(self.name + " for " + self.entity_state.name)
        return