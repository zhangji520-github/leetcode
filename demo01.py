"""
如果 a + b + c = 1000, 且 a^2 + b^2 = c^2, 求满足条件的 a, b, c 的值
"""

# 程序运行的时间不一样，但是运行的步骤是一致的
# 程序运行的步骤 时间频度 T
# T = 1000 * 1000 * 8
# T = 1000 * 1000 * 3

# 如果说把问题的数据规模设为n 那么时间频度 : T = n * n * 3
# T = 3*n^2 式按键复杂度 O(n^2)


import time 

start_Time = time.time() # 记录开始时间
# 法一：暴力求解
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a + b + c == 1000 and a**2 + b**2 == c**2:
#                 print(f'组合为: a={a}, b={b}, c={c}')

# end_Time = time.time() # 记录结束时间
# print(f'运行时间: {end_Time - start_Time} 秒')

# 法二：优化暴力求解
for a in range(1, 1000):
    for b in range(0, 1001):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(f'组合为: a={a}, b={b}, c={c}')
            break
end_Time = time.time()
print(f'运行时间: {end_Time - start_Time} 秒')