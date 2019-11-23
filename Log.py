class Log:
    '''Provides Log files handling'''

    # Constr.
    def __init__(self, file_path: str, data_array: []):

        # store filename
        if file_path.count("\\") > 0:
            self.file_name = file_path[file_path.find("\\") + 1:]
        else:
            self.file_name = file_path

        # check and store the data
        self.data_array = Log.check_data(data_array)

    # Exec. certain func. of the class
    def exec(self, opt: int):
        '''Execute function by it's order if the data is exists in the "data_array"'''

        # check if data exists
        if len(self.data_array) > 0:

            # list of funcs
            funcs = Log.show_details, Log.show_per_date, Log.show_adresses, Log.show_total_records

            # if value in range
            if 0 < opt <= len(funcs):
                Log.print(funcs[opt - 1](self.data_array, self.file_name))  # print result of certain fun.
        else:
            print("No valid data have been loaded!")

    # Funcs names
    @staticmethod
    def get_funcs_names() -> str:
        '''Returns a string with available functions'''
        return "1. Show details\n2. Show per date\n3. Show addresses\n4. Show total records"

    # Funcs total num.
    @staticmethod
    def get_funcs_number() -> int:
        '''Returns a total amount of available functions'''
        return 4

    # Show details
    @staticmethod
    def show_details(data_array: [], *args) -> str:
        '''
        Proccess the log data to obtain a date, time and command info
        :param data_array: A list with a log data, other params not used (catch only)
        :return: formated string with the info
        '''
        date_time_len = 15  # date and time chars at the beginning of line 'JAN 20 10:10:10'
        t_str = ""

        # build lines in result
        for line in data_array:
            raw_str = str(line)

            # concat. appr. parts (date + command)
            t_str += raw_str[:date_time_len] + " : " + raw_str[raw_str.find(":", date_time_len) + 1:].lstrip() + "\n"

        return t_str

    # Show per date
    @staticmethod
    def show_per_date(data_array: [], *args):
        '''
        Proccess the log data to count records for each date
        :param data_array: A list with a log data, other params not used (catch only)
        :return: formated string with the dates and their appearances counter
        '''
        date_len = 6  # the lenght of a date repr. in ex. 'JUN 10'
        t_str = ""

        # list of unique dates in the list
        unique_dates = list(set([line[:date_len] for line in data_array]))

        # sort the list
        unique_dates.sort()

        # unique dates + counter
        for date in unique_dates:
            t_str += "\n" + date + " - " + str(
                sum(date in line[:date_len] for line in data_array))  # sum date presense in date part of each line

        # create result
        res = "Found " + str(len(unique_dates)) + " different dates\n--------------------------------" + t_str

        return res

    # Show addresses
    @staticmethod
    def show_adresses(data_array: [], *args):
        '''
        Proccess the log data to get a list with memory addresses
        :param data_array: A list with a log data, other params not used (catch only)
        :return: formated string with the memory addresses (non-repeated)
        '''
        addr_list = []

        # find all addresses
        for line in data_array:
            while line.find("[") > 0:
                addr_list.append(line[line.find("["): line.find("]") + 1])
                line = line[line.find("]") + 1:]

        # remove duplicates and sort
        addr_list = list(set(addr_list))
        addr_list.sort()

        res = "Memory dump:\n----------------"

        # add to result
        for val in addr_list:
            res += "\n" + val

        return res

    # Show total records
    # @staticmethod
    def show_total_records(data_array: [], filename: str):
        '''Return a string showing total records found in a certain file'''
        return str(len(data_array)) + " Records found at " + filename

    # Print
    @staticmethod
    def print(data: str):
        '''Prints the string provided to the screen'''
        print(data)

    # Check data
    @staticmethod
    def check_data(data_array: []) -> []:
        '''
        Proccess the log data to obtain a list with valid log records
        :param data_array: A list with a log data
        :return: list with valid log records
        '''
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        # check 3rd ':' sign and remove spaces at beg. of line
        checked_data = [str(line).lstrip() for line in data_array if str(line).count(":") >= 3]

        # check if a line has the following format [month] [space] [number 1-31]
        checked_data = [line for line in checked_data if
                        line[:3] in months and line[4:6].isdecimal() and 1 <= int(line[4:6]) <= 31]

        return checked_data
