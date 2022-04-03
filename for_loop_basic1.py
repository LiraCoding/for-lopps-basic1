# Basic - Print all integers from 0 to 150.
for x in range(0, 151, 1):
    print(x)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(5,1001,5):
    print(i)

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for y in range(0,101):
    if y % 5 == 0:
        print("Coding")
    elif y %10 ==0:
        print("Coding Dojo")
    else:
        print(y)

# Add odd integers from 0 to 500,000, and print the final sum.
max = int(input(" Please Enter the Maximum Value : "))
sum = 0
for d in range(0, max + 1):
    if (d % 2 != 0):
        # print(d)
        sum+=d
        print(sum)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for var in range(2018, 0, -4):
    if var> 0:
        print(var)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3

for n in range(lowNum,highNum + 1):
    if n % mult == 0:
        print(n)
        