# Initialize an empty list to store items
todo_list = []
# All actions on main_menu
def main_menu():
    print('''
    1. Add To List
    2. Remove From List
    3. Edit List Item
    4. View Entire To-Do List
    5. EXIT''')

def add_prompt():
    item_added = input("Enter Item To Add: ")
    print(f"\nAdded {item_added} to to-do list!")
    todo_list.append(item_added)
    print(f"\nNew List: {todo_list}")
    return item_added

def remove_prompt():
    try:
        item_removed = input("Enter Item To Remove: ")
        todo_list.remove(item_removed)
        print(f"\nRemoved {item_removed} from list.")
        print(f"\nNew List: {todo_list}")
    except ValueError:
        print(f"\nError: {item_removed} not found in list.")
    return item_removed

def edit_prompt():
    try:
        item_removed = input("Enter the list item needing an edit: ")
        todo_list.remove(item_removed)
        edited_item = input("Enter the new item: ")
        todo_list.append(edited_item)
        print(f"\n{item_removed} replaced with {edited_item}")
        print(f"\nNew List: {todo_list}")
        return edited_item
    except ValueError:
        print(f"\nError: {item_removed} not found in list.")

def view_prompt():
    print("\nCurrent To-Do List:")
    for idx, item in enumerate(todo_list, start=1):
        print(f"{idx}. {item}")
    return todo_list
# My Loop for Main_Menu 
while True:
    main_menu()
    try:
        prompt = int(input("Enter number of process desired: "))
        if prompt == 5:
            print("Exiting the program. Goodbye!")
            break
        elif prompt == 1:
            add_prompt()
        elif prompt == 2:
            remove_prompt()
        elif prompt == 3:
            edit_prompt()
        elif prompt == 4:
            view_prompt()
        else:
            print("\nError, invalid action or event. Try again.")
    except ValueError:
        print("\nError, invalid input. Please enter a number (1-5).")
