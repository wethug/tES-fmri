#电极和电极膏等材料信噪比的影响
import matplotlib
import matplotlib.pyplot as plt

# 感兴趣区域
x_list = ['ROI1', 'ROI2', 'ROI3', 'ROI4', 'ROI5']
# 信噪比下降/%
y1 = [6.37,	4.88, 2.89, 2.97, 0.58]
y2 = [7.02,	5.53, 3.26,	2.54, 2.16]
y3 = [8.24,	5.19, 3.19,	3.61, 0.75]
y4 = [13.45, 8.74, 11.00, 9.72, 6.39]
y5 = [10.19, 5.64, 3.08, 2.00, 2.51]
y6 = [7.08,	4.52, 2.05, 1.24, 1.79]
y7 = [48.82, 47.99, 40.41, 42.56, 34.98]
y8 = [8.39,	8.14, 9.11, 6.79, 3.53]
y9 = [7.26,	8.46, 6.04, 4.03, 0.83]
y10 = [9.92, 5.11, 8.31, 4.05, 3.61]
y11 = [6.87, .55, 9.23, 7.01, 3.98]
# 定义中文格式
font = {'family': 'MicroSoft Yahei', 'size': 10}
matplotlib.rc('font', **font)

l1, = plt.plot(range(len(y1)), y1, marker='o', markersize=3, color='blue', linewidth=1.50)
l2, = plt.plot(range(len(y2)), y2, marker='o', markersize=3, color='orange', linewidth=1.50)
l3, = plt.plot(range(len(y3)), y3, marker='o', markersize=3, color='grey', linewidth=1.50)
l4, = plt.plot(range(len(y4)), y4, marker='o', markersize=3, color='yellow', linewidth=1.50)
l5, = plt.plot(range(len(y5)), y5, marker='o', markersize=3, color='cornflowerblue', linewidth=1.50)
l6, = plt.plot(range(len(y6)), y6, marker='o', markersize=3, color='red', linewidth=1.50)
l7, = plt.plot(range(len(y7)), y7, marker='o', markersize=3, color='green', linewidth=1.50)
l8, = plt.plot(range(len(y8)), y8, marker='o', markersize=3, color='black', linewidth=1.50)
l9, = plt.plot(range(len(y9)), y9, marker='o', markersize=3, color='pink', linewidth=1.50)
l10, = plt.plot(range(len(y10)), y10, marker='o', markersize=3, color='purple', linewidth=1.50)
l11, = plt.plot(range(len(y11)), y11, marker='o', markersize=3, color='purple', linewidth=1.50)

plt.xticks(range(len(x_list)), x_list)
plt.xlabel("信号区域")

plt.ylabel("信噪比下降/%")
plt.ylim(0, 50)

plt.title('多种材料组合对水膜成像信噪比的影响')
plt.legend(handles=[l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11], labels=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'], prop=font)
#plt.legend(loc='upper left')

plt.axhline(y=8, ls=":", c="red", linewidth=2.00)#添加水平直线

plt.show()