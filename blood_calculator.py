def interface():
    print("My Program")
    print("Options: ")
    print("1 - Analyze HDL")
    print("2 - Analyze LDL")
    print("3 - Analyze Total Cholestrol Levels")
    print("9 - Quit")
    keep_running = True

    while keep_running:
        choice = input("Enter a choice: ")
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            Total_Cholestrol_Driver()


def input_HDL():
    HDL_input = input("Enter the HDL Value: ")
    return int(HDL_input)


def check_HDL(hdl_value):
    if hdl_value >= 60:
        return "Normal"
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
        return "Normal"
    elif ldl_value >= 130 and ldl_value < 160:
        return "Borderline High"
    elif ldl_value >= 160 and ldl_value < 190:
        return "High"
    else:
        return "Very High"


def output_LDL_results(ldl_value, answer):
    print("The results for an LDL value of {} is {}".format(ldl_value, answer))


def LDL_driver():
    ldl_input_value = input_LDL()
    answer = check_LDL(ldl_input_value)
    output_LDL_results(ldl_input_value, answer)


def input_Total_Cholestrol():
    cholestrol_input = input("Enter the level of cholestrol: ")
    return int(cholestrol_input)


def check_Total_Cholestrol(cholestrol_value):
    if cholestrol_value < 200:
        return "Normal"
    elif cholestrol_value >= 200 and cholestrol_value < 240:
        return "Borderline High"
    else:
        return "High"


def output_Total_Cholestrol_Levels(cholestrol_value, analysed_output):
    print("The results for a Total Cholestrol value of {} is {}".format(
        cholestrol_value, analysed_output))


def Total_Cholestrol_Driver():
    cholestrol_input = input_Total_Cholestrol()
    answer = check_Total_Cholestrol(cholestrol_input)
    output_Total_Cholestrol_Levels(cholestrol_input, answer)


def main():
    interface()


if __name__ == "__main__":
    main()
