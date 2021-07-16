import re


pattern = "(?<= )(&&|\|\|)(?= )"

for lines in range(int(input())):
    line = str(input())
    print(re.sub(pattern, lambda x: "and" if x.group() == "&&" else "or", line))
    
