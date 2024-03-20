#author: Miguel Covarrubias-Conde
import math


def normalize_matrix(matrix):
    normalized_matrix = []
    for i in range(len(matrix[0])):
        column = [row[i] for row in matrix]
        max_val = max(column)
        min_val = min(column)
        normalized_column = [(value - min_val) / (max_val - min_val) for value in column]
        normalized_matrix.append(normalized_column)
    return normalized_matrix


def weighted_normalized_matrix(normalized_matrix, weights):
    weighted_normalized_matrix = []
    for i in range(len(normalized_matrix)):
        weighted_column = [value * weights[i] for value in normalized_matrix[i]]
        weighted_normalized_matrix.append(weighted_column)
    return weighted_normalized_matrix


def ideal_worst_cases(weighted_normalized_matrix, maximize):
    ideal_worst = []
    for i in range(len(weighted_normalized_matrix[0])):
        values = [row[i] for row in weighted_normalized_matrix]
        if maximize[i]:
            ideal_worst.append(max(values))
        else:
            ideal_worst.append(min(values))
    return ideal_worst


def euclidean_distances(weighted_normalized_matrix, ideal_best, ideal_worst):
    distances = []
    for row in weighted_normalized_matrix:
        ideal_best_distance = math.sqrt(sum([(x - y) ** 2 for x, y in zip(row, ideal_best)]))
        ideal_worst_distance = math.sqrt(sum([(x - y) ** 2 for x, y in zip(row, ideal_worst)]))
        distances.append(ideal_worst_distance / (ideal_best_distance + ideal_worst_distance))
    return distances


def topsis(matrix, weights, maximize):
    normalized_matrix = normalize_matrix(matrix)
    weighted_normalized_matrix = weighted_normalized_matrix(normalized_matrix, weights)
    ideal_best = ideal_worst_cases(weighted_normalized_matrix, maximize)
    ideal_worst = ideal_worst_cases(weighted_normalized_matrix, [not x for x in maximize])
    distances = euclidean_distances(weighted_normalized_matrix, ideal_best, ideal_worst)
    return distances


# V. HIGH/GOOD = 3
# HIGH/GOOD = 2
# LOW/POOR = 1
# V. LOW/POOR = 0
matrix = [
    [15000, 2, 500, 0],
    [25000, 3, 2000, 1],
    [29000, 2, 15000, 2],
    [30000, 1, 0, 1]
]
weights = [0.25, 0.50, 0.20, 0.10] # weights
maximize = [True, True, True, True]   # maximize all criteria


results = topsis(matrix, weights, maximize)
for i, result in enumerate(results):
    print(f'Alternative {i+1}: TOPSIS Score = {result}')

