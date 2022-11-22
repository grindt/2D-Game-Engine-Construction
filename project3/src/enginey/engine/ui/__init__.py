### 
###  Entities 
### 

def make_hud(screenSize):
    import enginey.engine.ui.entity.hud as hd
    return hd.HUD(screenSize)

def make_basic_button(msg, screen,  bounds, color):
    import enginey.engine.ui.entity.basicButton as bscBtn
    return bscBtn.BasicButton(msg, screen, bounds, color)

### 
### Actions 
### 

def make_press_button():
    import enginey.engine.ui.action.press_button as prsBtn
    return prsBtn.ButtonPressed()

def make_draw_button():
    import enginey.engine.ui.action.draw_button as drwBtn
    return drwBtn.DrawRectButtonAction()

def make_draw_hud():
    import enginey.engine.ui.action.draw_hud as drwHd
    return drwHd.DrawHUDAction()