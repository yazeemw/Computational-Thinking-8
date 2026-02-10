import turtle, time, random
from utils import *

#keep the dog alive for as long as possible by feeding him and keeping him happy and warm!
set_background("park")
t1 = create_sprite("puppy",-300,-200)

happiness = 50
hunger = 50
temp = 75
age = 0


def give_food():
    global hunger
    hunger += 1
    x = random.randint (-200, 200)
    y = random.randint (-200, 200)
    c1 = create_sprite ("cookie",x,y)
    time.sleep (0.2)
    c1.hideturtle()

def increase_age():
    global age
    age+= 1

def throw_ball ():
    global happiness
    happiness += 1 
    x = random.randint (-200, 200)
    y = random.randint (-200, 200)
    t2 = create_sprite ("tennis_ball",x,y)
    time.sleep(0.2)
    t2.hideturtle()

def give_blanket ():
    global temp
    temp += 1 
    x = random.randint (-200, 200)
    y = random.randint (-200, 200)
    b1 = create_sprite ("blanket",x,y)
    time.sleep(0.2)
    b1.hideturtle()

window.onkeypress (give_food, "f")
#"f" spawns a cookie sprite on the screen and increases the hunger variable by 1
window.onkeypress (throw_ball, "t")
#"t" spawns a tennis ball sprite on the screen and increases the happiness variable by 1
window.onkeypress (give_blanket, "b")
#"b" spawns a blanket sprite on the screen and increases the temperature variable by 1

window.listen() 

message1 = create_sprite("alien",-200,160)
message1.color("black")
message1.hideturtle()

for i in range(1000000000):
    message1.clear()
    message1.write(f"hunger: {hunger}\nhappiness: {happiness}\ntemp: {temp}\nage {age}", font=("arial", 20, "normal"))
    

    time.sleep(0.01)
    if i % 150 == 0:
        temp -= 1
    if i % 100 == 0:
        hunger -= 1
    if i % 500 == 0:
        age += 1
    if i % 90 == 0:
        happiness -= 1

    if hunger == 0:
        break
    if happiness == 0:
        break
    if age == 100:
        break
    elif temp == 100:
        break

    window.update()
print("game over")