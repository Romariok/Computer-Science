import timeit

print("-----------------------------------Мой алгоритм-----------------------------------")
start1 = timeit.default_timer()

for i in range(100):
    input = open("input.yaml", "r", encoding="UTF-8")
    output = open("output.xml", "w", encoding="UTF-8")
    condition = True
    lastline = ''
    numdots = 0
    linebool = True
    tag1 = " "

    output.write('<Расписание>\n')
    for i in input.readlines():
        line = i.rstrip()
        if line == '':
            condition = True
            output.write(" "*2+"</" + lastline + ">\n\n")
        else:
            if condition == True:
                condition = False
                line = line[1:len(line) - 2]
                line = line.replace('(', '.', -1).replace(')', '.', -1).replace(' ', '', -1).replace(':', '', -1)
                output.write(" "*2+"<" + line + ">\n")
                lastline = line
            else:
                line = line.replace('/', '', -1)
                s = line.split(" ")
                if s[-1][-1] != ":":
                    for b in range(len(s)):
                        if s[0] != '' and s[0] != '-':
                            break
                        else:
                            s.pop(0)

                    output.write(" "*4+'<' + tag1 + '>' + ' '.join(s) + "</" + tag1 + ">\n")
                else:
                    tag1 = line[1:len(line) - 1].replace(' ', '', -1)

    output.write(" "*2+"</" + lastline + ">\n")
    output.write('</Расписание>')

    input.close()
    output.close()

stop1 = timeit.default_timer()
print("Test succesfully done\nTime: "+str(stop1-start1))

print("----------------------------Программа с помощью библиотеки------------------------")
start2 = timeit.default_timer()

for i in range(100):
    import yaml

    output = open("output1.xml", "w", encoding="UTF-8")
    output.write('<Расписание>\n')
    with open('input.yaml', "r", encoding="UTF-8") as fh:
        read_data = yaml.load(fh, Loader=yaml.SafeLoader)
        for i in read_data.keys():
            output.write(
                " "*2+'<' + i.replace('(', '.', -1).replace(')', '.', -1).replace(' ', '', -1).replace(':', '', -1) + '>\n')
            for j in read_data.get(i):
                for k in read_data.get(i).get(j):
                    output.write(" "*6+'<' + j.replace('/', '', -1).replace(' ', '', -1)
                                 + '>' + str(k) + '</'
                                 + j.replace('/', '', -1).replace(' ', '', -1) + '>\n')
            output.write(" "*2+'</' + i.replace('(', '.', -1).replace(')', '.', -1).replace(' ', '', -1).replace(':', '',
                                                                                                             -1) + '>\n')

    output.write('</Расписание>\n')
    output.close()

stop2 = timeit.default_timer()
print("Test succesfully done\nTime: "+str(stop2-start2))
print("--------------------Программа с помощью регулярных выражений----------------------")
start3 = timeit.default_timer()

for i in range(100):
    import re

    input = open("input.yaml", "r", encoding="UTF-8")
    output = open("output2.xml", "w", encoding="UTF-8")

    pat1 = r'"[а-яА-я():\s\w]+":$'
    pat2 = r'(?<=^\s\s)[а-яА-Я\.\/\s]+(?<!:)'
    pat3 = r'^[ -]+(?<!\w)'
    lastline = ''
    output.write('<Расписание>\n')

    condition = True

    for i in input.readlines():
        line = i.rstrip()
        if line == '':
            condition = True
            output.write("  </" + lastline + ">\n\n")
        else:
            if condition == True:
                condition = False
                line = re.search(pat1, line)
                line = line.group().replace('(', '.', -1).replace(')', '.', -1).replace(' ', '', -1).replace(':', '',
                                                                                                             -1).replace(
                    '"', '', -1)
                output.write(" "*2+"<" + line + ">\n")
                lastline = line
            else:
                if line[-1] != ':':
                    k = re.sub(pat3, '', line)
                    output.write(" "*4+'<' + tag1 + '>' + k + "</" + tag1 + ">\n")
                else:
                    tag1 = re.search(pat2, line)
                    tag1 = tag1.group().replace('/', '', -1).replace(' ', '', -1)
    output.write("  </" + lastline + ">\n")
    output.write('</Расписание>')

    input.close()
    output.close()

stop3 = timeit.default_timer()
print("Test succesfully done\nTime: "+str(stop3-start3))
