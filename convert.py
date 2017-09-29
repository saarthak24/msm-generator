def convert(message):
    output = ""
    i = True  # capitalize
    for char in message:
        if i:
            output += char.lower()
        else:
            output += char.upper()
        i = not i
    return output
