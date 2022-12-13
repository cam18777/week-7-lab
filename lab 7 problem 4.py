# camryn echevarria
# 11/15/2022

# Problem 4 create a list of numbers that come back to the unique elements.
# making a randomm number list
numbers = [1, 2, 2, 3, 3, 4, 7]
# it create a function
def get_unique_numbers_list(list_numbers):
# its creating a place holder for the new list of numbers
    list_of_unique_numbers = []

    for number in list_numbers:

        if number in list_of_unique_numbers:
            continue
        # if the current number in the loop isn't in the list_of_unique_numbers then add it to the end
        else:
            list_of_unique_numbers.append(number)
    return list_of_unique_numbers

print(get_unique_numbers_list(numbers))
