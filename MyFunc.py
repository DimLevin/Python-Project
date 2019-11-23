from Log import Log


# Get user input for integer number
def user_input_int(msg: str) -> int:
    '''
    Gets user input for integer number
    :param msg: A message prompt to be shown
    :return: integer number
    '''
    while True:

        # get user input
        user_inp = input(msg)

        # check if integer num.
        if user_inp.isdecimal():
            return int(user_inp)
        else:
            print("Invalid input! Please enter a valid value.")


# Get user input for string
def user_input_str(msg: str) -> str:
    '''
    Gets user input for string
    :param msg: A message prompt to be shown
    :return: string
    '''
    while True:

        # get user input
        user_inp = input(msg)

        # check if the input contains only alpha-numeric characters
        if user_inp.isalnum():
            return user_inp
        else:
            print("Invalid input! Please enter only valid characters.")


# Program menu
def program_menu(log: Log):
    '''
    The program main menu
    :param log: A log data handler class
    :return: none
    '''
    funcs_num = Log.get_funcs_number()  # num of func. that can be executed via the menu

    print(Log.get_funcs_names() + "\n" + str(funcs_num + 1) + ". EXIT")  # print menu options

    while True:
        # get input from user
        opt = user_input_int("Enter option: ")

        # if input value within valid range
        if 0 < opt <= funcs_num:
            log.exec(opt)  # execute func.
        elif opt == funcs_num + 1:
            print("Thank you for using our program. Exiting...")
            break
        else:
            print("Wrong option!")
