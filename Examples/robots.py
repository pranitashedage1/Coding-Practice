'''
Amazon uses small, Roomba-shaped robots, called "Drives", 
to deliver large stacks of products to human workers by following set paths around a warehouse. 
The warehouse can be represented in the form of a Cartesian plane, 
where robots are located at integral points of the form (x, y). When a product 
is to be delivered to some point (i, j), the nearest robot is sought and chosen.

A robot is considered idle if it has a robot located above, below, left, and right of it. 
Given the locations of n robots, find the number of idle robots.
'''
# def idlerobots(x, y):
#     robots = list(zip(x, y))
#     print(robots)
#     for i, j in robots:
#         i
#     return

def count_idle_robots(x, y):
    # Create dictionaries to store robots by row and column
    rows = {}
    cols = {}

    for rx, ry in zip(x, y):
        if rx not in rows:
            rows[rx] = set()
        if ry not in cols:
            cols[ry] = set()
        rows[rx].add(ry)
        cols[ry].add(rx)

    # Initialize idle robot count
    idle_count = 0

    # Check each robot's neighbors
    for rx, ry in zip(x, y):
        # Check for robots above and below in the same column
        has_above = any(r > ry for r in rows[rx])
        has_below = any(r < ry for r in rows[rx])
        # Check for robots to the left and right in the same row
        has_left = any(c < rx for c in cols[ry])
        has_right = any(c > rx for c in cols[ry])

        if has_above and has_below and has_left and has_right:
            idle_count += 1

    return idle_count

# Example coordinates
x = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
y = [1, 2, 3, 1, 2, 3, 5, 1, 2, 3]

# Calculate the number of idle robots
idle_robots = count_idle_robots(x, y)
print(idle_robots)  # Expected output: 2



