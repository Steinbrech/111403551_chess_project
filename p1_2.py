# -*- coding: utf-8 -*-
"""P1_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h2y5sE8l8R37HD909UgQPwcQF_P61RrO
"""

checkerboard =[ [1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0] ]

origin = input().split()
move = input().split()
x1, y1 = int(origin[0]), int(origin[1])
x2, y2 = int(move[0]), int(move[1])

# 檢查是否停在原地
if (x1, y1) == (x2, y2):
    print("No")
    exit()

# 檢查目標位置是否超出範圍或有棋子
if x2 < 0 or x2 > 7 or y2 < 0 or y2 > 7 or checkerboard[x2][y2] == 1:
    print("No")
    exit()

# 檢查移動規則
if x1 == x2:  # 縱向移動
    for y in range(min(y1, y2) + 1, max(y1, y2)):
        if checkerboard[x1][y] == 1:
            print("No")
            exit()
elif y1 == y2:  # 橫向移動
    for x in range(min(x1, x2) + 1, max(x1, x2)):
        if checkerboard[x][y1] == 1:
            print("No")
            exit()
elif abs(x2 - x1) == abs(y2 - y1):  # 對角線移動
    step_x = 1 if x2 > x1 else -1
    step_y = 1 if y2 > y1 else -1
    x, y = x1 + step_x, y1 + step_y
    while x != x2 and y != y2:
        if checkerboard[x][y] == 1:
            print("No")
            exit()
        x += step_x
        y += step_y
else:
    print("No")
    exit()

print("Yes")