import random as r
import matplotlib.pyplot as plt
import math
import time

start_time = time.time()

MAX_X = 200
MAX_Y = 200
CENTROIDS = r.randint(3, 4)
POINTS = CENTROIDS * 300
POINTS_AT_CENTROIDS = [[] for _ in range(CENTROIDS)]

rand_centroids = [[
    r.randint(-MAX_X + 50, MAX_X - 50), r.randint(-MAX_Y + 50, MAX_Y - 50)
    ] for _ in range(CENTROIDS)]
new_centroids = []

rand_clst_points = []
for i in range(CENTROIDS):
    for _ in range(300):
        x = r.randint(rand_centroids[i][0] - r.randint(0, 15), rand_centroids[i][0] + r.randint(0, 25))
        y = r.randint(rand_centroids[i][1] - r.randint(0, 50), rand_centroids[i][1] + r.randint(0, 20))
        rand_clst_points.append([x, y])

def get_distance(dist_x, dist_y):
    dist = math.sqrt(dist_x**2 + dist_y**2)
    return dist

def assign_points():
    global at_cent
    for point in rand_clst_points:
        at_cent = 0
        min_dist = MAX_X
        for idx in range(len(rand_centroids)):
            dist = get_distance(
                rand_centroids[idx][0] - point[0],
                rand_centroids[idx][1] - point[1]
            )
            if dist < min_dist:
                min_dist = dist
                at_cent = idx
        POINTS_AT_CENTROIDS[at_cent].append(point) # [[[], []], []]

def calculate_new_centroids():
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

def plot_centroids():
    for i in range(POINTS):
        x = rand_clst_points[i][0]
        y = rand_clst_points[i][1]
        plt.scatter(x, y, color='green')

    for i in range(CENTROIDS):
        x1 = rand_centroids[i][0]
        y1 = rand_centroids[i][1]
        x2 = new_centroids[i][0]
        y2 = new_centroids[i][1]
        plt.scatter(x1, y1, color='red', marker='+', label='Old centroid')
        plt.scatter(x2, y2, color='orange', marker='*', label='New centroid')

assign_points()
calculate_new_centroids()
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
