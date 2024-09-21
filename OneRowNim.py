import time
import random
"""
Nadeem Elsayed
Game is called one row nim
This program plays this game smartly

Game Rules:
there are around 21 sticks in a cup
there are two players who take turns taking out one, two, or three sticks
the last person to take a stick out loses

"""
#variable declarations
nsticks = 21
player = 1 #first player

#gets a number from 1-3 on sticks to be removed
def get_input():
    #do while loop
    ready = False
    while not ready:
        try:
            print("There are", nsticks, "sticks remaining")
            userChoice = int(input("Enter a proper number of matchsticks from 1 to 3: "))
            if userChoice >= 1 and userChoice <=3 and userChoice<=nsticks:
                ready = True
            else:
                print("Out of Range")
        except ValueError:
            print("not an integer")
    return userChoice

def tk_sticks(rmv_sticks):
    global nsticks
    nsticks = nsticks - rmv_sticks

#player is either one or two, this alternates
def switch_player():
    global player
    player = 3-player

def ai_magic():
    global nsticks
    #we want to leave the opponent with a number of sticks such that n%4 == 1
    if nsticks == 1:
        rmv_sticks = 1 #loss :(
    elif nsticks %4 == 2:
        rmv_sticks = 1
    elif nsticks %4 == 3:
        rmv_sticks = 2
    elif nsticks %4 == 0:
        rmv_sticks = 3
    else: #opponent should win, value doesn't matter
        rmv_sticks = random.randint(0,3)+1
    tk_sticks(rmv_sticks)
    print("The AI took", rmv_sticks, "sticks")

aiplayer = random.randint(0,1)+1 #could go first or second
print("Welcome to One Row Nim")
# time.sleep(1)
print("You and the program take turns removing sticks from a cup")
# time.sleep(1)
print("The last person to remove a stick from a cup is the loser")
# time.sleep(1)

while (nsticks>0):
    if player == aiplayer:
        ai_magic()
        switch_player()
    else:
        userChoice = get_input()
        tk_sticks(userChoice)
        switch_player()

#send results
if player == aiplayer:
    print("The AI won and you lost")
else:
    print("You won and the AI Player lost")