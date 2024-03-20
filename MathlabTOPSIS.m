data = [
    15000, 1, 500, 0;   
    25000, 0, 2000, 1;      
    29000, 2, 15000, 2;         
    30000, 3, 0, 1      
];

weights = [0.25, 0.50, 0.20, 0.10];

% Step 1: Normalize the data
norm_data = data ./ sqrt(sum(data.^2));

% Step 2: Calculate the weighted normalized decision matrix
weighted_norm_data = norm_data .* weights;

% Step 3: Determine the ideal and anti-ideal solutions
ideal_solution = max(weighted_norm_data);
anti_ideal_solution = min(weighted_norm_data);

% Step 4: Calculate the Euclidean distances to the ideal and anti-ideal solutions
dist_to_ideal = sqrt(sum((weighted_norm_data - ideal_solution).^2, 2));
dist_to_anti_ideal = sqrt(sum((weighted_norm_data - anti_ideal_solution).^2, 2));

% Step 5: Calculate the relative closeness to the ideal solution
closeness = dist_to_anti_ideal ./ (dist_to_ideal + dist_to_anti_ideal);

% Step 6: Sort the alternatives based on their relative closeness
[~, sorted_indices] = sort(closeness, 'descend');

% Print the sorted alternatives
fprintf('Sorted alternatives:\n');
disp(sorted_indices);

% Print the geometric results
fprintf('Geometric results:\n');
disp([dist_to_ideal, dist_to_anti_ideal, closeness]);
