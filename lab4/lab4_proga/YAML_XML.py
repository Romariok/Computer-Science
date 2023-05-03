input = open("input.yaml", "r", encoding="UTF-8")
output = open("output.xml", "w", encoding="UTF-8")
condition = True
lastline = ''
tag1 = " "

output.write('<Расписание>\n')
for i in input.readlines():
    line = i.rstrip()
    if line == '':
        condition = True
        output.write("  </"+lastline+">\n\n")
    else:
        if condition == True:
            condition = False
            line = line[1:len(line)-2]
            line = line.replace('(', '.', -1).replace(')','.', -1).replace(' ', '', -1).replace(':', '', -1)
            output.write("  <"+line+">\n")
            lastline = line
        else:
            line = line.replace('/', '', -1).replace('<', '', -1).replace('>', '', -1)
            s = line.split(" ")
            if s[-1][-1] !=":":
                for b in range(len(s)):
                    if s[0] !='' and s[0] !='-':
                        break
                    else:
                        s.pop(0)

                output.write(' '*4+'<'+tag1+'>'+' '.join(s)+"</"+tag1+">\n")
            else:
                tag1 = line[1:len(line)-1].replace(' ', '', -1)

output.write(" "*2+"</"+lastline+">\n")
output.write('</Расписание>')

input.close()
output.close()
