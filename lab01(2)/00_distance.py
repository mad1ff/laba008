sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

def calculate_distances(cities):
        distances = {}
        
        for city1, coords1 in cities.items():
            city_distances = {}
            for city2, coords2 in cities.items():
                if city1 != city2:
                    x1, y1 = coords1
                    x2, y2 = coords2
                    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                    city_distances[city2] = round(distance, 2)
            
            distances[city1] = city_distances
        
        return distances


def goroda():
    distances = calculate_distances(sites)
    print(distances)








