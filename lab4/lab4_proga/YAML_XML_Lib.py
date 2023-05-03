import yaml
import dict2xml
output = open("output1.xml", "w", encoding="UTF-8")
temp = open("temp.yaml", "w", encoding="UTF-8")
with open('input.yaml', "r", encoding="UTF-8") as fh:
    bol = True
    for i in fh.readlines():
        line = i.rstrip()
        if line == '':
            bol = True
            temp.write(line+"\n")
        else:
            if bol:
                bol = False
                line = line[:line.find(":")]+line[line.find(":")+2:]
                if line[-1]!=":":
                    line+=":"
                temp.write(line+"\n")
            else:
                temp.write(line + "\n")
    temp.close()
    temp1 = open("temp.yaml", "r", encoding="UTF-8")
    read_data = yaml.load(temp1, Loader=yaml.SafeLoader)
    output.write(dict2xml.dict2xml(read_data, wrap="Расписание", indent = "  "))



output.close()
