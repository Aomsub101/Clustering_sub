"""
----- Wihtout using numpy -----
"""
import random as r
import matplotlib.pyplot as plt
import math
import time

start_time = time.time()

COLORS = ['green', 'blue', 'black', 'purple']
MAX_X = 500
MAX_Y = 200
CENTROIDS = r.randint(3, 4)
POINTS_PER_CENTROID = 300
TOTAL_POINTS = CENTROIDS * POINTS_PER_CENTROID

centroids_cord = [[
    r.randint(-MAX_X + MAX_X // 5, MAX_X - MAX_X // 5), 
    r.randint(-MAX_Y + MAX_Y // 5, MAX_Y - MAX_Y // 5)
] for _ in range(CENTROIDS)]

rand_clst_points = []
for i, centroid in enumerate(centroids_cord):
    rand_clst_points.extend([
        [
            r.randint(centroid[0] - r.randint(0, MAX_X) // 5, centroid[0] + r.randint(0, MAX_X) // 4),
            r.randint(centroid[1] - r.randint(0, MAX_Y) // 4, centroid[1] + r.randint(0, MAX_Y) // 4)
        ]
        for _ in range(POINTS_PER_CENTROID)
    ])

def get_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def assign_points(points, centroids):
    clusters = [[] for _ in range(len(centroids))]
    for point in points:
        distances = [get_distance(point, centroid) for centroid in centroids]
        nearest_centroid_idx = distances.index(min(distances))
        clusters[nearest_centroid_idx].append(point)
    return clusters

def calculate_new_centroids(clusters):
    new_centroids = []
    for cluster in clusters:
        if cluster:  # Avoid division by zero for empty clusters
            mean_x = sum(point[0] for point in cluster) // len(cluster)
            mean_y = sum(point[1] for point in cluster) // len(cluster)
            new_centroids.append([mean_x, mean_y])
        else:
            new_centroids.append([0, 0])  # Fallback for empty clusters
    return new_centroids

def k_means(points, initial_centroids, iterations):
    centroids = initial_centroids
    for _ in range(iterations):
        clusters = assign_points(points, centroids)
        centroids = calculate_new_centroids(clusters)
    return centroids, clusters

def plot_clusters(initial_centroids, final_centroids, clusters):
    for cluster_idx, cluster in enumerate(clusters):
        x_coords = [p[0] for p in cluster]
        y_coords = [p[1] for p in cluster]
        plt.scatter(x_coords, y_coords, color=COLORS[cluster_idx % len(COLORS)], s=10)

    for i in range(len(initial_centroids)):
        plt.scatter(*initial_centroids[i], color='red', marker='+', label='Old centroid' if i == 0 else None)
        plt.scatter(*final_centroids[i], color='orange', marker='*', label='New centroid' if i == 0 else None)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('K-Means Clustering')
    plt.grid(True)
    plt.legend()

final_centroids, clusters = k_means(rand_clst_points, centroids_cord, 500)

plot_clusters(centroids_cord, final_centroids, clusters)

end_time = time.time()
print(f'Program time: {end_time - start_time:.2f} seconds')
plt.show()

# End of file
