
def findSum(num):  #user-defined function
 if(num == 0):
    return num
 else:
    return (num + findSum(num - 1))

# take input
num = int(input('Enter a number: '))

# display result
print('The sum of n numbers =', findSum(num))