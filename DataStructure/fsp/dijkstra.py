from collections import defaultdict

class FindShortestPath:
    def __init__(self):
        print("Dijkstra")
        self.graph = defaultdict(dict)

    def load_data(self, filename):
        print("load_data ...", filename)
        # 파일에서 데이터를 읽어와 그래프를 초기화하는 로직을 추가합니다.
        # 예를 들어, 파일을 열고 데이터를 읽어와 그래프를 생성하는 코드를 작성합니다.
        with open(filename, 'r') as f:
            for line in f:
                parts = line.split()
                if len(parts) == 3:
                    src, dest, weight = parts
                    if src.isdigit() and dest.isdigit() and weight.isdigit():
                        src = int(src)
                        dest = int(dest)
                        weight = int(weight)
                        self.graph[src][dest] = weight

    def initialize(self):
        print("initialize ...")
        # 초기화 작업을 수행하는 코드를 추가합니다.
        # 예를 들어, 시작 노드의 거리를 0으로 설정하고 나머지 노드의 거리를 무한대로 초기화하는 등의 작업을 수행합니다.
        self.distances = {}
        self.previous = {}
        for node in self.graph:
            self.distances[node] = float('inf')
            self.previous[node] = None
    
    def find_path(self, r):
        print("find_path ...")
        self.distances[r] = 0
        unvisited = set(self.graph.keys())

        while unvisited:
            current = min(unvisited, key=lambda node: self.distances[node])
            unvisited.remove(current)

            for neighbor in self.graph[current]:
                distance = self.distances[current] + self.graph[current][neighbor]
                if distance < self.distances[neighbor]:
                    self.distances[neighbor] = distance
                    self.previous[neighbor] = current
    
    def print_path(self, r):
        print("print_path ...")
        print("[ 순서 ]: 전체경로 : 가중치")
        for node in self.graph:
            path = self.get_path(r, node)
            distance = self.distances[node]
            print(f"[ {node} ]: {' => '.join(str(n) for n in path)} : {distance}")

    def get_path(self, start, end):
        path = []
        current = end
        while current != start:
            path.insert(0, current)
            current = self.previous[current]
        path.insert(0, start)
        return path