#author: Miguel COvarrubias
import numpy as np

# Separate numeric and string data
numeric_data = np.array([
    [15000, 500],   # Object 1
    [25000, 2000],  # Object 2
    [29000, 15000], # Object 3
    [30000, 0]      # Object 4 referance
])

string_data = np.array([
    ['high', 'v poor'],   # Object 1
    ['v high', 'poor'],   # Object 2
    ['low', 'good'],      # Object 3
    ['v low', 'v poor']   # Object 4 referance
])

# Hash function
def hash_string(string_data):
    return np.array([[hash(s) for s in row] for row in string_data])

hashed_string_data = hash_string(string_data)

# Combine numeric and hashed string data
data = np.concatenate((numeric_data, hashed_string_data), axis=1)

weights = np.array([0.25, 0.50, 0.20, 0.10])

# Modify your normalize function to only take numeric data
def normalize(data):
    mins = np.min(data, axis=0)
    maxs = np.max(data, axis=0)
    return (data - mins) / (maxs - mins)

normalized_data = normalize(data)

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
