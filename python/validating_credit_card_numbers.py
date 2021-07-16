import re


pattern = r'^[4|5|6][0-9]{3}(-)?[0-9]{4}(-)?[0-9]{4}(-)?[0-9]{4}$'

for item in range(int(input())):
    i = input()
    if re.match(pattern, i) and not re.search(r'([\d])\1\1\1', i.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")