def interface():
    print("My Program")
    print("Options: ")
    print("9 - Quit")
    keep_running = True
    
    while keep_running:
        choice = input("Enter your choice: ")
        if choice == '9':
            return

def input_HDL():
    HDL_input = input("Enter the HDL Value: ")
    return int(HDL_input)

interface()