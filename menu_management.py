def add_item(menu, item):
    menu.append(item)

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} not found in menu!")

def check_item(menu, item):
    if item in menu:
        return f"{item} is available"
    return f"{item} is not available"

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]

item_to_add = "Tacos"
item_to_remove = "Salad"
item_to_check = "Pizza"

add_item(initial_menu, item_to_add)
remove_item(initial_menu, item_to_remove)

print("Updated menu:", initial_menu)
print(check_item(initial_menu, item_to_check))
