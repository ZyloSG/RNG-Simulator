import random
import os

os.system("title RNG Simulator 1.0")
os.system("color 4")

# random functions
def RandomNumber(min_value: int, max_value: int):
    generatednumber = random.randint(min_value, max_value)
    return generatednumber

# base
def levelbase(currentleveldef, currentlevel: str, minvalue: int, maxvalue: int, nextlevel):
    os.system("cls")
    needednumber = RandomNumber(minvalue, maxvalue)
    print("Welcome to level " + currentlevel + "!")
    print("Your numbers will be ranging from " + minvalue.__str__() + " to " + maxvalue.__str__())
    print("The needed number is: " + needednumber.__str__())
    rngnumber = input("Press any key to generate your random number")
    rngnumber = RandomNumber(minvalue, maxvalue)
    if (rngnumber != needednumber):
        print("Better luck next time! Your Number: " + rngnumber.__str__())
        input("Press enter to try again")
        currentleveldef()
    elif (rngnumber == needednumber):
        print("Wow! you did it! Your Number: " + rngnumber.__str__())
        input("Press enter to go to next level")
        nextlevel()

# levels
def level1():
    levelbase(level1, "1", 1, 10, level2)

def level2():
    levelbase(level2, "2", 1, 30, level3)

def level3():
    levelbase(level3, "3", 1, 50, level4)

def level4():
    levelbase(level4, "4", 1, 70, level5)

def level5():
    levelbase(level5, "5", 1, 100, endscreen)

def endscreen():
    os.system("cls")
    print("""Game over! You completed all levels, congratulations!
          Made by Zylo (github.com/ZyloSG)""")


# entry point
if __name__ == "__main__":
    level1()