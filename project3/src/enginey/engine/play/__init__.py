### 
###  Entities 
### 
 
def make_game_loop(game_content):
    import enginey.engine.play.entity.gameLoopey as gl
    return gl.GameLoopey(game_content)

def make_frame_viewer(screen):
    import enginey.engine.play.entity.frameViewey as fv
    return fv.FrameViewey(screen)
 
### 
### Actions 
### 

def make_screen_display_action():
    import enginey.engine.play.action.frameVieweyAction as fv
    return fv.FrameVieweyAction()

def make_terminate():
    import enginey.engine.play.action.terminate as term
    return term.Terminate()
