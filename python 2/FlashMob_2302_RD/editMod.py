# check the input coming from main.py
def check_item(item, allowed_symbols):
    ok = True
    for letter in item:
        if (letter in allowed_symbols) or\
           (allowed_symbols[0] == "num" and letter.isdigit()) or\
           (allowed_symbols[0] == "alpha" and letter.isalpha()) or\
           (allowed_symbols[0] == "alnum" and letter.isalnum()) or \
           (allowed_symbols[0] == "all"):
            ok = True
        else:
            ok = False
            break
    return ok

# check the input. If right pass the input to listClassMod.py
def edit_item(prompt, allowed_symbols):
    while True:
        item = input(prompt)
        if item == 'q':
            break
        if check_item(item, allowed_symbols):
            break
    return item
