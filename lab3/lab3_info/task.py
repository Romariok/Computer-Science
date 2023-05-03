import re
file = open("task_text.txt", "r", encoding="UTF-8")
s = file.readlines()
for i in s:
    if bool(re.search(r'вна$', i)):
        print(i.rstrip())

file.close()