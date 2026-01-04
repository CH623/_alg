## Dijkstra 最短路徑演算法

Dijkstra 最短路徑演算法是一種用來解決 「單一起點 → 到其他所有點的最短路徑」 的經典演算法。


常用於：

Google Maps 導航、網路封包路由、遊戲 AI 尋路、圖論與演算法教學

##

二、問題要解決什麼？


給你：

  一張「帶權重的圖」

  一個起點 source

你要找：

  從起點出發，到「每一個節點」的最短距離

##

三、為什麼這樣做？

核心思想（貪婪法）：每一步都選擇「目前距離起點最近、且尚未確定的節點」


為什麼可以？因為邊權重不為負，一旦某節點是目前最短，就不可能再被繞路變得更短

這就是「貪婪選擇性質」

##

流程圖

```
開始
 ↓
初始化 dist[]
起點 = 0，其餘 = ∞
 ↓
將 (0, 起點) 放入 priority queue
 ↓
┌───────────────┐
│  queue 是否為空? │
└───────┬───────┘
        │否
        ↓
取出距離最小的節點 u
 ↓
是否為舊距離?
(dist[u] < 取出的距離)
 ├─是 → 忽略
 └─否
        ↓
對 u 的每個鄰居 v
 ↓
嘗試鬆弛：
dist[v] > dist[u] + w ?
 ├─是 → 更新 dist[v]，放入 queue
 └─否 → 不動作
 ↓
回到 queue 是否為空
 ↓
結束
```

##

程式碼

```
import heapq

def dijkstra(graph, start):
    """
    graph: dict
        graph[u] = [(v, weight), ...]
    start: 起點
    """

    # 初始化距離
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    # 優先佇列 (距離, 節點)
    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        # 如果這個距離不是最新的，就跳過
        if current_dist > dist[u]:
            continue

        # 檢查鄰居
        for v, weight in graph[u]:
            new_dist = dist[u] + weight

            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

result = dijkstra(graph, 'A')
print(result)

```

輸出結果

```
{'A': 0, 'B': 1, 'C': 3, 'D': 4}

```

關鍵概念：鬆弛（Relaxation）

```
if dist[v] > dist[u] + weight:
    dist[v] = dist[u] + weight
```

意思是：

「我是不是可以經過 u，走一條更短的路到 v？」

這是最短路徑演算法的核心操作

##

為什麼不能有負權重？

如果有負邊，已經「確定最短」的節點可能之後被負邊繞路變更短

##

## Dijkstra 重點總結

Dijkstra 最短路徑演算法透過「每次選擇目前距離最小的節點」與「鬆弛操作」，在非負權重圖中，逐步將節點從「未確定」轉為「已確定」，最終得到從起點到所有節點的最短路徑。

##

[AI對話](https://chatgpt.com/share/6959e472-ccb0-8012-8b92-114652e624e5)
