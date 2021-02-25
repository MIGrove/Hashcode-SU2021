import math
from Input import input
from Output import output 
from Intersection import Intersection

inFiles = ["a.txt", "b.txt", "c.txt", "d.txt", "e.txt", "f.txt"]
outFiles = ["a_out.txt", "b_out.txt","c_out.txt","d_out.txt","e_out.txt","f_out.txt"]

for a in range(len(inFiles)):

	simDuration, nIntersections, points, streetList, carList = input([inFiles[a]])

	for car in carList:
		for street in car.streets_list:
			for street_alt in streetList:
				if street_alt.street_name == street:
					street_alt.cars_crossed += 1

	intersections = []
	for j in range(nIntersections):
		schedule = {}
		intersections.append( Intersection(j, schedule) )
		
	for street in streetList:
		intersections[street.end_intersection].schedule.update({street.street_name : min(simDuration, max(1, street.cars_crossed))})

	output(outFiles[a], intersections)
