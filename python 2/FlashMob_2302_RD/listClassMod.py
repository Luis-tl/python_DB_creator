import ioMod as io
import editMod as ed

# escape sequence color
# \033[XXXm

PINK = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[0;31m'
WHITE_ON_RED = '\033[0;37;41m'
WHITE_ON_RED2 = '\033[101;97m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

class List: # class muss beginn with capital letter

    # constructor
    def __init__(self, fpath):
        self.fpath = fpath
        self.list = []
        self.load_list()
        self.changed = False

    def __del__(self):
        if self.changed:
            answer = input("Do you want to save your changes? y / n : ")
            if answer == "y":
                self.save_list()
        print('List is saved')

    def modify_sublist(self, mod_no, prompts, allowed_symbols_tpl):
            mod_sublist = []
            mod_sublist.append(mod_no)
            for index in range(1, len(prompts)):
                item = ed.edit_item(prompts[index], allowed_symbols_tpl[index])
                if item == "q":
                    break
                mod_sublist.append(item)

            for index, sublist in enumerate(self.list):
                if sublist[0] == mod_no:
                    self.list[index] = mod_sublist
                    self.changed = True
                    break


    def edit_list(self, prompts, allowed_symbols_tpl):
        while True:
            sublist = []
            for index, prompt in enumerate(prompts):
                # enumerate and assign a new number for the item
                if index == 0:
                    # take the last item of the list. bookid is the last element
                    if len(self.list) == 0:
                        bookid = "001"
                    else:
                        bookid = int(self.list[-1][0]) + 1
                        item = f"{bookid:>03}"
                    #print(item)
                    sublist.append(item)
                    continue
                # end of the numeration
                item = ed.edit_item(prompt, allowed_symbols_tpl[index])
                if item == "q":
                    break
                sublist.append(item)
            # ends the while loop
            if item == "q":
                break
            self.list.append(sublist)
            self.changed = True

    def print_list(self, format_tpl, headers):
        formatStr = ""
        for index, header in enumerate(headers):
            if format_tpl[index] == 0:
                continue
            formatStr += f"{header:{format_tpl[index]}}"
        print(formatStr)
        # draw line after header line
        sum = 0
        for i in format_tpl:
            sum += i
        print(sum * "-")

        for sublist in self.list:
            formatStr = f""
            for index, item in enumerate(sublist):
                if format_tpl[index] == 0:
                    continue
                if index == 2:
                    formatStr += f"{GREEN}"
                item = item[:format_tpl[index]-1]
                formatStr += f"{item:{format_tpl[index]}}"
                formatStr += f"{ENDC}"
            print(formatStr)

    def load_list(self):
        file = io.fopen(self.fpath, "r")

        if file:
            for line in file:
                line = line[:-1]
                sublist = line.split(',')
                self.list.append(sublist)
            file.close()

    def save_list(self):
        file = io.fopen(self.fpath, "w")
        for sublist in self.list:
            formatStr = f""
            for item in (sublist):
                formatStr += f"{item},"
            formatStr = formatStr[:-1] + '\n'
            file.write(formatStr)

        file.close()
        self.changed = False # error by saving and closing

    def del_sublist(self, del_no):
        deleted_sublist = False

        if int(self.list[-1][0]) >= int(del_no):
            for index, sublist in enumerate(self.list):
                if sublist[0] == del_no:
                    deleted_sublist = self.list.pop(index)
                    break
        return deleted_sublist
