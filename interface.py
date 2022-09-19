def interface():
    print("My Program")
    print("Options: ")
    print("1 - Analyze HDL")
    print("2 - Analyze LDL")
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


def input_LDL():
    LDL_input = input("Enter the LDL value: ")
    return int(LDL_input)


def check_LDL(ldl_value):
    if ldl_value < 130:
        return "normal"
    elif ldl_value >= 130 and ldl_value < 160:
        return "borderline high"
    elif ldl_value >= 160 and ldl_value < 190:
        return "high"
    else:
        return "very high"


def output_LDL_results(ldl_value, answer):
    print("The results for an LDL value of {} is {}".format(ldl_value, answer))


def LDL_driver():
    ldl_input_value = input_LDL()
    answer = check_LDL(ldl_input_value)
    output_LDL_results(ldl_input_value, answer)


interface()
