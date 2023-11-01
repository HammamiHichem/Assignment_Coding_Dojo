# #1 : Ok
def number_of_food_groups():
    return 5
print(number_of_food_groups())


# #2 name 'number_of_days_in_a_week_silicon_or_triangle_sides' is not defined 
def number_of_military_branches():
    return 5
print(7+ number_of_military_branches())
number_of_days_in_a_week_silicon_or_triangle_sides= (7)

# 3 number_of_books_on_hold
def number_of_books_on_hold():
    return (5, 10) 
result = number_of_books_on_hold()
print(result)  # This will print (5, 10)


#4
def number_of_fingers():
    return 5
    print(10) #The print(10) statement is never executed because the function has already returned 
print(number_of_fingers())


"""
5 You print the value of x, which is None
"""
def number_of_great_lakes():
    return (None)
x = number_of_great_lakes()
print(x)


"""
6 TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
"""
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))

# def add(b, c):
#     return b + c

# result = add(1, 2) + add(2, 3)
# print(result)

def add(b, c):
    return b + c

result = add(1, 2) + add(2, 3)
print(result)

# #7 ok 
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))




"""
#8 In the provided code, the number_of_oceans_or_fingers_or_continents function sets the variable b to the value 100 and then prints it. It then checks the value of b with an if statement. If b is less than 10, it returns 5; otherwise, it returns 10. The return 7 statement after the else block is effectively unreachable because the function has already returned a value in the if or else block.
"""
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


"""  
#9 number_of_days_in_a_week_silicon_or_triangle_sides(2, 3):
# b is 2, and c is 3.
# The condition 2 < 3 is true, so it returns 7.
# number_of_days_in_a_week_silicon_or_triangle_sides(5, 3):
# b is 5, and c is 3.
# The condition 5 < 3 is false, so it returns 14.
# number_of_days_in_a_week_silicon_or_triangle_sides(2, 3) + number_of_days_in_a_week_silicon_or_triangle_sides(5, 3):
# The first function call returns 7, and the second function call returns 14.
# You add 7 and 14 together, which results in 21
"""
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


#10 when you run the code, it will return 8, and you won't see the value 10.

def addition(b,c):
    return b+c
print(addition(3,5))

"""#11 You print the value of the global variable b, which is 500.
# The foobar function is defined but not called yet.
# You print the value of the global variable b again, which is still 500.
# You call the foobar function.
# Inside the foobar function, a new local variable b is defined with a value of 300. This local variable shadows (hides) the global variable b within the function's scope.
# You print the value of the local variable b inside the foobar function, which is 300.
# The function foobar finishes execution, and the local variable b within the function goes out of scope.
# You print the value of the global variable b again, which remains 500 because the local variable defined within the foobar function does not affect the global variable."""
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)


"""#12 b = 500 assigns the value 500 to the global variable b.
# print(b) prints the global variable b, so it will print "500".
# Now, we enter the foobar function:

# Inside the foobar function, b = 300 assigns the value 300 to a new local variable b that shadows the global b.
# print(b) inside the foobar function prints the local variable b, so it will print "300".
# return b returns the local variable b with a value of 300, but it's not being used in this code.
# After the function call to foobar, we continue with the global scope:

# print(b) again prints the global variable b, so it will print "500"."""
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)


"""#13 b = 500 assigns the value 500 to the global variable b.
# print(b) prints the global variable b, so it will print "500".
# Now, we enter the foobar function:

# Inside the foobar function, b = 300 assigns the value 300 to a new local variable b that shadows the global b.
# print(b) inside the foobar function prints the local variable b, so it will print "300".
# return b returns the local variable b with a value of 300.
# After the function call to foobar, you assign the result of the function (which is the local variable b with a value of 300) back to the global variable b.

# b = foobar() assigns the value returned by foobar (300) to the global variable b.
# Now, when you print b again:

# print(b) prints the global variable b, which now has a value of 300, so it will print "300".
# 500
# 300
# 300
"""
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)


"""#14 foo() is called.

# print(1) is executed, so it prints "1".
# bar() is called from within foo.
# Inside bar:

# print(3) is executed, so it prints "3".
# After bar returns, we return to the foo function:

# print(2) is executed, so it prints "2"."""
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()


"""#15
# foo() is called.

# print(1) is executed, so it prints "1".
# bar() is called from within foo.
# Inside bar:

# print(3) is executed, so it prints "3".
# return 5 returns the value 5 to where bar() was called from, which is within foo.
# The value returned by bar (which is 5) is assigned to the variable x.

# print(x) is executed, so it prints "5".
# return 10 in the foo function returns the value 10 to where foo() was called from, which is at the beginning of the code.

# The value returned by foo (which is 10) is assigned to the variable y.

# Finally, print(y) is executed, so it prints "10"."""
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)