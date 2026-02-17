def add_fruit(fruit_list, fruit):
    if fruit not in fruit_list:
        fruit_list.append(fruit)
    return fruit_list

fruits = ["apple", "banana", "cherry"]
print(add_fruit(fruits, "orange"))
