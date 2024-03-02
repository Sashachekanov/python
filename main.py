import shutil

for i in range(1,11):
    shutil.copy('data.txt', str(i) + '//data')