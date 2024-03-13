from matplotlib import pyplot as plt

class Cluster:
    def __init__(self, points, initial_guesses):
        self.points = points
        self.means = initial_guesses
        self.k = len(initial_guesses)
        self.prev_means = sorted(initial_guesses)
    
    def compareWithPrevious(self):
        return self.means == self.prev_means
    
    def calDistance(self, point1: tuple[int, int], point2: tuple[int, int]) -> float:
        (x1, y1), (x2, y2) = point1, point2
        return pow(pow((x1-x2),2) + pow((y1-y2),2), 0.5)

    def chooseCluster(self, point: tuple[int, int]) -> int:
        distances = [self.calDistance(mean, point) for mean in self.means]
        return distances.index(min(distances))
    
    def computeMean(self, cluster: set) -> tuple[int, int]:
        x_sum = y_sum = 0
        for x, y in cluster:
            x_sum += x
            y_sum += y
        return (round(x_sum / len(cluster), 3), round(y_sum / len(cluster), 3))
        
    def getResult(self) -> list[tuple[int, int]]:
        clusters = [set() for i in range(self.k)]
        
        for point in self.points:
            clusters[self.chooseCluster(point)].add(point)
        
        self.means = sorted([self.computeMean(cluster) for cluster in clusters])
        
        if self.compareWithPrevious():
            print(clusters)
            return self.means
        else:
            self.prev_means = sorted(self.means)
            return self.getResult()

if __name__ == "__main__":
    points = [(55, 50), (43, 50), (55, 52), (43, 54), (58, 53), (41, 47), (50, 41), (50, 70)]
    initial_guesses = [(50, 41), (50, 70), (43, 50), (55, 50)]
    
    c = Cluster(points, initial_guesses)
    final_means = c.getResult()
    print(final_means)
    plt.scatter([x[0] for x in points], [x[1] for x in points], c="blue")
    plt.scatter([x[0] for x in final_means], [x[1] for x in final_means], c="red")
    plt.show()