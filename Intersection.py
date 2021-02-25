class Intersection:
    def __init__(self, id, schedule):
        self.id = id
        self.nIncomingStreets = len(schedule)
        self.schedule = schedule    # Dictionary with names of streets and duration of green light