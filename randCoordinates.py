import pycristoforo as pyc

class randCoordinatesGenerator():
    """
    RandCoordinatesGenerator generates specified random points for a
    """
    def __init__(self, country_name, num_points):
        self.country_name = country_name
        self.num_points = num_points
        self.points = self.getCoordinates(self.country_name, self.num_points) 
        
        
    def getCoordinates(self, country_name, num_points):
        """" returns a list of tuples of the form (lat, long) """
        country = pyc.get_shape(country_name)
        points = pyc.geoloc_generation(country, num_points, country_name)
        points = [point['geometry']['coordinates'] for point in points]
        points = [(point[1], point[0]) for point in points]
        return points

    def printPoints(self):
        pyc.geoloc_print(points, ',')


