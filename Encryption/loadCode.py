def loadc(filename):
    try:
        with open(filename) as file_object:
            ass=[]
            for line in file_object:
                line=line.strip()
                ass.append(list(map(int,line.split(" "))))
            return ass
    except FileNotFoundError:
        return 0