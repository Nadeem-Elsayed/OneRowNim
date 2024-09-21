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
player = 1 #player can be one or two

def main():
    while (nsticks>0):
        return

main()
#gets a number from 1-3 on sticks to be removed
def getInput():
    sticks = None
    #check for int, check in range, check that you're not taking more sticks than in cup
    while (not isinstance(sticks, int) and sticks > 1 and sticks < 3 and sticks > nsticks):
        sticks = input("How many sticks do you want to take out? (1-3) Enter a proper Integer: ")
    return sticks

#player is either one or two, this alternates
def switchPlayer():
    global player
    player = 3-player

def takeSticks(removed):
    global nsticks
    nsticks = nsticks - removed