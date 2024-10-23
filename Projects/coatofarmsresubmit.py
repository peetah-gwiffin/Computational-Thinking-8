###############################################
### SETUP ###
import codesters
from codesters import StageClass

stage = StageClass()
stage.set_background("court")

# Create squares
s1 = codesters.Square(100, 100, 200, 'white')
s2 = codesters.Square(-100, 100, 200, 'black')
s3 = codesters.Square(-100, -100, 200, 'white')
s4 = codesters.Square(100, -100, 200, 'black')

# Set the size of the squares
s1.set_size(0.5)
s2.set_size(0.5)
s3.set_size(0.5)
s4.set_size(0.5)

# Create and position text
text1 = codesters.Text("pete Kicska", x=0, y=150)
text2 = codesters.Text("Witawy", x=0, y=-150)

# Create sprites
