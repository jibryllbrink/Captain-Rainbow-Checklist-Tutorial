checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

    # UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    return (index, "√" + checklist[item])
    #print("[completed items √]")
    #checklist[index] = "√" + checklist[index]
    #print(checklist[index])

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
        return True

    elif function_code == "R":
        item_index = user_input("Index Number?")
        read(int(item_index))
        return True

    elif function_code == "U":
        item_index = user_input("Index Number?")
        item_index = user_input("Edit item:")
        return True

    elif function_code == "D":
        item_index = user_input("destroy item?")
        return True
        # Remember that item_index must actually exist or our program will crash.
        #read(index)

        # Print all items
    elif function_code == "P":
        list_all_items()
        return True

    elif function_code == "Q":
        return  False
    # Catch all
    else:
        print("Unknown Option")
        return True
def test():
    create("purple sox")
    create("red cloak")

    #print(read(1))


    #update(0, "purple socks")
    #destroy(1)

    #print(read(0))
    #print(read(1))

    #select("C" or "c")
    ## View the results
    #list_all_items()
    ## Call function with new value
    #select("R" or "r")
    ## View results
    #list_all_items()
    ## Continue until all code is run
    #list_all_items()
    #mark_completed(1)

#test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, U to update from list, D to destroy from list, P to display list, and Q to quit")
    running = select(selection)
