def readData(path):
    arr = []
    temp = ()
    with open(path, "r") as file:
        for line in file:
            dir = line[:1]
            end = line[1:]
            parts = end.split("\n")
            val = parts[0]
            temp = (dir, val)
            arr.append(temp)
    return arr


parsed_data = readData("data.txt")