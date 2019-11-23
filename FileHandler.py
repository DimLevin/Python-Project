# load data from file
def load_data(file_path: str) -> []:
    """
    This method is responsible to get a file (by given path) contents as a new list for allowed file types
    :param file_path: A path to a file to read from
    :return: file contents (a new list) -succes, None -else
    """
    allowed_files = [".log"]  # list of allowed file extensions

    file_path = file_path.lower()

    # if type is allowed
    if file_path[-4:] in allowed_files:

        # try to open the file
        try:
            with open(file_path, "r") as fl:
                return [line.rstrip('\n') for line in fl]  # getting a list of log lines

        # fail
        except FileNotFoundError:
            print("Couldn't find a file to read from.")
        except PermissionError:
            print('File reading permission denied.')
    else:
        print("Wrong file type.")

    return None
