import os

flazki = 0
h = os.listdir()
for file_name in h:
    if file_name[-4:] == '.txt':
        with open(file_name, 'r', encoding='utf-8') as f:
            # print(f.read())
            if 'пупырка' in f.read():
                flazki = True
        if flazki:
            os.remove(file_name)
            flazki = 0
