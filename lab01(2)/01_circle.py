RADIUS = 42
PI=3.1415926

def calculate_area(radius = RADIUS, pi = PI):
    S=pi*radius**2
    return round(S, 4)

def length_comparison (point, radius = RADIUS):
    x, y = point
    distance = (x**2 + y**2)**(1/2)
    return distance < radius


point_1 = (23, 34)
point_2 = (30, 30)
def ploshad():
    print(calculate_area())
    print(length_comparison(point_1))
    print(length_comparison(point_2))




