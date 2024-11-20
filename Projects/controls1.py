# Section 1: Setup
import codesters
from codesters import StageClass
stage = StageClass()

stage.set_background("court")
s1 = codesters.Sprite("person1",0,-200)
s1.set_size(0.5)

s2 = codesters.Sprite("toilet",0,200)
s2.set_size(0.5)

# Section 2: define controls
def move_up(sprite):
    sprite.move_up(1)

def move_down(sprite):
    sprite.move_down(1)

def move_left(sprite):
    sprite.move_left(1)

def move_right(sprite):    
    sprite.move_right(1)

# Section 3: define hide and show
def hide(sprite):
    sprite.hide()

# Section 4: bind controls to specific keys
s1.event_key("w", move_up)
s1.event_key("s", move_down)
s1.event_key("a", move_left)
s1.event_key("d", move_right)

# Section 5: reminder message
print("Game has started. Open the screen using PORTS to play")

def move_up(sprite2):
    sprite2.move_up(1)

def move_down(sprite2):
    sprite2.move_down(1)

def move_left(sprite2):
    sprite2.move_left(1)

def move_right(sprite2):    
    sprite2.move_right(1)

s2.event_key("up", move_up)
s2.event_key("down", move_down)
s2.event_key("left", move_left)
s2.event_key("right", move_right)

def hide(sprite2):
    sprite2.hide()
s2.event_key("m", hide)
def show(sprite2):
    sprite2.show()
s2.event_key("n", show)



def reset(sprite2):
    sprite2.goto(0,200)
s2.event_key("r", reset)

def reset(sprite):
    sprite.goto(0,-200)
s1.event_key("r", reset)






























