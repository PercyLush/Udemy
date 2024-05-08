import re
upper_and_lower = r"[A-z]+"
upper = r"[A-Z]+"
digit = r"[0-9]+"
lower = r"[a-z]+"


def is_alnum(s):

        match1 = re.search(upper, s)
        match2 = re.search(lower, s)
        match3 = re.search(digit, s)
        if match1:
            print(True)
        elif match2:
            print(True)
        elif match3:
            print(True)
        else:
            print(False)

def is_alpha(s):

        match1 = re.search(upper, s)
        match2 = re.search(lower, s)
        if match1:
            print(True)
        elif match2:
             print(True)
        else:
            print(False)

def is_digit(s):

        match1 = re.search(digit, s)
        if match1:
            print(True)
        else:
            print(False)

def is_lower(s):

        match1 = re.search(lower, s)
        if match1:
            print(True)
        else:
            print(False)

def is_upper(s):

        match1 = re.search(upper, s)
        if match1:
            print(True)
        else:
            print(False)
            
if __name__ == '__main__':
    s = input()
    is_alnum(s)
    is_alpha(s)
    is_digit(s)
    is_lower(s)
    is_upper(s)

    