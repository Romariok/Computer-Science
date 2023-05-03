import re

def readfile(s):
    file = open(s, encoding='utf8')
    s = file.readlines()
    k = []
    for i in s:
        tmp = i.rstrip()
        k.append(tmp)
    return k

print("Введите тип взаимодействия с программой\n1 - Встроенные тесты\n2 - Саммостоятельное введение группы и текста")
k = int(input())

if k == 1:
    group = r'P0000'
    groups = [r'M5144', r'N121', r'J5555', r'K918273', r'P3112']

    s = readfile("dop2_tests/dop2_test.txt")
    for i in s:
        tmp = re.findall(r'(?<=[а-я]\s)[А-Я](?<!\.)', i)
        tmp = r'' + tmp[0] + '\.' + tmp[0] + '\.'
        if not bool(re.search(tmp, i)) or not bool(re.search(group, i)):
            print(i)

    print('')
    for j in range(1, 6):
        print(str(j), 'тест')
        s = readfile("dop2_tests/dop2_test" + str(j) + ".txt")
        for i in s:
            tmp = re.findall(r'(?<=[а-я]\s)[А-Я](?<!\.)', i)
            tmp = r'' + tmp[0] + '\.' + tmp[0] + '\.'
            if not bool(re.search(tmp, i)) or not bool(re.search(groups[j - 1], i)):
                print(i)
        print('')
else:
    print("Введите вашу группу")
    group = r''.join(str(input()))
    group = re.escape(group)
    print("Введите путь вашего теста относительно программы")
    path = str(input())
    s = readfile(path)
    for i in s:
        tmp = re.findall(r'(?<=[а-я]\s)[А-Я](?<!\.)', i)
        tmp = r'' + tmp[0] + '\.' + tmp[0] + '\.'
        if not bool(re.search(tmp, i)) or not bool(re.search(group, i)):
            print(i)

