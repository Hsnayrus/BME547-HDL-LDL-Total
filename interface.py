def interface():
    print("My Program")
    print("Options: ")
    print("1 - Analyze HDL")
    print("9 - Quit")
    keep_running = True

    while keep_running:
        choice = input("Enter a choice: ")
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()


def input_HDL():
    HDL_input = input("Enter the HDL Value: ")
    return int(HDL_input)


def check_HDL(hdl_value):
    if hdl_value >= 60:
        return "normal"
    elif hdl_value >= 40 and hdl_value < 60:
        return "Borderline Low"
    else:
        return "Low"


def HDL_driver():
    hdl_value = input_HDL()
    answer = check_HDL(hdl_value)
    output_results(hdl_value, answer)


def output_results(hdl_value, answer):
    print("The results for an HDL value of {} is {}".format(hdl_value, answer))


interface()
