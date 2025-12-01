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

def getAns(data):
    curr = 50
    temp = 0
    zeros = 0
    for pair in data:
        dir = pair[0]
        mag = pair[1]
        if dir == "R":
            temp = curr + int(mag)
        else:
            temp = curr - int(mag)
        curr = temp % 100
        if curr == 0:
            zeros+=1 
    return zeros
parsed_data = readData("data.txt")
print(getAns(parsed_data))

