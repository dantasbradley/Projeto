# This is the hangman game
# Project started in May/30th/2020
#
import random
#str1 = input('Digite uma palavra: ')
frutas = ['apple', 'grape', 'papaya', 'strawberry', 'mango', 'blueberry', 'watermelon', 'lemon', 'orange', 'cherry']
# randint will generate a random number from 0 to 9
selection = frutas[random.randint(0,9)]
print('resultado : ', selection)
size = len(selection)
y = ""
for x in range(size):
    y+= "_ "
print(y)
print('\n\nIt has ',size,' letters')
amt=5
status = 0
print ("U start with 5 chances")
while status!=1:
    z= input('digite uma letra: ')
    if len(z)>1:
        print ("EU DISSE 1 LETRA!! Repete aí")
    if len(z)==1 :
        found = selection.find(z)
        if found == -1:
            amt= amt-1
            print((amt),'attempts remaining')
        if found == 0:
            y= y[1:]
            new = selection[0] +y
            y=new
            print(y)
        if found > 0:
            print("good job")
            print(selection.find(z))
            dub = found*2
            y = y[:dub] + selection[found] + y[dub + 1:]
            print(y)

    if len(z)==0:
        print("U ARE NOT FUN")
    if amt==0:
        print("WEAK")
        status =1

