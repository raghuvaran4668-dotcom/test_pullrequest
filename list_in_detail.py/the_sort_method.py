def the_sort_method(Lst: list) -> list:

    
    Lst.sort()  # sort the list in place.
    return Lst  # return the sorted list
print(the_sort_method([7,5,4,3,2,1])) # should return [1, 2, 3, 4, 5, 7]


def group_of_letters(name: str) -> list:
    """
    This function takes a string as an argument and returns a list of the letters in the string.
    """
    letters = list(name.replace(" ", ""))  # Convert string to list and remove spaces
    letters.sort(reverse=True)  # sort the list of letters in reverse order.
    return letters # return the sorted list of letters
print(group_of_letters("hello world")) # should return ['w', 'r', 'o', 'l', 'l', 'h', 'e', 'd']


# create a function that sorts a list by the length of the elements in the list
def sort_by_length(cricketers: list) -> list:
    return sorted(cricketers, key= len) # sort the list of cricketers by the length of the elements in the list

# Example list of cricketers
cricketers = ["Dhoni", "Kohli", "Rohit", "Ashwin", "Rahul"]
sorted_cricketers = sort_by_length(cricketers)
print(sorted_cricketers)  # Print the sorted list
print(sorted_cricketers[1])  # Print the person at index 1
