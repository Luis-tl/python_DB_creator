import ioMod as io


def readCfg(id, fpath):
    file = io.fopen(fpath,"r")
    list = []
    tagfound = False
    for line in file:
        if tagfound:
            if "$END" in line:
                break
            if "|" in line:
                line = tuple(line.split("|"))
            list.append(line[:-1])
        if id in line:
            tagfound = True

    return list

if __name__ == '__main__':
    fpath = "bookDB.cfg"

    prompts = readCfg("$PROMPTS", fpath)
    print(prompts)

    path = readCfg("$FPATH:", fpath)
    print(path)

    format_tpl = readCfg("$FORMAT:", fpath)
    print(format_tpl)

    symbols = readCfg("$SYMBOLS", fpath)
    print(symbols)

    headers = readCfg("$HEADERS", fpath)
    print(headers)
