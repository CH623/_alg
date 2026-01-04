import numpy as np
import matplotlib.pyplot as plt

# 資料
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# 誤差函數
def mse(w, b):
    return np.sum((y - (w * x + b)) ** 2)

# 初始化
w, b = 0.0, 0.0
delta = 0.01
history = []

# 貪婪迭代
for _ in range(5000):
    current_error = mse(w, b)

    candidates = [
        (w + delta, b),
        (w - delta, b),
        (w, b + delta),
        (w, b - delta)
    ]

    # 選局部最佳
    best_w, best_b = w, b
    best_error = current_error

    for cw, cb in candidates:
        e = mse(cw, cb)
        if e < best_error:
            best_error = e
            best_w, best_b = cw, cb

    if best_error < current_error:
        w, b = best_w, best_b
        history.append(best_error)
    else:
        break

print(f"w = {w:.3f}, b = {b:.3f}")

plt.scatter(x, y)
plt.plot(x, w * x + b)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Greedy Linear Regression")
plt.show()
