# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()


player = codesters.Sprite("sodacan")
player.set_size(0.4)
player.go_to(0,-200)
stage.disable_floor()


gameOver = False
lives = 3


# Section 2 - Objects


def falling_object():
    global gameOver
    if not gameOver:
        x_position = random.randint(-250,250)
        object = codesters.Sprite("soccerball", x_position, 250)
        object.set_size(0.4)
        object.set_y_speed(-12)
   
stage.event_interval(falling_object, 0.8)


# Section 3 - Collision


def collision(s1, s2):
    global lives, gameOver
   
    if s2.get_image_name() == "soccerball":
        stage.remove_sprite(s2)
        if lives == 0:
            player.say("game over lil bro")
            gameOver = True
        else:
            lives -= 1
            
             
player.event_collision(collision)

def move_left(player):
    player.move_left(2)

def move_right(player):    
    player.move_right(2)

player.event_key("a", move_left)
player.event_key("d", move_right)


    




# Section 4 - Controls 

