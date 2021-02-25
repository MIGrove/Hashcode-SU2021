def input(filename, intersections):
    f = open(filename, "w")
    f.write(len(intersections))
    for inter in intersections.keys():
        f.write(inter)
        f.write(len(intersections[inter]))
        for i in intersections[inter].keys:
            f.write(i + " " + intersections[inter][i])
