from pygame import mixer

class SoundAction():
    def __init__(self):
        self.types = ["draw"]
        self.entity_state = None
        self.verbose = False
        self.name = "play_sound_action"
        return

    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self, *args):
        if self.condition_to_act():
            self.playSound()
        if self.verbose:
            print(self.name + " for " + self.entity_state.name)
        return

    def playSound(self):
        
        mixer.init()
        mixer.music.load(self.entity_state.file)
        mixer.music.set_volume(self.entity_state.volume)
        mixer.music.play()

        return