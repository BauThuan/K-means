import random
import math

def euclidean_distance(point1, point2):
    return math.sqrt(sum([(x - y) ** 2 for x, y in zip(point1, point2)]))

def initialize_centroids(data, k):
    return random.sample(data, k)

def assign_clusters(data, centroids):
    clusters = [[] for _ in range(len(centroids))]
    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        min_distance_index = distances.index(min(distances))
        clusters[min_distance_index].append(point)
    return clusters

def calculate_new_centroids(clusters):
    new_centroids = []
    for cluster in clusters:
        new_centroid = [sum(dim) / len(cluster) for dim in zip(*cluster)]
        new_centroids.append(new_centroid)
    return new_centroids

def kmeans(data, k, max_iterations=100, tolerance=1e-4):
    centroids = initialize_centroids(data, k)
    for _ in range(max_iterations):
        clusters = assign_clusters(data, centroids)
        new_centroids = calculate_new_centroids(clusters)
        differences = [euclidean_distance(c, nc) for c, nc in zip(centroids, new_centroids)]
        if sum(differences) <= tolerance:
            break
        centroids = new_centroids
    return centroids, clusters

# Example usage
if __name__ == "__main__":
    # Sample data: list of points (each point is a list of coordinates)
    data = [
        [1.0, 2.0], [1.5, 1.8], [5.0, 8.0],
        [8.0, 8.0], [1.0, 0.6], [9.0, 11.0],
        [8.0, 2.0], [10.0, 2.0], [9.0, 3.0]
    ]
    k = 3
    centroids, clusters = kmeans(data, k)

    print("Centroids:")
    for centroid in centroids:
        print(centroid)

    print("\nClusters:")
    for i, cluster in enumerate(clusters):
        print(f"Cluster {i + 1}:")
        for point in cluster:
            print(point)
