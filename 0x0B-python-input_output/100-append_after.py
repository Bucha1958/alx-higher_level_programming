#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    string_buff = ""
    with open(filename, encoding="utf-8") as fd:
        for line in fd:
            string_buff += line
            if search_string in line:
                string_buff += new_string
                
    with open(filename, mode="w") as fd:
        fd.write(string_buff)
