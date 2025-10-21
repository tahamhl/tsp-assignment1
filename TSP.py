import random
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# 1. Adım: Rastgele Noktalar Üretme
def generate_random_points(n, x_range=(0, 100), y_range=(0, 100)):
    """
    Rastgele n adet 2D nokta üretir.
    """
    return [(random.uniform(x_range[0], x_range[1]), random.uniform(y_range[0], y_range[1])) for _ in range(n)]

# 2. Adım: Euclidean mesafesini hesaplamak
def euclidean_distance(p1, p2):
    """
    İki nokta arasındaki Euclidean mesafesini hesaplar.
    """
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# 3. Adım: NetworkX ile Grafik Oluşturma
def create_graph(points):
    """
    Noktalar arasında NetworkX grafiği oluşturur.
    """
    G = nx.Graph()
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points):
            if i < j:
                distance = euclidean_distance(p1, p2)
                G.add_edge(i, j, weight=distance)
    return G

# 4. Adım: En Yakın Komşu (Nearest Neighbor) Algoritması
def nearest_neighbor(points):
    """
    En Yakın Komşu algoritmasını uygulayarak TSP turunu bulur.
    """
    unvisited = list(range(len(points)))
    tour = []
    current = 0  # Başlangıç noktasını seçiyoruz (ilk nokta)
    tour.append(current)
    unvisited.remove(current)
    
    while unvisited:
        nearest = min(unvisited, key=lambda x: euclidean_distance(points[current], points[x]))
        tour.append(nearest)
        current = nearest
        unvisited.remove(current)
    
    # İlk noktayı son noktaya bağlayarak tam bir tur elde ederiz
    tour.append(tour[0])
    return tour

# 5. Adım: Turu Görselleştirme
def visualize_tour(points, tour):
    """
    Noktaları ve TSP turunu görselleştirir.
    """
    tour_points = [points[i] for i in tour]
    x, y = zip(*tour_points)
    
    plt.figure(figsize=(8, 6))
    plt.scatter(*zip(*points), c='blue', label='Noktalar', zorder=5)
    plt.plot(x, y, marker='o', color='red', label='TSP Turu', zorder=10)
    
    # Noktalara etiket ekleme
    for i, (x_val, y_val) in enumerate(points):
        plt.text(x_val, y_val, str(i), fontsize=9, ha='right')
    
    plt.title("TSP Çözümü - En Yakın Komşu Algoritması")
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

# 6. Adım: Ana Program
def main():
    # Adım 1: Rastgele 100 nokta üretme
    num_points = 100
    points = generate_random_points(num_points)
    
    # Adım 2: NetworkX ile grafiği oluşturma
    G = create_graph(points)
    
    # Adım 3: En Yakın Komşu algoritmasını uygulama
    tour = nearest_neighbor(points)
    
    # Adım 4: Turu görselleştirme
    visualize_tour(points, tour)

if __name__ == "__main__":
    main()
