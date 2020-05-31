import random
def part(errorNumber, shadow):
    if errorNumber == 6:
        print(' ________')
        print(' |      |')
        print(' |      -')
        print(' |      O')
        print(' |     /|\\')
        print(' |     / \\       <-- Error(6)')
        print(' |')
        print('___________________   => FRUIT with ',len(shadow), 'letters: ', end='')
    elif errorNumber == 5:
        print(' ________')
        print(' |      |')
        print(' |      -')
        print(' |      O')
        print(' |     /|\\')
        print(' |     /        <-- Error(5)')
        print(' |')
        print('___________________   => FRUIT with ',len(shadow), 'letters: ', end='')
    elif errorNumber == 4:
        print(' ________')
        print(' |      |')
        print(' |      -')
        print(' |      O')
        print(' |     /|\\       <-- Error(4)')
        print(' |')
        print(' |')
        print('___________________   => FRUIT with ',len(shadow), 'letters: ', end='')
    elif errorNumber == 3:
        print(' ________')
        print(' |      |')
        print(' |      -')
        print(' |      O')
        print(' |     /|       <-- Error(3)')
        print(' |')
        print(' |')
        print('___________________   => FRUIT with ',len(shadow), 'letters: ', end='')
    elif errorNumber == 2:
        print(' ________')
        print(' |      |')
        print(' |      -')
        print(' |      O')
        print(' |      |       <-- Error(2)')
        print(' |')
        print(' |')
        print('___________________   => FRUIT with ',len(shadow), 'letters: ', end='')
    elif errorNumber == 1:
        print(' ________')
        print(' |      |')
        print(' |      -')
        print(' |      O       <-- Error(1)')
        print(' |      ')
        print(' |')
        print(' |')
        print('___________________   => FRUIT with ',len(shadow), 'letters: ', end='')
    else:
        print(' ________')
        print(' |      |')
        print(' |      -')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print('___________________   => FRUIT with ',len(shadow), 'letters: ', end='')
    print(shadow)

def createShadow(size):
    shadow = ''
    for x in range(size):
        shadow += '*'
    return shadow

def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")
    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring
    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]
#MAIN
frutas = ['apple', 'grape', 'papaya', 'strawberry', 'mango', 'blueberry', 'watermelon', 'lemon', 'orange', 'cherry']
# randint will generate a random number from 0 to 9
selection = frutas[random.randint(0,9)]
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
            selectionShadow = replacer(selectionShadow, guess[0], index)
            position = index +1
        print('GREAT JOB !!!')
    else:
        error += 1
        if error < 6:
            print('WRONG GUESS, TRY AGAIN')
        else:
            print('GAME OVER, YOU LOST!!!')
    if selectionShadow.find('*') == -1:
        gameOver = True
        print('CONGRATULATIONS YOU WON!!!!')
        print('The right answer is: ', selectionShadow)
    else:
        part(error, selectionShadow)
