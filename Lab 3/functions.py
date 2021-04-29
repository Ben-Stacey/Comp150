def new_line():
    print()

def three_lines():
    new_line()
    new_line()
    new_line()

def nine_lines():
    three_lines()
    three_lines()
    three_lines()
       
def clear_screen():
    nine_lines()
    nine_lines()
    nine_lines()
    nine_lines()
    three_lines()
    new_line()
    
def print_name(usr_name, today):
     print("Hello", usr_name, ", it;s nice to meet you!")
     print("Today is ", today)
     
print_name("Peter", "Monday")
clear_screen()
print_name("Ben", "Tuesday")