import random

def part(errorNumber, shadow):
    if errorNumber == 6:
        print(' =========')
        print(' ||      !')
        print(' ||      -')
        print(' ||      O')
        print(' ||     /|\\')
        print(' ||     / \\       <-- 6 Mistakes ')
        print(' ||')
        print('___________________   => FRUIT with ',len(shadow), 'letters: ', end='')
    elif errorNumber == 5:
        print(' =========')
        print(' ||      !')
        print(' ||      -')
        print(' ||      O')
        print(' ||     /|\\')
        print(' ||     /        <-- 5 Mistakes ')
        print(' ||')
        print('___________________   => FRUIT with ',len(shadow), 'letters: ', end='')
    elif errorNumber == 4:
        print(' =========')
        print(' ||      !')
        print(' ||      -')
        print(' ||      O')
        print(' ||     /|\\       <-- 4 Mistakes ')
        print(' ||')
        print(' ||')
        print('___________________   => FRUIT with ',len(shadow), 'letters: ', end='')
    elif errorNumber == 3:
        print(' =========')
        print(' ||      !')
        print(' ||      -')
        print(' ||      O')
        print(' ||     /|       <-- 3 Mistakes ')
        print(' ||')
        print(' ||')
        print('___________________   => FRUIT with ',len(shadow), 'letters: ', end='')
    elif errorNumber == 2:
        print(' =========')
        print(' ||      !')
        print(' ||      -')
        print(' ||      O')
        print(' ||      |       <-- 2 Mistakes ')
        print(' ||')
        print(' ||')
        print('___________________   => FRUIT with ',len(shadow), 'letters: ', end='')
    elif errorNumber == 1:
        print(' =========')
        print(' ||      !')
        print(' ||      -')
        print(' ||      O       <-- 1 Mistake ')
        print(' ||      ')
        print(' ||')
        print(' ||')
        print('___________________   => FRUIT with ',len(shadow), 'letters: ', end='')
    else:
        print(' =========')
        print(' ||      !')
        print(' ||      -')
        print(' ||')
        print(' ||')
        print(' ||')
        print(' ||')
        print('___________________   => FRUIT with ',len(shadow), 'letters: ', end='')
    print('\033[32m'+shadow+'\033[37m')
def happy():
    print('           \           --- ---          /')
    print('            \        / /    \  \       /')
    print('             \      |  O    O  |      /')
    print('              \     |    ..    |     /')
    print('               \     \ \----/ /     /')
    print('                \      - -- -      /\n\n')

def sad():
    print('                    /   - -- -    \ ')
    print('                   /  / __  __ \   \  ')
    print('                  /  |  o    o  |   \  ')
    print('                 /   |    ..    |    \ ')
    print('                /     \  .--.  /      \\')
    print('               /        - -- -         \\\n\n')

def line():
    print('\n\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n\n')

def positive():
    line()
    happy()
    print('                    GREAT JOB !!!')
    line()

def negative():
    line()
    sad()
    print('                WRONG GUESS, TRY AGAIN')
    line()

def createShadow(size):
    shadow = ''
    for x in range(size):
        shadow += '*'
    return shadow

#MAIN
frutas = ['apple', 'grape', 'papaya', 'strawberry', 'mango', 'blueberry', 'watermelon', 'lemon', 'orange', 'cherry',
          'avocado', 'carambola', 'coconut', 'guava', 'jackfruit', 'pineapple', 'pomegranate', 'tangerine', 'pitanga', 'cranberrie']
# randint will generate a random number from 0 to 9
selection = frutas[random.randint(0,19)]
size = len(selection)
selectionShadow = createShadow(size)
error = 0
part(error, selectionShadow)
gameOver = False
while error < 6 and gameOver == False:
    guess = input('\nGuess a letter: ').split()
    count = selection.count(guess[0])
    position = 0
    if count > 0:
        for x in range(count):
            index = selection.find(guess[0], position)
            selectionShadow = selectionShadow[:index] + guess[0].upper() + selectionShadow[index + 1:]
            position = index + 1
        positive()
    else:
        error += 1
        if error < 6:
           negative()
        else:
            negative()
            print('               GAME OVER, YOU LOST!!!')
            print('          The right answer is: ', selection.upper())
    if selectionShadow.find('*') == -1:
        gameOver = True
        print('          CONGRATULATIONS YOU WON!!!!')
        print('          The right answer is: ', selectionShadow)
    else:
        part(error, selectionShadow)