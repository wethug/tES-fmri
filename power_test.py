#功耗测试
import matplotlib
import matplotlib.pyplot as plt

# 电流(mA)
x_list = ['0.1', '0.2', '0.5', '0.8', '1.0', '1.2', '1.5', '1.8', '2.0', '2.5']
# 功耗(W)
y1 = [3.687, 3.697, 3.681, 3.688, 3.688, 3.699, 3.699, 3.710, 3.721, 3.721]
y2 = [3.677, 3.691, 3.691, 3.691, 3.691, 3.691, 3.713, 3.713, 3.720, 3.739]
y3 = [3.675, 3.672, 3.691, 3.673, 3.676, 3.673, 3.684, 3.695, 3.706, 3.725]
y4 = [3.672, 3.672, 3.672, 3.683, 3.694, 3.694, 3.694, 3.724, 3.724, 3.746]
y5 = [3.686, 3.683, 3.686, 3.687, 3.698, 3.709, 3.709, 3.732, 3.750, 3.772]
y6 = [3.680, 3.680, 3.691, 3.691, 3.691, 3.691, 3.713, 3.724, 3.735, 3.779]
y7 = [3.691, 3.687, 3.687, 3.687, 3.698, 3.709, 3.728, 3.739, 3.761, 3.791]
y8 = [3.681, 3.681, 3.681, 3.681, 3.703, 3.714, 3.714, 3.755, 3.777, 3.807]
y9 = [3.695, 3.696, 3.704, 3.704, 3.720, 3.742, 3.753, 3.805, 3.827, 3.915]
y10 = [3.687, 3.680, 3.687, 3.702, 3.721, 3.743, 3.773, 3.818, 3.851, 3.970]
# 定义中文格式
font = {'family': 'MicroSoft Yahei', 'size': 10}
matplotlib.rc('font', **font)

l1, = plt.plot(range(len(y1)), y1, marker='o', markersize=3, color='blue', linewidth=1.2)
l2, = plt.plot(range(len(y2)), y2, marker='o', markersize=3, color='orange', linewidth=1.2)
l3, = plt.plot(range(len(y3)), y3, marker='o', markersize=3, color='grey', linewidth=1.2)
l4, = plt.plot(range(len(y4)), y4, marker='o', markersize=3, color='yellow', linewidth=1.2)
l5, = plt.plot(range(len(y5)), y5, marker='o', markersize=3, color='cornflowerblue', linewidth=1.2)
l6, = plt.plot(range(len(y6)), y6, marker='o', markersize=3, color='red', linewidth=1.2)
l7, = plt.plot(range(len(y7)), y7, marker='o', markersize=3, color='green', linewidth=1.2)
l8, = plt.plot(range(len(y8)), y8, marker='o', markersize=3, color='black', linewidth=1.2)
l9, = plt.plot(range(len(y9)), y9, marker='o', markersize=3, color='pink', linewidth=1.2)
l10, = plt.plot(range(len(y10)), y10, marker='o', markersize=3, color='purple', linewidth=1.2)

plt.xticks(range(len(x_list)), x_list)
plt.xlabel("电流/(mA)")

plt.ylabel("功耗/W")
#plt.ylim(3.500, 4.000)

plt.title('不同负载功耗测试')
plt.legend(handles=[l1, l2, l3, l4, l5, l6, l7, l8, l9, l10], labels=['3KΩ', '4.3KΩ', '5.1KΩ', '6.2KΩ', '7.5KΩ', '8.2KΩ', '9.1KΩ', '10KΩ', '15KΩ', '18KΩ'], prop=font)

plt.show()