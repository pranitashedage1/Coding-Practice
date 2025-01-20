def find_path(pyramid, target):
    def dfs(row, col, product, path):
        # If the product exceeds the target, stop exploring
        if product > target:
            return None
        # If we've reached the last row and the product matches the target, return the path
        if row == len(pyramid) - 1:
            return path if product == target else None

        # Explore the left child
        left_path = dfs(row + 1, col, product * pyramid[row + 1][col], path + 'L')
        if left_path:
            return left_path

        # Explore the right child
        right_path = dfs(row + 1, col + 1, product * pyramid[row + 1][col + 1], path + 'R')
        if right_path:
            return right_path

        # If no path is found, return None
        return None

    # Start the DFS search from the second row of the pyramid
    return dfs(0, 0, pyramid[0][0], '')

# Example input
pyramid = [
    [2],
    [4, 3],
    [3, 2, 6],
    [2, 9, 5, 2],
    [10, 5, 2, 15, 5]
]
target = 720


# pyramid = [
#     [1],
#     [2, 3],
#     [4, 1, 1],
# ]
# target = 2

# Find the path
result = find_path(pyramid, target)

# Output the result
print(result)  # Expected output: 'LRLL'
# print(result)  # Expected output: 'LR'
