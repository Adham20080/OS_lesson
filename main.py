with open("sana.txt", "r") as file:
    data = file.read()
    for i in data.split(' '):
        if 'a' in i:
            print(i, end=' ')
        else:
            continue
