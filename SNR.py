#不同条件的信噪比的影响
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

x = np.arange(5)
y = [650, 660, 670, 680, 690]
y1 = [640, 650, 660, 670, 680]
y2 = [630, 640, 650, 660, 670]
y3 = [620, 630, 640, 650, 660]

bar_width = 0.20
tick_label = ["ROI1", "ROI2", "ROI3", "ROI4", "ROI5"]

plt.bar(x, y, bar_width, align="center", color="c", label="A", alpha=0.5)
plt.bar(x+bar_width, y1, bar_width, color="b", align="center", label="B", alpha=0.5)
plt.bar(x+bar_width*2, y2, bar_width, color="g", align="center", label="C", alpha=0.5)
plt.bar(x+bar_width*3, y3, bar_width, color="r", align="center", label="D", alpha=0.5)

plt.xlabel("信号区域")
plt.ylabel("信噪比")
plt.ylim(0, 800)

plt.xticks(x+bar_width*3/2, tick_label)

plt.legend()

plt.show()