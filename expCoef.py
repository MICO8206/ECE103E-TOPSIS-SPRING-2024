import numpy as np


data = np.array([
    [15000, 'high', 500, 'v poor'],   # Object 1
    [25000, 'v high', 2000, 'poor'],       # Object 2
    [29000, 'low', 15000, 'good'],         # Object 3
    [30000, 'v low', 0, 'v poor']      # Object 4 referance
])


weights = np.array([0.25, 0.50, 0.20, 0.10])


impacts = np.array([1, -1, 1, 1])


def normalize(data):
    mins = np.min(data, axis=0)
    maxs = np.max(data, axis=0)
    return (data - mins) / (maxs - mins)

normalized_data = normalize(data.astype(float))


weighted_normalized_data = normalized_data * weights


ideal_solution = np.max(weighted_normalized_data, axis=0)
anti_ideal_solution = np.min(weighted_normalized_data, axis=0)


def euclidean_distance(x, y):
    return np.sqrt(np.sum((x - y) ** 2))

dist_to_ideal = np.array([euclidean_distance(x, ideal_solution) for x in weighted_normalized_data])
dist_to_anti_ideal = np.array([euclidean_distance(x, anti_ideal_solution) for x in weighted_normalized_data])


performance_scores = dist_to_anti_ideal / (dist_to_ideal + dist_to_anti_ideal)


ranked_indices = np.argsort(performance_scores)[::-1]


print("Ranking of objects (from best to worst):")
for i, idx in enumerate(ranked_indices):
    print(f"{i+1}. Object {idx+1} ({performance_scores[idx]})")
