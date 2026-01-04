import random
import math

# ==================================================
# n 維黎曼積分（遞迴）
# ==================================================
def riemann_nd(f, bounds, m=10):
    """
    n 維黎曼積分（使用遞迴，不用 n 層迴圈）
    f      : n 維函數，輸入 list
    bounds : [(a1,b1), ..., (an,bn)]
    m      : 每一維切 m 份
    """
    n = len(bounds)
    dx = [(b - a) / m for a, b in bounds]

    volume = 1
    for d in dx:
        volume *= d

    def recurse(dim, x):
        if dim == n:
            return f(x)
        a, b = bounds[dim]
        step = dx[dim]
        total = 0
        for i in range(m):
            xi = a + (i + 0.5) * step  # 中點黎曼
            total += recurse(dim + 1, x + [xi])
        return total

    return recurse(0, []) * volume


# ==================================================
# n 維蒙地卡羅積分
# ==================================================
def monte_carlo_nd(f, bounds, N=100000):
    """
    n 維蒙地卡羅積分
    f      : n 維函數
    bounds : [(a1,b1), ..., (an,bn)]
    N      : 取樣點數
    """
    n = len(bounds)

    volume = 1
    for a, b in bounds:
        volume *= (b - a)

    total = 0
    for _ in range(N):
        x = [random.uniform(a, b) for a, b in bounds]
        total += f(x)

    return volume * total / N


# ==================================================
# 測試函數（可自行更換）
# f(x1, x2, ..., xn) = x1^2 + x2^2 + ... + xn^2
# ==================================================
def f(x):
    return sum(xi ** 2 for xi in x)


# ==================================================
# 主程式
# ==================================================
if __name__ == "__main__":

    # 設定維度與積分區間
    n = 3
    bounds = [(0, 1)] * n

    # 參數
    m = 20        # 黎曼：每維切 m 份
    N = 200000    # 蒙地卡羅：取樣點數

    print(f"維度 n = {n}")
    print("積分區間 =", bounds)
    print()

    # 黎曼積分
    riemann_result = riemann_nd(f, bounds, m)
    print("黎曼積分結果：", riemann_result)

    # 蒙地卡羅積分
    mc_result = monte_carlo_nd(f, bounds, N)
    print("蒙地卡羅積分結果：", mc_result)

    # 理論值（∫0^1 x^2 dx = 1/3）
    exact = n / 3
    print("理論值：", exact)
