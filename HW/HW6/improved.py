import numpy as np
import random
import matplotlib.pyplot as plt

# ======================
# 1. 建立資料
# ======================
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# ======================
# 2. 誤差函數
# ======================
def error(w, b):
    return np.sum((y - (w * x + b)) ** 2)

# ======================
# 3. 初始化參數
# ======================
w = random.uniform(-5, 5)
b = random.uniform(-5, 5)

step = 0.05
errors = []

# ======================
# 4. 改良法主迴圈
# ======================
for _ in range(3000):
    errors.append(error(w, b))

    # 嘗試小改動
    w_new = w + random.choice([-step, step])
    b_new = b + random.choice([-step, step])

    # 只要變好就接受
    if error(w_new, b_new) < error(w, b):
        w, b = w_new, b_new

# ======================
# 5. 畫圖
# ======================
plt.figure()
plt.scatter(x, y)
plt.plot(x, w * x + b)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression by Improvement Method")
plt.show()

plt.figure()
plt.plot(errors)
plt.xlabel("Iteration")
plt.ylabel("Error")
plt.title("Error Decrease Over Time")
plt.show()

print("w =", w)
print("b =", b)
print("final error =", error(w, b))
