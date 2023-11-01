# Basic 
for i in range (0,151) : 
    print (i)

# Multiples of Five
for num in range(5, 1001, 5):
    print(num)

#Counting, the Dojo Wa
for num in range(1, 101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)

#Whoa. That Sucker's Huge 
# Initialize a variable to store the sum
total_sum = 0

# Loop through odd integers from 1 to 500,000
for num in range(1, 500001, 2):
    total_sum += num

# Print the final sum
print(total_sum)

#Countdown by Fours
for num in range(2018, 0, -4):
    print(num)

# Flexible Counter 
lowNum = 2
highNum = 9
mult = 3

for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)

