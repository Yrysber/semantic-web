import networkx as nx

def filter_edges_by_weight(graph, min_weight):
    """
    Возвращает новый граф, содержащий только рёбра с весом >= min_weight.
    """
    filtered_graph = nx.Graph()
    for u, v, data in graph.edges(data=True):
        if data.get('weight', 0) >= min_weight:
            filtered_graph.add_edge(u, v, weight=data['weight'])
    return filtered_graph

def find_shortest_path(graph, start_node, end_node):
    """
    Находит кратчайший путь между двумя узлами с использованием алгоритма Дейкстры.
    """
    start_node = start_node.lower()
    end_node = end_node.lower()
    
    if start_node not in graph or end_node not in graph:
        print("Один из узлов не найден в графе.")
        return
    
    try:
        path = nx.shortest_path(graph, source=start_node, target=end_node, weight='weight')
        length = nx.shortest_path_length(graph, source=start_node, target=end_node, weight='weight')
        print(f"Кратчайший путь от '{start_node}' до '{end_node}':")
        print(" -> ".join(path))
        print(f"Длина пути: {length}")
    except nx.NetworkXNoPath:
        print(f"Путь между '{start_node}' и '{end_node}' не существует.")
