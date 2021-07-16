def merge_the_tools(string, k):
    for c in range(0, len(string), k):
        
        print(''.join(dict.fromkeys(string[c : c + k])))
