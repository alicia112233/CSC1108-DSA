def color(country):
    global countryColor
    global map

    N = len(map)

    if country == N:
        printSolution()
        exit()

    usedColor = set([])
    availableColor = set([1, 2, 3, 4])

    for i in range(N):
        if map[country][i] == 1 and countryColor[i] > 0:
            usedColor = usedColor.union(set(countryColor[i]))

    availableColor = availableColor.difference(usedColor)

    for aColor in availableColor:
        countryColor[country] = aColor
        color(country + 1)
        
def readMap(filename):
    global map
    f = open(filename, 'r')
    for line in f:
        map.append([int(x) for x in line.split(",")])
    f.close()
    
readMap('map.txt')

def initializeColor(map):
    N = len(map)
    for i in range(N):
        countryColor.append(0)

initializeColor(map)
color(0)

colorCode = ['Red', 'Green', 'Blue', 'Yellow']
countryColor = []
map = []

def printSolution():
    global colorCode
    for i in range(len(countryColor)):
        print("Country", i, ": ", colorCode[countryColor[i] - 1])