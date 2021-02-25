inFiles = ["a.txt", "b.txt", "c.txt", "d.txt", "e.txt", "f.txt"]

for j in range(6):

    filename = inFiles[j]
    infile = open(filename, 'r')

    numbers = [int(m) for m in infile.readline().split()]
    simDuration = numbers[0]
    nIntersections = numbers[1]
    nStreets = numbers[2]
    nCars = numbers[3]
    points = numbers[4]