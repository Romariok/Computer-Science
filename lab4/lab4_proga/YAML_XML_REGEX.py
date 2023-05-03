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
        output.write(" "*2+"</"+lastline+">\n\n")
    else:
        if condition == True:
            condition = False
            line = re.search(pat1, line)
            line = line.group().replace('(', '.', -1).replace(')','.', -1).replace(' ', '', -1).replace(':', '', -1).replace('"', '', -1)
            output.write(" "*2+"<"+line+">\n")
            lastline = line
        else:
            if line[-1] != ':':
                k = re.sub(pat3, '', line)
                k = k.replace('<', '', -1).replace('>', '', -1)
                output.write(" "*4+'<'+tag1+'>'+k+"</"+tag1+">\n")
            else:
                tag1 = re.search(pat2, line)
                tag1 = tag1.group().replace('/', '', -1).replace(' ', '', -1)
output.write(" "*2+"</"+lastline+">\n")
output.write('</Расписание>')

input.close()
output.close()
