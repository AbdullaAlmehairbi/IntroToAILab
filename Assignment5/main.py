import random

random.seed(42)

distances = [
    [0, 4, 8, 6, 7, 9, 5],
    [4, 0, 5, 7, 3, 8, 6],
    [8, 5, 0, 4, 6, 3, 7],
    [6, 7, 4, 0, 5, 6, 8],
    [7, 3, 6, 5, 0, 4, 6],
    [9, 8, 3, 6, 4, 0, 5],
    [5, 6, 7, 8, 6, 5, 0]
]

def distance(route):
    trip = [0] + route + [0]
    return sum(distances[a][b] for a, b in zip(trip, trip[1:]))


def select(population):
    return min(random.sample(population, 3), key=distance)


def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(7), 2))
    child = [None] * 6
    child[start:end] = parent1[start:end]
    remaining = iter(city for city in parent2 if city not in child)
    return [next(remaining) if city is None else city for city in child]


population = [random.sample(range(1, 7), 6) for _ in range(60)]

for generation in range(100):
  
    next_population = [min(population, key=distance)[:]]

    while len(next_population) < 60:
        child = crossover(select(population), select(population))

   
        if random.random() < 0.2:
            i, j = random.sample(range(6), 2)
            child[i], child[j] = child[j], child[i]

        next_population.append(child)

    population = next_population

best = min(population, key=distance)
print("Best route:", " -> ".join("ABCDEFG"[i] for i in [0] + best + [0]))
print("Total distance:", distance(best), "km")