#import pdb; pdb.set_trace()
#walking from london @ 2
#walking from Leicester @ 1

miles = 102
walking = True
miles_walked = 0
miles_walked2 = 0

#where do these men meet

while walking:
    if miles_walked <= miles:
        #man walking to leicester:
        print ("man1 on mile {}: <<{} man2 on mile").format(miles_walked, miles_walked2)
        miles_walked += 1
        miles_walked2  += 2
    else:
        walking = False

print ("all done now ")
