"""
----- Without using numpy -----
"""
import random as r
import matplotlib.pyplot as plt
import math
import time

start_time = time.time()

MAX_X = 500
MAX_Y = 200
CENTROIDS = r.randint(3, 4)
POINTS = CENTROIDS * 300
POINTS_AT_CENTROIDS = [[] for _ in range(CENTROIDS)]

centroids_cord = [[
    r.randint(-MAX_X + MAX_X//5, MAX_X - MAX_X//5), r.randint(-MAX_Y + MAX_Y//5, MAX_Y - MAX_Y//5)
    ] for _ in range(CENTROIDS)]
new_centroids = centroids_cord

rand_clst_points = []
for i in range(CENTROIDS):
    for _ in range(300):
        x = r.randint(centroids_cord[i][0] - r.randint(0, MAX_X//5), centroids_cord[i][0] + r.randint(0, MAX_X//4))
        y = r.randint(centroids_cord[i][1] - r.randint(0, MAX_Y//4), centroids_cord[i][1] + r.randint(0, MAX_Y//4))
        rand_clst_points.append([x, y])

def get_distance(dist_x, dist_y):
    dist = math.sqrt(dist_x**2 + dist_y**2)
    return dist

def k_mean_algo(n):
    def assign_points():
        global at_cent 
        global POINTS_AT_CENTROIDS
        POINTS_AT_CENTROIDS = [[] for _ in range(CENTROIDS)]
        for point in rand_clst_points:
            at_cent = 0
            min_dist = MAX_X
            for idx, val in enumerate(new_centroids):
                dist = get_distance(
                    new_centroids[idx][0] - point[0],
                    new_centroids[idx][1] - point[1]
                )
                if dist < min_dist:
                    min_dist = dist
                    at_cent = idx
            POINTS_AT_CENTROIDS[at_cent].append(point) # [[[], []], []]

    def calculate_new_centroids():
        global new_centroids
        new_centroids = []
        for point_set in POINTS_AT_CENTROIDS:
            l = len(point_set)
            sum_x = 0
            sum_y = 0
            for points in point_set:
                sum_x += points[0]
                sum_y += points[1]
            mean_x = int(sum_x / l)
            mean_y = int(sum_y / l)
            new_centroids.append([mean_x, mean_y])
        # print(new_centroids)

    for _ in range(n):
        assign_points()
        calculate_new_centroids()

def plot_centroids():
    for i in range(POINTS):
        x = rand_clst_points[i][0]
        y = rand_clst_points[i][1]
        plt.scatter(x, y, color='green')

    for i in range(CENTROIDS):
        x1 = centroids_cord[i][0]
        y1 = centroids_cord[i][1]
        x2 = new_centroids[i][0]
        y2 = new_centroids[i][1]
        plt.scatter(x1, y1, color='red', marker='+', label='Old centroid')
        plt.scatter(x2, y2, color='orange', marker='*', label='New centroid')

k_mean_algo(500)
plot_centroids()

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Centroids and random points.')
plt.grid(True)
plt.legend()
end_time = time.time()
print(f'Program time: {end_time - start_time}')
plt.show()
# print(guess_centroids)

# End of file
