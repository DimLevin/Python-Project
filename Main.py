import FileHandler as Fl
from Log import Log
import MyFunc as Mf


# Main
def main():
    # Get file name input
    file_path = Mf.user_input_str("Enter file path\\name: ")

    # Load data from file
    data_array = Fl.load_data(file_path)

    # If the data is loaded
    if data_array:
        log = Log(file_path, data_array)  # create new log handler
        Mf.program_menu(log)  # run menu

    else:
        print("Unable to load data.")


# Check for main
if __name__ == '__main__':
    main()
