command = input()

while not command == "End":
    if command == "SoftUni":
        pass
    else:
        text = ""
        for i in command:
            text += (i * 2)
        print(text)
    command = input()