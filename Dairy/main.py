print("""
    Here is your dairy. Welcome!\n
    Choose your activity from the list \n
    \t 1. Show the task list.
    \t 2. Add the task.
    \t 3. Edit the task.
    \t 4. Finish the task
    \t 5. Begin the task again
    \t 6. Exit.
    """
    )


my_choise=()
while my_choise!=6:
    my_choise=int(input())
    if my_choise==1:
        print("1. Show the task list.")
    elif my_choise==2:
        print("2. Add the task.")
    elif my_choise==3:
        print("3. Edit the task.")
    elif my_choise==4:
        print("4. Finish the task")
    elif  my_choise==5:
        print("5. Begin the task again")
    elif my_choise == 6:
        print ("Goodbay")
    else:
        my_choise=int(input())
