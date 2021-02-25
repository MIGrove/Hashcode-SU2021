def output(filename, intersections):
    f = open(filename, "w")
    f.write(len(intersections))
    for inter in intersections:
        f.write(inter.id)
        f.write(inter.nIncomingStreets)
        for i in inter.schedule.keys:
            f.write(i + " " + inter.schedule[i])
