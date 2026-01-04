import numpy as np
import math

# 定義基礎函數
def softmax(logits):
    exp_logits = np.exp(logits - np.max(logits)) # 減去 max 是為了數值穩定性
    return exp_logits / np.sum(exp_logits)

def cross_entropy(p, q):
    # 加上一個極小值 1e-15 避免 log(0)
    return -np.sum(p * np.log2(q + 1e-15))

def entropy(p):
    return -np.sum(p * np.log2(p + 1e-15))

# --- 設定參數 ---
p = np.array([1/2, 1/4, 1/4])
target_entropy = entropy(p)

print(f"目標 Entropy(p): {target_entropy:.6f}")
print(f"目標最佳 q 分佈: {p}")
print("-" * 30)

# --- 初始化 ---
# 我們隨機初始化 logits (z)，而不是直接初始化 q
# 這樣 q 一開始會是隨機的合法分佈
np.random.seed(42)
logits = np.random.randn(len(p)) 

learning_rate = 0.1
iterations = 1000

# --- 優化迴圈 (Gradient Descent) ---
for i in range(iterations):
    # 1. 前向傳播 (Forward): 從 logits 算出 q
    q = softmax(logits)
    
    # 2. 計算損失 (Loss)
    loss = cross_entropy(p, q)
    
    # 3. 計算梯度 (Gradient)
    # 這是數學推導後的結果： dL/dz = (q - p) / ln(2)
    # 這裡的梯度是針對 logits 的
    gradient = (q - p) / np.log(2)
    
    # 4. 更新參數 (Update Logits)
    logits = logits - learning_rate * gradient
    
    if i % 200 == 0:
        print(f"Iter {i:4d} | Loss: {loss:.6f} | q: {np.round(q, 4)}")

print("-" * 30)
final_q = softmax(logits)
print(f"最終優化結果 q: {np.round(final_q, 4)}")
print(f"最終 Cross Entropy: {cross_entropy(p, final_q):.6f}")

# --- 驗證 ---
tolerance = 1e-4
is_optimal = np.allclose(final_q, p, atol=tolerance)
is_min_loss = np.isclose(cross_entropy(p, final_q), target_entropy, atol=tolerance)

print(f"\n驗證結果:")
print(f"1. q 是否收斂至 p? -> {'是 (Yes)' if is_optimal else '否 (No)'}")
print(f"2. Cross Entropy 是否降至 Entropy? -> {'是 (Yes)' if is_min_loss else '否 (No)'}")
