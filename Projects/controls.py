# Section 1: Setup
import codesters
from codesters import StageClass
stage = StageClass()

stage.set_background("moon")
s1 = codesters.Sprite("person1",0,-200)
s1.set_size(0.5)



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
s1.event_key("h", hide)

def show(sprite):
	sprite.show()
s1.event_key("g", show)

s1.event_key("a", move_left)
s1.event_key("d", move_right)


# Section 4: bind controls to specific keys
s1.event_key("w", move_up)
s1.event_key("s", move_down)


# Section 5: reminder message
print("Game has started. Open the screen using PORTS to play")



def turn_left(sprite):
	heading = sprite.heading
	sprite.set_heading(heading + 1)
s1.event_key("e", turn_right)

def turn_right(sprite):
	heading = sprite.heading
	sprite.set_heading(heading - 1)
s1.event_key("q", turn_left)
def forward(sprite):
	sprite.forward(1)
