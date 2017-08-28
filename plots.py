import numpy as np
import matplotlib.pyplot as plt


def plot_wiki_scroller_input_frame():
    tlist= np.arange(0, 8001, 200) # times
    plt.title("boo yah")

    plt.subplot(211)
    plt.ylabel('Digital input pin 6')
    def f1(t):
        return not (1000 <= t < 3000 or 4000 <= t < 4600 or 5000 <= t < 7000)
    plt.step(tlist, [f1(t) for t in tlist], where='post')
    plt.annotate('short press', xy=(4300, 0.1), xytext=(2000, 0.8),
                 arrowprops=dict(facecolor='black', shrink=0.05), ha='center')
    plt.text(2000, 0.1, 'long press', ha='center')
    plt.text(6000, 0.1, 'long press', ha='center')

    plt.subplot(212)
    plt.ylabel('Accelerometer x-axis (g)')
    plt.xlabel('Time after $t_{start}$ of frame (ms)')

    def f2(t):
        return (0.5 if 3200 <= t < 3600 else 0.0)
    plt.step(tlist, [f2(t) for t in tlist], where='post')
    plt.text(1600, 0.05, 'flat', ha='center')
    plt.text(5800, 0.05, 'flat', ha='center')
    plt.annotate('right tilt', xy=(3800, 0.45), xytext=(5800, 0.45),
                 arrowprops=dict(facecolor='black', shrink=0.05), ha='center', va='center')

    plt.show()

if __name__ == "__main__":
    plot_wiki_scroller_input_frame()
