def remove_fruit(fruit_list, fruit):
    if fruit in fruit_list:
        fruit_list.remove(fruit)
        print(fruit_list)
        return fruit_list
    else:
        print(f"Fruit '{fruit}' not found in the list")
        return fruit_list


