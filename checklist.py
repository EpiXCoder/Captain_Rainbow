# CAPTAIN RAINBOW'S CHECKLIST
from colored import fg
checklist = []
# checklist = ['red socks', 'green hat']
# item_index = 6
# item_index = int(input("Index Number?"))
# if type(item_index) == int and item_index < len(checklist):
#     loop_var = False
# else: 
#     loop_var = True
# print (len(checklist))
# print(type(item_index))
# print (loop_var)

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    print(checklist[index])
    
# UPDATE
def update(index, item):
    checklist[index] = item
 
# DESTROY
def destroy(index):
    checklist.pop(index)
     
# LIST ALL ITEMS
index = 0
def list_all_items():
    print('\n***** Items Selected *****')
    index = 0
    for list_item in checklist:
        if 'red' in list_item.lower():
            color = fg(196)
        elif 'orange' in list_item.lower():
            color = fg(208)
        elif 'yellow' in list_item.lower():
            color = fg(226)
        elif 'green' in list_item.lower():
            color = fg(34)
        elif 'blue' in list_item.lower():
            color = fg(4)
        elif 'indigo' in list_item.lower():
            color = fg(27)
        elif 'violet' in list_item.lower():
            color = fg(99)
        print(color + "{} {}".format(index, list_item))
        index += 1
    print('**************************')
  

# MARK ITEMS AS COMPLETE
def mark_completed(index):
    checklist[index] = '√ ' + checklist[index]


# UNCHECK ITEMS MARKED AS COMPLETE
def uncheck_item(index):
    checklist[index] = checklist[index].replace('√ ','')


def select(function_code):
    # Create item
    if function_code == "A":
        input_item = user_input("Input item:")
        create(input_item)
        return True

    # Read item
    elif function_code == "R":
        item_index = int(user_input("Index Number?"))
        if type(item_index) == int and item_index < len(checklist):
            loop_var = False
        else: 
            loop_var = True
        while loop_var:
            print('Invalid Entry')
            item_index = int(user_input("Index Number?"))
            if type(item_index) == int and item_index < len(checklist):
                loop_var = False
            else: 
                loop_var = True
        read(item_index)
        return True
    
    # Update an item
    elif function_code == "U":
        item_index = int(user_input("Index Number?"))
        if type(item_index) == int and item_index < len(checklist):
            loop_var = False
        else: 
            loop_var = True
        while loop_var:
            print('Invalid Entry')
            item_index = int(user_input("Index Number?"))
            if type(item_index) == int and item_index < len(checklist):
                loop_var = False
            else: 
                loop_var = True

        input_item = user_input("Input item:")
        update(item_index, input_item)
        return True
    

    # Print all items
    elif function_code == "D":
        list_all_items()
        return True

    # Mark as complete
    elif function_code == "C":
        item_index = int(user_input("Index Number?"))
        if type(item_index) == int and item_index < len(checklist):
            loop_var = False
        else: 
            loop_var = True
        while loop_var:
            print('Invalid Entry')
            item_index = int(user_input("Index Number?"))
            if type(item_index) == int and item_index < len(checklist):
                loop_var = False
            else: 
                loop_var = True
        mark_completed(item_index)
        return True
    # Uncheck item marked as complete
    elif function_code == "Z":
        item_index = int(user_input("Index Number?"))
        if type(item_index) == int and item_index < len(checklist):
            loop_var = False
        else: 
            loop_var = True
        while loop_var:
            print('Invalid Entry')
            item_index = int(user_input("Index Number?"))
            if type(item_index) == int and item_index < len(checklist):
                loop_var = False
            else: 
                loop_var = True
        uncheck_item(item_index)
        return True

    # Delete an item
    elif function_code == "X":
        item_index = int(user_input("Index Number?"))
        if type(item_index) == int and item_index < len(checklist):
            loop_var = False
        else: 
            loop_var = True
        while loop_var:
            print('Invalid Entry')
            item_index = int(user_input("Index Number?"))
            if type(item_index) == int and item_index < len(checklist):
                loop_var = False
            else: 
                loop_var = True
        destroy(item_index)
        return True
    
    # Quit
    elif function_code == "Q":
        return False

    # Catch all
    else:
        print("Unknown Option")
        return True

# This function defines 'user_input' and will be called in the 'action loop'
def user_input(prompt):
    user_input = input(prompt)
    return user_input


# Action loop
print('Welcome Captain Rainbow!')
running = True
while running:
    selection = user_input("\nPress\nA to add to list\nU to update the list\nR to Read from list (use an existing index number)\nD to display list (add at least one item before selecting this option)\nC to Mark an item as complete\nZ to Uncheck an item marked as complete\nX to delete an item\nQ to quit\nEnter value: ")
    upper_selection = selection.upper()
    running = select(upper_selection)



