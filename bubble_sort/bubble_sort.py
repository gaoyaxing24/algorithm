# coding: utf-8
#!/usr/bin/env python
"""
    created by: Gao YaXing
    created on: 17/4/20
"""
from __future__ import print_function


def bubble_sort(vl):
    """自己写的冒泡算法
     不知道逻辑是否符合冒泡, 但是可以得到正确的排序结果
     时间复杂度 O(n^2)
     空间复杂度O(1)  Python较为特殊, 如果不使用xrange而使用range, 则空间复杂度将指数提升O(n^2)
     timeit 3次测试结果: (41.5 + 41.8 + 47.2) / 3
    """
    global count
    length = len(vl)
    for i in xrange(length):
        # 倒序
        # for j in range(i, length):
        # 正序
        for j in xrange(0, i):
            count += 1  # 此处耗费时间不计
            if vl[i] < vl[j]:
                vl[i], vl[j] = vl[j], vl[i]

# 计算器, 看排序用了多少次
count = 0
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  更容易debug 算法逻辑
vl = range(10, 0, -1)

print("not sort: ", vl)
bubble_sort(vl)
print("sorted: ", vl)

print("loops %s time" % count)
