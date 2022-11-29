para_str = "Hello worlD"
i = 0
while i < len(para_str):
    if para_str[i].islower():
        print(para_str[i].upper())
    else:
        print(para_str[i].lower())
    i += 1

