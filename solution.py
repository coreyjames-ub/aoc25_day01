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
# parsed_data = readData("data.txt")
# print(getAns(parsed_data))

def moreZeros(data):
    total = 100
    curr = 50
    temp = 0
    mod = 0
    zeros2 = 0
    for pair in data:
        dir = pair[0]
        mag = int(pair[1])
        mod = mag % total
        div = mag // total
        zeros2 += div
        if dir == "R":
            temp = curr + mag 
            if mod + curr >= total and curr != 0:
                zeros2 += 1
        else:
            temp = curr - mag
            if curr - mod <= 0 and curr != 0:
                zeros2 += 1
            
        curr = temp % total
        print(curr)
        print("zero count: " + str(zeros2))
    return zeros2
testdata=[("L", "6")]
test2 = [
    ("L", "68"),
    ("L", "30"),
    ("R", "48"),
    ("L", "5"),
    ("R", "60"),
    ("L", "55"),
    ("L", "1"),
    ("L", "99"),
    ("R", "14"),
    ("L", "82"),
]
test3 = [
    ("L", "50"),
    ("R", "1"),
]
# parsed_data
# print(moreZeros(test3))

txt = "5542145-5582046,243-401,884211-917063,1174-1665,767028-791710,308275-370459,285243789-285316649,3303028-3361832,793080-871112,82187-123398,7788-14096,21-34,33187450-33443224,2750031-2956556,19974-42168,37655953-37738891,1759-2640,55544-75026,9938140738-9938223673,965895186-966026269,502675-625082,11041548-11204207,1-20,3679-7591,8642243-8776142,40-88,2872703083-2872760877,532-998,211488-230593,3088932-3236371,442734-459620,8484829519-8484873271,5859767462-5859911897,9987328-10008767,656641-673714,262248430-262271846"

txt2 = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862"

def parse_ranges(txt):
    blocks = txt.split(",")
    data = ()
    ranges = []
    for block in blocks:
        nums = block.split("-")
        data = (int(nums[0]), int(nums[1]))
        ranges.append(data)
    return ranges

ranges = parse_ranges(txt)
# print(ranges)

def find_dbl(data):
    invalids = []
    for pair in data:
        for x in range(pair[0], pair[1]+1):
            txt = str(x)
            if len(txt) % 2 != 0:
                continue
            half = len(txt) // 2
            beg = txt[:half]
            end = txt[half:]
            if beg == end:
                invalids.append(x)
    total = 0
    for num in invalids:
        total += num
    return total
# test5 = [(9, 22)]
print(find_dbl(ranges))
