def search_node(graph, start_node):
    start_node = start_node.lower()  # Приводим ввод пользователя к нижнему регистру
    if start_node not in graph:
        print("Узел не найден в сети.")
        return

    print(f"Связанные понятия с '{start_node}':")
    for neighbor in graph.neighbors(start_node):
        print(f"- {neighbor}")
