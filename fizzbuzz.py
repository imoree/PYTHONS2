
import sys

def f(num):

    for i in range(num):
        if i % 5 == 0 and i % 3 == 0:
            print "FizzBuzz"
        elif i % 3 == 0:
            print "Fizz"
        elif i % 5 == 0:
            print "Buzz"
        else:
            print i
    return

def fizz_buzz():
    # import pdb;pdb.set_trace()

    if len(sys.argv) == 1:
        answer = raw_input("please enter int ")
        try:
            answer = int(answer)
            f(answer)
        except ValueError:
            print "Error here buddy or girly "
    else:
        for arg in sys.argv[1:]:
            try:
                f(int(arg))
            except ValueError:
                # return "There was a problem with your value "
                print "Hey, had to terminate. Please enter in an integet next time"
                sys.exit()
    # return
while True:
    fizz_buzz()
