import matplotlib.pyplot as plt
import networkx as nx
import plotly.graph_objects as go

def visualize_graph(graph):
    """Статичная визуализация графа с улучшенной читаемостью."""
    plt.figure(figsize=(16, 16))  # Увеличиваем размер графа для лучшей читаемости
    
    # Используем spring_layout с увеличенным параметром k для большего расстояния между узлами
    pos = nx.spring_layout(graph, k=0.5, iterations=50)
    
    # Настройка параметров узлов и текста
    nx.draw_networkx_nodes(graph, pos, node_size=700, node_color="lightblue")  # Увеличенные узлы
    nx.draw_networkx_edges(graph, pos, width=1.0, alpha=0.7)  # Линии рёбер
    nx.draw_networkx_labels(graph, pos, font_size=12, font_color="black", font_weight="bold")  # Увеличенные метки
    
    # Добавляем отображение весов рёбер (если они есть)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10, font_color="red")
    
    plt.title("Семантическая сеть по информатике", fontsize=16)  # Заголовок графа
    plt.axis("off")  # Убираем оси
    plt.show()

def save_graph_as_html(graph, file_path):
    """Сохраняет интерактивную визуализацию графа в HTML-файл."""
    pos = nx.spring_layout(graph, k=0.5, iterations=50)  # Расположение узлов
    
    # Координаты узлов
    x_nodes = [pos[node][0] for node in graph.nodes()]
    y_nodes = [pos[node][1] for node in graph.nodes()]
    
    # Рёбра
    edge_x = []
    edge_y = []
    for edge in graph.edges(data=True):
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    # Построение рёбер
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    # Построение узлов
    node_trace = go.Scatter(
        x=x_nodes, y=y_nodes,
        mode='markers+text',
        text=list(graph.nodes()),  # Имена узлов
        textposition="top center",
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            size=10,
            colorbar=dict(
                thickness=15,
                title='Связи узлов',
                xanchor='left',
                titleside='right'
            )
        )
    )

    # Создание интерактивного графа
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title="Интерактивная семантическая сеть",
                        titlefont=dict(size=16),
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=0, l=0, r=0, t=0),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )
    
    # Сохранение графа в HTML-файл
    fig.write_html(file_path)
    print(f"Интерактивная визуализация сохранена в файл: {file_path}")

def visualize_graph_interactive(graph):
    """Интерактивная визуализация графа с Plotly."""
    pos = nx.spring_layout(graph, k=0.5, iterations=50)  # Увеличение расстояния между узлами
    
    # Координаты узлов
    x_nodes = [pos[node][0] for node in graph.nodes()]
    y_nodes = [pos[node][1] for node in graph.nodes()]
    
    # Рёбра
    edge_x = []
    edge_y = []
    for edge in graph.edges(data=True):
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    # Построение рёбер
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    # Построение узлов
    node_trace = go.Scatter(
        x=x_nodes, y=y_nodes,
        mode='markers+text',
        text=list(graph.nodes()),  # Имена узлов
        textposition="top center",
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            size=10,
            colorbar=dict(
                thickness=15,
                title='Связи узлов',
                xanchor='left',
                titleside='right'
            )
        )
    )

    # Построение интерактивного графа
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title="Интерактивная семантическая сеть",
                        titlefont=dict(size=16),
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=0, l=0, r=0, t=0),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )
    fig.show()

    # Создание графа
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title="Интерактивная семантическая сеть",
                        titlefont=dict(size=16),
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=0, l=0, r=0, t=0),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )

    fig.show()
