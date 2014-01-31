$First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich

Bread = '2'
Jelly = '1'
PB = '4'

if Bread >=2 and Jelly >=1 and PB >= 4:
    print "PBJ Sandwich for lunch!"
else:
    print 'No sandwich for me'

#Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make

Bread = 2
Jelly = 1
PB = 4


if Bread == 2 and Jelly == 1 and PB ==4:
    print 'I can make exactly 2 sandwiches'
elif Bread >2 and Jelly >5 and PB >6:
    print 'Guess i\'ll just starve'
    
OR, using Raw_Input:

print "So how many sandwiches can you make"
total= raw_input()
print "how many slices of bread do you need?"
bread = raw_input()
print "How many spoons of jelly do you need?"
jelly = raw_input()
print "Okay how about the PB?"
pb = raw_input()

print "So you can make %r sandwihes if you have %r slices of bread, %r spoons of jelly and %r spoon of peanut butter. That sounds like a great sandwich!" %(total, bread, jelly, pb)

# Third Goal: Modify that program to allow you to make open-face sandwiches ifyou have an odd number of slices of bread ( )

Bread = 16
Jelly = 1
PB = 4


if Bread % 2 == 1:
    print 'Make open faced sandwiches'
else:
    print 'full sandwich with bread on both sides!'

#% 2 means if you divide bread/2, then what would be the remainder? that's why if bread is an even number, you'd get zero, if bread is an odd number, you'd get 1
    

# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches
Bread = 0
Jelly = 0
PB = 0

if Bread <=10 and Jelly ==1 and PB >= 5:
    print 'Great, I can make many sandwich'
elif Bread <=10 and Jelly ==1 and PB <=5:
    print 'I need more PB so that I can make my sandwich'
elif Bread <=5 and Jelly <1 and PB >=5:
    print 'Ok on the PB, but need more Bread and Jelly'
else:
    print 'Well life sucks'

#change the values for Bread, Jelly and PB to see what prints

# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life.  
Wow, your program is kinda judgy

Bread = 15
Jelly = 30
PB = 15

if Jelly/Bread == 3:
    print "I can make one sandwich"
elif 1 < Jelly/Bread < 3:
    print "I can make one full sandwich without enough Jelly"
elif Jelly/Bread == 1:
    print "Well I guess i'll make just half a sandwich"

#change the values for Bread, Jelly and PB to see what prints








