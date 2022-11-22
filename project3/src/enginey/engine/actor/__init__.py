### 
###  Entities 
### 
 
def make_basic_rectangle(bounds, color):
    import enginey.engine.actor.entity.rectangle as shp
    return shp.Rectangle(bounds, color)

def make_basic_circle(radius, color, location):
    import enginey.engine.actor.entity.circle as shp
    return shp.Circle(radius, color, location)

def make_basic_letter(fontSize, letter, color, location):
    import enginey.engine.actor.entity.letter as shp
    return shp.Letter(fontSize, letter, color, location)
 
### 
### Actions 
### 

def make_draw_rectangle_action():
    import enginey.engine.actor.action.drawRectangle as drShp
    return drShp.DrawRectangleAction()

def make_draw_circle_action():
    import enginey.engine.actor.action.drawCircle as drShp
    return drShp.DrawCircleAction()

def make_draw_letter_action():
    import enginey.engine.actor.action.drawLetter as drShp
    return drShp.DrawLetterAction()

def make_letter_handler(word):
    import enginey.engine.actor.action.letterHandler as drShp
    return drShp.LetterHandler(word)