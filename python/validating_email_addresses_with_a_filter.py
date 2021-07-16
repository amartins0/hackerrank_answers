import re

pattern = '^[\\w_-]+@[a-zA-Z0-9]+\\.[a-z]{1,3}$'

def fun(s):
    return re.match(pattern, s)
