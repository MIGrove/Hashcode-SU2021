import math
from Input import input
from Output import output 
from Intersection import Intersection

inFiles = ["a.txt", "b.txt", "c.txt", "d.txt", "e.txt", "f.txt"]
outFiles = ["a_out.txt", "b_out.txt","c_out.txt","d_out.txt","e_out.txt","f_out.txt"]

simDuration, nIntersections, points, streetList, carList = input(["a.txt"])

intersections = []
for j in range(len(streetList)):
    schedule = {streetList[j].street_name : 1 }
    intersections.append( Intersection(streetList[j].end_intersection, schedule) )

output("a_out.txt", intersections)

#def loop():
#    for current_second in range(simDuration):
