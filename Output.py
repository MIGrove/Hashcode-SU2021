def output(filename, intersections):
    f = open(filename, "w")
    f.write(str(len(intersections))+"\n")
    for inter in intersections:
        f.write(str(inter.id)+"\n")
        f.write(str(len(inter.schedule))+"\n")
        for i in inter.schedule.keys():
            f.write(i + " " + str(inter.schedule[i])+"\n")
