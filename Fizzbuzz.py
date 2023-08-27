# alright fizz buzz why.... cause i can
# how to approuch the problem 1 layout the problem
# print 1 - 100 
# if a number can be devided by 3 print fizz 
# if a number can be devided by 5 print buzz
# if its devisable by both print fizz buss 

# lets define our variables 
fizz = 3
buzz = 5


# loops 0-100 times 
for i in range(1, 101):
#    if iterations devided == 0 its devisable by the defined variable and the second defined variable
    if i % fizz == 0 and i % buzz == 0:
        # print fizzbuzz, thank god for the and gate
        print('fizzbuzz')
        # if its not devidable by both check with fizz 
    elif i % fizz == 0:
        # if fizz is true print fizz instead of iteration 
        print('fizz')
        # if fizz is not true check buzz 
    elif i % buzz == 0:
        # if buzz is true print buzz 
        print('buzz')
        # if neither statment is true print iteration 
    else:
        print(i)
        
        # i originally had the sequence the other way around but it was messy, it did the job but was messy and missed some itterations when it got to fizzbuzz 