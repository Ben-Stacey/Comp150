def function_a():
    print("Function_a was called")
    
def function_b():
    print("Function_b was called")
    
def function_c():
    print("Function_c was called")
    
def dispatch(choice):
    if choice == 'a':
        function_a()
    elif choice == 'b':
        function_b()
    elif choice == 'c':
        function_c()
    else:
        print("Invalid choice.")
        
        
choice = input("Choose a letter: ")
dispatch(choice)
