# Sum of natural numbers up to num

value = int(input("Please enter the number: "))

#create a sum variable to store  the sum
sum = 0

# loop through the numbers from 0 to num
for val in range(0, value + 1):
    
    sum = sum + val
    
# return the sum
print("The sum of the numbers from 0 to num is: ", sum)
