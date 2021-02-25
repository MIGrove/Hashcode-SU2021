class Scorer:
    def __init__(self, filename):
        self.filename = filename

    def calculate_score(self):
        file = open(self.filename, "r")

        text_raw = file.read().replace('\n', ' ')
        text_list = text_raw.split(" ")
        text_list.pop()

        simulation_total_time = int(text_list[0])
        number_intersections = int(text_list[1])
        number_streets = int(text_list[2])
        number_cars = int(text_list[3])
        points_for_car_reaching_destination = int(text_list[4])

        # for seconds_passed in range(simulation_total_time):


Scorer("a.txt").calculate_score()
