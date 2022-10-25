class FrameViewey():
    def __init__(self, screen, children = []):
        self.screen = screen
        self.actions = []
        self.name = "frame_viewey"
        self.verbose = False
        self.active = True
        self.children = children
        return

    def insert_action(self, action):
        action.entity_state = self
        self.actions.append(action)
        return

    
    
