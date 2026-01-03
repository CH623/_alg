n = 15

# 方法 1
def power2n(n):
    return 2**n

print("1.",power2n(n))

# 方法 2a：用遞迴
def power2n2(n):
    if n == 0:
        return 1
    return power2n2(n-1)+power2n2(n-1)

print("2a.",power2n2(n))

# 方法2b：用遞迴
def power2n3(n):
    if n == 0:
        return 1
    return 2*power2n3(n-1)

print("2b.",power2n3(n))

# 方法 3：用遞迴+查表

pow2 = [None]*10000
pow2[0] = 1

def power2n4(n):
    if pow2[n] is not None: 
        return pow2[n]
    pow2[n] = power2n4(n-1)+power2n4(n-1)
    return pow2[n]

print("4.",power2n4(n))
