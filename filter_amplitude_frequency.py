# 滤波器幅频特性
import matplotlib
import matplotlib.pyplot as plt

# 频率(Hz)
x_list = ['10', '100', '10K', '12.64K', '20K', '50K', '100K', '500K', '1M']
# 20lg(Vo/Vi)/dB
y1 = [0, 0, -2.6, -3.57, -6.13, -13.46, -20.58, -40.4, -52.57]
y2 = [0, 0, -3.12, -3.87, -6.58, -13.89, -21.62, -43.68, -55.35]
y3 = [0, 0, -2.96, -3.98, -6.84, -14.16, -21.62, -44.7, -56.96]
y4 = [0, 0, -3.32, -4.29, -6.93, -14.43, -21.69, -45.34, -55.19]
y5 = [0, 0, -3.34, -4.25, -6.97, -15.11, -22.44, -45.85, -56.94]

# 定义中文格式
font = {'family': 'MicroSoft Yahei', 'size': 10}
matplotlib.rc('font', **font)

l1, = plt.plot(range(len(y1)), y1, marker='o', markersize=4, color='blue', linewidth=0.75)
l2, = plt.plot(range(len(y2)), y2, marker='o', markersize=4, color='orange', linewidth=0.75)
l3, = plt.plot(range(len(y3)), y3, marker='o', markersize=4, color='grey', linewidth=0.75)
l4, = plt.plot(range(len(y4)), y4, marker='o', markersize=4, color='yellow', linewidth=0.75)
l5, = plt.plot(range(len(y5)), y5, marker='o', markersize=4, color='cornflowerblue', linewidth=0.75)

plt.xticks(range(len(x_list)), x_list)
plt.xlabel("频率/Hz")

plt.ylabel("20lg(Vo/Vi)/dB")

plt.title('滤波器幅频特性')
plt.legend(handles=[l1, l2, l3, l4, l5], labels=['2V', '5V', '10V', '15V', '20V'], prop=font)

# 添加水平虚线
plt.axhline(y=-3, ls=":", c="red")
# 添加垂直虚线
plt.axvline(x=3, ls=":", c="red")

plt.show()
