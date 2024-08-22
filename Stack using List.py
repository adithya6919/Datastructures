def push_ele():
    x=int(input("Enter the element to be pushed inside the stack: "))
    list.append(x)
    print(f"{x} is appended inside the list ")

def pop_ele():
    if not list:
        print("The stack is empty!!!")
    else:
      e=list.pop()
      print(f"the popped element is {e} ")
      print(list)
    
print("Welcome to Python's Stack Club!")

list=[]
while True:
    a=int(input("Press the below numbers to decided which action to proceed with :\n1.Push\n2.Pop\n3.Print the list\n4.exit \n"))
    if a==1:
        push_ele()
    elif a==2:
        pop_ele()
    elif a==3:
        print(list)
    elif a==4:
        break


