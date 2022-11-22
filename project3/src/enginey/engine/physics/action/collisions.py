class InsideRectangleCollisionAction:
    def __init__(self):
        self.types = ["physics"]
        self.entity_state = None
        self.name = "inside_rectangle_action"
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
            for i in range(0,len(data.position)):
                if data.active_particle[i]:
                    if data.position[i][0] < self.entity_state.ulc[0]:
                        data.position[i][0] = 2.0*self.entity_state.ulc[0] - data.position[i][0]
                        data.velocity[i][0] = -data.velocity[i][0]
                    elif data.position[i][0] > self.entity_state.lrc[0]:
                        data.position[i][0] = 2.0*self.entity_state.lrc[0] - data.position[i][0]
                        data.velocity[i][0] = -data.velocity[i][0]
                    elif data.position[i][1] < self.entity_state.ulc[1]:
                        data.position[i][1] = 2.0*self.entity_state.ulc[1] - data.position[i][1]
                        data.velocity[i][1] = -data.velocity[i][1]
                    elif data.position[i][1] > self.entity_state.lrc[1]:
                        data.position[i][1] = 2.0*self.entity_state.lrc[1] - data.position[i][1]
                        data.velocity[i][1] = -data.velocity[i][1]
            for c in self.children:
                c.act(data)
        return

class OutsideRectangleCollisionAction:
    def __init__(self):
        self.types = ["physics"]
        self.entity_state = None
        self.name = "outside_rectangle_action"
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
            for i in range(0,len(data.position)):
                if data.active_particle[i]:
                    if data.position[i][0] > self.entity_state.ulc[0] and data.position[i][0] < self.entity_state.lrc[0]:
                        if data.position[i][1] > self.entity_state.ulc[1] and data.position[i][1] < self.entity_state.lrc[1]:
                            right_time = (data.position[i][0] - self.entity_state.ulc[0]) / data.velocity[i][0]
                            if right_time < 0.0:
                                right_time = 100000000.0
                            left_time = (data.position[i][0] - self.entity_state.lrc[0]) / data.velocity[i][0]
                            if left_time < 0.0:
                                left_time = 100000000.0
                            top_time = (data.position[i][1] - self.entity_state.ulc[1]) / data.velocity[i][1]
                            if top_time < 0.0:
                                top_time = 100000000.0
                            bottom_time = (data.position[i][1] - self.entity_state.lrc[1]) / data.velocity[i][1]
                            if bottom_time < 0.0:
                                bottom_time = 100000000.0
                            minimum_time = min(right_time, left_time, top_time, bottom_time)
                            if right_time == minimum_time:
                                data.position[i][0] = 2.0*self.entity_state.ulc[0] - data.position[i][0]
                                data.velocity[i][0] = -data.velocity[i][0]
                            if left_time == minimum_time:
                                data.position[i][0] = 2.0*self.entity_state.lrc[0] - data.position[i][0]
                                data.velocity[i][0] = -data.velocity[i][0]
                            if top_time == minimum_time:
                                data.position[i][1] = 2.0*self.entity_state.ulc[1] - data.position[i][1]
                                data.velocity[i][1] = -data.velocity[i][1]
                            if bottom_time == minimum_time:
                                data.position[i][1] = 2.0*self.entity_state.lrc[1] - data.position[i][1]
                                data.velocity[i][1] = -data.velocity[i][1]
            for c in self.children:
                c.act(data)

        return

class Flip1RectangleCollisionAction:
    def __init__(self):
        self.types = ["physics"]
        self.entity_state = None
        self.name = "flip_rectangle_action"
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
            for i in range(0,len(data.position)):
                if data.position[i][0] > self.entity_state.ulc[0] and data.position[i][0] < self.entity_state.lrc[0]:
                    if data.position[i][1] > self.entity_state.ulc[1] and data.position[i][1] < self.entity_state.lrc[1]:
                        right_time = (data.position[i][0] - self.entity_state.ulc[0]) / data.velocity[i][0]
                        if right_time < 0.0:
                            right_time = 100000000.0
                        left_time = (data.position[i][0] - self.entity_state.lrc[0]) / data.velocity[i][0]
                        if left_time < 0.0:
                            left_time = 100000000.0
                        top_time = (data.position[i][1] - self.entity_state.ulc[1]) / data.velocity[i][1]
                        if top_time < 0.0:
                            top_time = 100000000.0
                        bottom_time = (data.position[i][1] - self.entity_state.lrc[1]) / data.velocity[i][1]
                        if bottom_time < 0.0:
                            bottom_time = 100000000.0
                        minimum_time = min(right_time, left_time, top_time, bottom_time)
                        if right_time == minimum_time \
                        or left_time == minimum_time \
                        or top_time == minimum_time \
                        or bottom_time == minimum_time:
                            data.sactive_particle[i] = False
            for c in self.children:
                c.act(data)
        return

class Flip2RectangleCollisionAction:
    def __init__(self):
        self.types = ["physics"]
        self.entity_state = None
        self.name = "flip_rectangle_action"
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
            for i in range(0,len(data.position)):
                if data.position[i][0] > self.entity_state.ulc[0] and data.position[i][0] < self.entity_state.lrc[0]:
                    if data.position[i][1] > self.entity_state.ulc[1] and data.position[i][1] < self.entity_state.lrc[1]:
                        right_time = (data.position[i][0] - self.entity_state.ulc[0]) / data.velocity[i][0]
                        if right_time < 0.0:
                            right_time = 100000000.0
                        left_time = (data.position[i][0] - self.entity_state.lrc[0]) / data.velocity[i][0]
                        if left_time < 0.0:
                            left_time = 100000000.0
                        top_time = (data.position[i][1] - self.entity_state.ulc[1]) / data.velocity[i][1]
                        if top_time < 0.0:
                            top_time = 100000000.0
                        bottom_time = (data.position[i][1] - self.entity_state.lrc[1]) / data.velocity[i][1]
                        if bottom_time < 0.0:
                            bottom_time = 100000000.0
                        minimum_time = min(right_time, left_time, top_time, bottom_time)
                        if right_time == minimum_time \
                        or left_time == minimum_time \
                        or top_time == minimum_time \
                        or bottom_time == minimum_time:
                            data.sactive_particle[i] = True
            for c in self.children:
                c.act(data)
        return