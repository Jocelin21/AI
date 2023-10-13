import itertools

graph = {
    'A': {'B': 12, 'C': 10, 'G': 12},
    'B': {'A': 12, 'C': 8, 'D': 12},
    'C': {'A': 10, 'B': 8, 'D': 11},
    'D': {'B': 12, 'C': 11, 'E': 11, 'F': 10},
    'E': {'C': 3, 'D': 11, 'F': 6, 'G': 7},
    'F': {'D': 10, 'E': 6, 'G': 9},
    'G': {'A': 12, 'C': 9, 'E': 7, 'F': 9}
}

# Calculate the total distance of a given route
def totalDistance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        city1, city2 = route[i], route[i + 1]

        # Check direct link between city1 and city2 in the graph
        if city2 in graph[city1]:
            total_distance += graph[city1][city2]
        else:
            # If there is no direct link, raise an error
            raise ValueError()
    return total_distance

def tsp(graph):
    cities = list(graph.keys())
    start = 'A'
    # Remove the starting city from the list of cities to visit
    cities.remove(start)

    shortestDistance = float('inf')
    shortestRoute = []

    # Explore different routes - permutations of the remaining cities
    for city in itertools.permutations(cities):
        # Route condition =  starts and ends in 'A'
        route = [start] + list(city) + [start]
        try:
            distance = totalDistance(route)
            # If this route is shorter than the previously shortest one, update the shortest route and distance
            if distance < shortestDistance:
                shortestDistance = distance
                shortestRoute = route
        except ValueError:
            # If no direct link between cities, continue with the next route
            pass

    return shortestRoute, shortestDistance

shortestRoute, shortestDistance = tsp(graph)
# Print the results
print("Shortest Route:", ' '.join(shortestRoute))
print("Total Distance:", shortestDistance)
