import random
def part6():
    print(' ________')
    print(' |      |')
    print(' |      -')
    print(' |      O')
    print(' |     /|\\')
    print(' |     / \\')
    print(' |')
    print('___________________')

def part5():
    print(' ________')
    print(' |      |')
    print(' |      -')
    print(' |      O')
    print(' |     /|\\')
    print(' |     / ')
    print(' |')
    print('___________________')

def part4():
    print(' ________')
    print(' |      |')
    print(' |      -')
    print(' |      O')
    print(' |     /|\\')
    print(' |')
    print(' |')
    print('___________________')

def part3():
    print(' ________')
    print(' |      |')
    print(' |      -')
    print(' |      O')
    print(' |     /|')
    print(' |')
    print(' |')
    print('___________________')

def part2():
    print(' ________')
    print(' |      |')
    print(' |      -')
    print(' |      O')
    print(' |      |')
    print(' |')
    print(' |')
    print('___________________')

def part1():
    print(' ________')
    print(' |      |')
    print(' |      -')
    print(' |      O')
    print(' |      ')
    print(' |')
    print(' |')
    print('___________________')

def part0():
    print(' ________')
    print(' |      |')
    print(' |      -')
    print(' |')
    print(' |')
    print(' |')
    print(' |')
    print('___________________   => FRUIT', end='')

#def checkGuess

frutas = ['apple', 'grape', 'papaya', 'strawberry', 'mango', 'blueberry', 'watermelon', 'lemon', 'orange', 'cherry']
# randint will generate a random number from 0 to 9
selection = frutas[random.randint(0,9)]
print('resultado : ', selection)
size = len(selection)
y = ""
for x in range(size):
    y += "_*_   "
part0()
print('(',size, 'letters ) ', end='')
print(y)
print("test")
Totalchances = 6
gameOver = False
userError = 0

#while (gameover != true  and usererror < 6 ):
 #   usertry = input('guess a letter: ')

