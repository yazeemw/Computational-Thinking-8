smileyface_points = 0
clownface_points = 0
sadface_points = 0

answer1 = input("When you're in class what is your usual mood? A happy and talkative B playful and loud or C alone and moody   ")
if answer1 == "A" or answer1 == "a":
    smileyface_points += 1
elif answer1 == "B" or answer1 == "b":
    clownface_points += 1
elif answer1 == "C" or answer1 == "c":
    sadface_points += 1
answer2 = input("Do you react to new people A outgoing B jokey C quiet    ")
if answer2 == "A":
    smileyface_points += 1
elif answer2 == "B":
    clownface_points += 1
elif answer2 == "C":
    sadface_points += 1

answer3 = input("Would you rather A go to a party B hang out with friends or C stay home alone   ")
if answer3 == "A":
    smileyface_points += 1
elif answer3 == "B":
    clownface_points += 1
elif answer3 == "C":
    sadface_points += 1

answer4 = input("How do you usually text? A all caps B lowercase and uppercase with random emojis C short mellow answers, late responses    ")
if answer4 == "A":
    smileyface_points += 1
elif answer4 == "B":
    clownface_points += 1
elif answer4 == "C":
    sadface_points += 1

answer5 = input("If plans get canceled how do you feel? A optimistic and flexible B jokingly dramatic C sad and dissapointed      ")
if answer5 == "A":
    smileyface_points += 1
elif answer5 == "B":
    clownface_points += 1
elif answer5 == "C":
    sadface_points += 1

if smileyface_points > clownface_points and smileyface_points > sadface_points: print (f" Your score is {smileyface_points} 😁, this means you are a very happy and an outgoing person")
if clownface_points > smileyface_points and clownface_points > sadface_points: print (f" Your score is {clownface_points} 🤡, this means you are a very silly and humorous person")
if sadface_points > clownface_points and sadface_points > smileyface_points: print (f" Your score is {sadface_points} 😔, this means you are a very moody person and down in the dumps")