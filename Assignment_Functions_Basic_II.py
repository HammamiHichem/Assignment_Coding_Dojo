def countdown(nombre):
    liste_compte_a_rebours = list(range(nombre, -1, -1))
    return liste_compte_a_rebours

resultat = countdown(5)
print(resultat)

def print_and_return(liste):
    if len(liste) == 2:
        premier = liste[0]
        print(premier)
        return liste[1]
    else:
        print("La liste doit contenir exactement deux nombres.")

resultat = print_and_return([1, 2])
print(resultat)

def first_plus_length(input_list):
    if len(input_list) > 0:
        return input_list[0] + len(input_list)
    else:
        return 0  # Return 0 for an empty list

# Example usage:
my_list = [1, 2, 3, 4, 5]
result = first_plus_length(my_list)
print(result)  # This will output 6

def values_greater_than_second(input_list):
    if len(input_list) < 2:
        return False  # Return False for lists with less than 2 elements
    
    second_value = input_list[1]
    new_list = [value for value in input_list if value > second_value]
    
    print(len(new_list))
    return new_list

# Example usage:
example_list1 = [5, 2, 3, 2, 1, 4]
result1 = values_greater_than_second(example_list1)
print(result1)  # This will print "3" and return [5, 3, 4]

example_list2 = [3]
result2 = values_greater_than_second(example_list2)
print(result2)  # This will return False

def length_and_value(size, value):
    new_list = [value] * size
    return new_list

# Example usage:
result1 = length_and_value(4, 7)
print(result1)  # This will return [7, 7, 7, 7]

result2 = length_and_value(6, 2)
print(result2)  # This will return [2, 2, 2, 2, 2, 2]
