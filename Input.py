from Street import Street
from Car import Car

def input(inFiles):
    for j in range(6):

        filename = inFiles[j]
        infile = open(filename, 'r')

        numbers = [int(m) for m in infile.readline().split()]
        simDuration = numbers[0]
        nIntersections = numbers[1]
        nStreets = numbers[2]
        nCars = numbers[3]
        points = numbers[4]

    streetList = []
    for _ in range(nStreets):
        streetParams = [int(m) for m in infile.readline().split()]
        streetList.append( Street(streetParams[0],streetParams[1],streetParams[2],streetParams[3]) ) 

    carList = []
    for _ in range(nCars):     
        carParams = [int(m) for m in infile.readline().split()]
        streetNames = []
        for j in range(carParams[0]):
            streetNames.append(carParams[j+1])

        carList.append( Car(carParams[0], streetNames) )

    return(simDuration, nIntersections, nStreets, nCars, points, streetList, carList)