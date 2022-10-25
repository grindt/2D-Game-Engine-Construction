### 
###  Entities 
### 

def make_sound(file, volume=0.0):
    import enginey.engine.sound.entity.sound as snd
    return snd.Sound(file, volume)

### 
### Actions 
### 

def make_sound_action():
    import enginey.engine.sound.action.sound_action as snd
    return snd.SoundAction()