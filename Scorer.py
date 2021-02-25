class Scorer:
    def __init__(self, filename):
        self.filename = filename

    def calculate_score(self):
        file = open(self.filename, "r")

        text_list = file.read().split(" ")

        print(text_list)

        # simulation_total_time
        # number_intersections

        # for seconds_passed in range()


Scorer("")