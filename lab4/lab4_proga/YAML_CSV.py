import csv, yaml

def refractor(g):
    s = str(g[0])
    if len(g)>=1:
        for i in range(1, len(g)):
            s+=(', '+str(g[i]))
    return s

with open('input.yaml', "r", encoding="UTF-8") as inp:
    with open("output.csv", "w", newline='') as out:
        suc = []
        fieldnames = ['Предмет']
        var = False
        read_data = yaml.load(inp, Loader=yaml.SafeLoader)
        for k, v in read_data.items():
            row = [k]
            for a, b in v.items():
                row.append(refractor(b))
                if not var:
                    fieldnames+=[a]
            if not var:
                writer = csv.writer(out)
                suc.append(fieldnames)
                var = True
            suc.append(row)
        writer.writerows(suc)