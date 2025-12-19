# Section 1 - Your code
from utils import *
set_background("new_york")

s1 = create_sprite("pineapple", -100, -100)
s2 = create_sprite("puppy", -100, 100)
s2 = create_sprite("basketball", -100, -100)
s2 = create_sprite("kitten", 100, -100)

message1 = create_sprite("alien",-200,200)
message1.color("yellow")
message1.write("     NYC",font = ("Times New Roman", 40, "bold"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()