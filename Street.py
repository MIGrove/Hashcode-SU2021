class Street:
    def __init__(self, start_intersection, end_intersection, street_name, time_to_drive):
        self.start_intersection = start_intersection
        self.end_intersection = end_intersection
        self.street_name = street_name
        self.time_to_drive = time_to_drive
        self.current_cars = []
