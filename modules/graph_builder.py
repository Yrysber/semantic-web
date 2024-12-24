import json
import networkx as nx

def build_graph(nodes_file, edges_file):
    graph = nx.Graph()
    
    # Загрузка узлов
    with open(nodes_file, 'r', encoding='utf-8') as nf:
        nodes = json.load(nf)
        nodes = [node.lower() for node in nodes]  # Приведение узлов к нижнему регистру
        graph.add_nodes_from(nodes)
    
    # Загрузка связей с обработкой отсутствующих весов
    with open(edges_file, 'r', encoding='utf-8') as ef:
        edges = json.load(ef)
        cleaned_edges = []
        for edge in edges:
            if len(edge) == 2:  # Если вес отсутствует, назначаем вес по умолчанию 1
                cleaned_edges.append((edge[0].lower(), edge[1].lower(), {"weight": 1}))
            elif len(edge) == 3:  # Вес присутствует
                cleaned_edges.append((edge[0].lower(), edge[1].lower(), {"weight": edge[2]}))
            else:
                print(f"Предупреждение: некорректная связь {edge} пропущена.")
        
        graph.add_edges_from(cleaned_edges)
    
    return graph

def save_graph(graph, file_path):
    """Сохраняет граф в файл формата GraphML."""
    nx.write_graphml(graph, file_path)
    print(f"Граф сохранён в файл: {file_path}")

def load_graph(file_path):
    """Загружает граф из файла формата GraphML."""
    graph = nx.read_graphml(file_path)
    print(f"Граф загружен из файла: {file_path}")
    return graph
