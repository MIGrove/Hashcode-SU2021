from Street import Street
from Car import Car

def input(inFiles):
    for j in range(len(inFiles)):

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
        streetParams = [m for m in infile.readline().split()]
        streetList.append( Street(int(streetParams[0]),int(streetParams[1]),streetParams[2],int(streetParams[3])) ) 

    carList = []
    for _ in range(nCars):     
        carParams = [m for m in infile.readline().split()]
        streetNames = []
        for j in range(int(carParams[0])):
            streetNames.append(carParams[j+1])

        carList.append( Car(int(carParams[0]), streetNames) )

    return(simDuration, nIntersections, points, streetList, carList)