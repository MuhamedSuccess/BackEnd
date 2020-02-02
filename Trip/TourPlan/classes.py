class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getTourPlan(self):
        tour_plan = TourPlan()


class TourPlan:

    def __init__(self):
        self.__schedule = None
        # schedule contains multiple locations to visit
        self.__location = list()
        self.__guide = None

    def setSchedule(self, schedule):
        self.__schedule = schedule

    def setLocation(self, location):
        self.__location.append(location)

    def setGuide(self, guide):
        self.__guide = guide


class Builder:
    def getSchedule(self): pass

    def getLocation(self): pass

    def getGuide(self): pass


class Schedule:
    __location = None

    def __init__(self, check_in, check_out, event, date):
        self.check_in = check_in
        self.check_out = check_out
        self.event = event
        self._date = date

    def setLocation(self, location):
        self.__location = location
