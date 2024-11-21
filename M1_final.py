list = []

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
    list.append(item_added)
    print(f"\nNew List: {list}")
    return item_added

def remove_prompt():
    item_removed = input("Enter Item To remove: ")
    list.remove(item_removed)
    print(f"\n{item_removed} from list leaving: ")
    print(f"\n{list}")
    
    return item_removed

def edit_prompt():
    item_removed = input("Enter the list item needing an edit:  ")
    list.remove(item_removed)
    edited_item = input("Enter the edit to he made")
    list.append(edited_item)
    print(f"\n{item_removed} replaced with {edited_item}")
    print(f"\nLeaving: {list} ")
    return edited_item

def view_prompt():
    print(list)
    return list

while list == []:
    main_menu()
    prompt = str(input("Enter number of process desired "))
    if prompt == '5':
        break
    elif prompt == '1':
        add_prompt()
    elif prompt == '2':
        remove_prompt()
    elif prompt == '3':
        edit_prompt()
    elif prompt == '4':
        view_prompt()
    else:
        print(f"\nError, invalid action or event. Try again: {prompt}")