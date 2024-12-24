from modules.graph_builder import build_graph
from modules.visualizer import visualize_graph_interactive, save_graph_as_html
from modules.search import search_node
from modules.graph_utils import filter_edges_by_weight, find_shortest_path

NODES_FILE = "data/nodes.json"
EDGES_FILE = "data/edges.json"

def main():
    print("Загрузка графа...")
    graph = build_graph(NODES_FILE, EDGES_FILE)
    
    while True:
        print("\nВыберите действие:")
        print("1. Визуализировать граф (интерактивно)")
        print("2. Найти узел и его связи")
        print("3. Сохранить визуализацию в файл")
        print("4. Фильтровать рёбра по весу")
        print("5. Найти кратчайший путь между узлами")
        print("6. Выйти")

        choice = input("Введите номер действия: ")
        
        if choice == '1':
            visualize_graph_interactive(graph)
        elif choice == '2':
            node = input("Введите название узла: ")
            search_node(graph, node)
        elif choice == '3':
            file_path = input("Введите путь к файлу (например, graph.html): ")
            save_graph_as_html(graph, file_path)
        elif choice == '4':
            min_weight = float(input("Введите минимальный вес рёбер: "))
            filtered_graph = filter_edges_by_weight(graph, min_weight)
            print(f"Фильтрация завершена. Визуализируем граф с рёбрами весом ≥ {min_weight}.")
            visualize_graph_interactive(filtered_graph)
        elif choice == '5':
            start_node = input("Введите начальный узел: ")
            end_node = input("Введите конечный узел: ")
            find_shortest_path(graph, start_node, end_node)
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
