import turtle, math, time, random
from utils import *

# Section 1: Setup
# TODO - create your player character and any other sprites
set_background("park.gif")
s1 = create_sprite("dog.gif")


# TODO - set the starting value for your variables
sprite_list = []
food = 10

#The goal of the game is to keep the dog alive and eating the cookie. Every few loops, the amount of food decreases so it must keep catching cookies to not die.

# Section 2: Controls
# TODO - define your controls
def move_left():
    x = s1.xcor() - 30
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s1.xcor() + 30
    y = s1.ycor() 
    s1.goto(x,y)

def move_up(): 
    x = s1.xcor() 
    y = s1.ycor() + 10
    s1.goto(x,y)

def move_down(): 
    x = s1.xcor() 
    y = s1.ycor() - 10
    s1.goto(x,y)

# TODO - pick keys for each control
window.onkeypress(move_right, "Right")
window.onkeypress(move_left, "Left")
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
# Section 3: Game Loop



window.listen()
message1 = create_sprite("alien",-200,160)
message1.color("black")
message1.hideturtle()

    
for i in range(10000000000):
    
    message1.clear()
    message1.write(f"food: {food}", font=("arial", 20, "normal"))
    
    if i % 80 == 0:
        x = random.randint(-300,300)
        s2 = create_sprite("cookie.gif", x, 400)
        s2.setheading(270)
        sprite_list.append(s2)

    for s2 in sprite_list:
        s2.forward(5)

    for s2 in sprite_list:
        if get_distance(s1, s2) < 80:
            food += 2
            s2.hideturtle()
            sprite_list.remove(s2)

    if i % 110 == 0:
        food -= 1
    
    if food <= 0:
        s1.write("You starved the dog!!!")
        break

    time.sleep(0.01)
    window.update()


    

	
print("Game Over")