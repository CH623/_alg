import random
import numpy as np
import matplotlib.pyplot as plt

# =====================
# 資料
# =====================
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# =====================
# MSE
# =====================
def mse(w, b):
    y_pred = w * x + b
    return np.mean((y - y_pred) ** 2)

# =====================
# 爬山演算法
# =====================
def hill_climbing(step=0.01, max_iter=10000):
    w = random.uniform(-5, 5)
    b = random.uniform(-5, 5)

    for _ in range(max_iter):
        current_error = mse(w, b)

        neighbors = [
            (w + step, b),
            (w - step, b),
            (w, b + step),
            (w, b - step)
        ]

        best_w, best_b = w, b
        best_error = current_error

        for nw, nb in neighbors:
            error = mse(nw, nb)
            if error < best_error:
                best_error = error
                best_w, best_b = nw, nb

        if best_error >= current_error:
            break

        w, b = best_w, best_b

    return w, b

# =====================
# 執行爬山演算法
# =====================
w, b = hill_climbing()
print(f"w = {w:.3f}, b = {b:.3f}")

# =====================
# 畫圖
# =====================
x_line = np.linspace(min(x), max(x), 100)
y_line = w * x_line + b

plt.figure()
plt.scatter(x, y)
plt.plot(x_line, y_line)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression using Hill Climbing")
plt.show()
