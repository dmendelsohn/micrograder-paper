import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import pickle

# Saves an objec to a file
def save(obj, filename):
    f = open(filename, 'wb')
    pickle.dump(obj,f)
    f.close()

# Loads an object from a file
def load(filename):
    f = open(filename, 'rb')
    obj = pickle.load(f)
    f.close()
    return obj

def plot_wiki_scroller_input_frame():
    tlist = np.arange(0, 8001, 200) # times

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
    plt.ylabel('Accelerometer x-axis $(m/s^2)$')
    plt.xlabel('Time after $t_{start}$ of frame (ms)')

    def f2(t):
        return (5.0 if 3200 <= t < 3600 else 0.0)
    plt.step(tlist, [f2(t) for t in tlist], where='post')
    plt.text(1600, 0.5, 'flat', ha='center')
    plt.text(5800, 0.5, 'flat', ha='center')
    plt.annotate('right tilt', xy=(3800, 4.5), xytext=(5800, 4.5),
                 arrowprops=dict(facecolor='black', shrink=0.05), ha='center', va='center')

    plt.show()

def plot_button_signal():
    tlist = np.arange(0, 5001, 1000)
    plt.step(tlist, [1, 0, 1, 0, 1, 1], where='post')
    plt.ylabel('Digital value')
    plt.xlabel('Time (ms)')
    plt.show()

def plot_input_samples(where=None): # "inter", "mid", "pre", "post" or ""/None
    x = [0, 1000, 2000, 3000, 4000, 5000]
    y = [0, 2, 0, 3, 1, 2]
    if where == "inter":
        plt.plot(x, y, label="continuous signal")
    elif where:
        plt.step(x, y, where=where, label="continuous signal")
    plt.stem(x, y, linefmt=" ", markerfmt='ro', basefmt=" ", label="discrete samples")
    plt.ylabel('Analog voltage (V)')
    plt.xlabel('Time (ms)')
    plt.legend(bbox_to_anchor=(0, 1), loc='upper left', ncol=1)
    plt.show()

def plot_input_slicing(do_slice=True):
    x = [0, 1000, 2000, 3000, 4000, 5000]
    if do_slice:
        y = [2, 0, 3, 1, 1, 1]
    else:
        y = [0, 2, 0, 3, 1, 2]
    plt.step(x, y, where='post', label="continuous signal")
    plt.ylabel('Analog voltage (V)')
    plt.xlabel('Time (ms)')
    plt.show()

# Hardcoded path
def plot_acc():
    x, y = load("pickles/f1_acc")
    y = [9*elt for elt in y]

    axes = plt.gca()
    axes.set_ylim([-2.5,2.5])

    plt.plot(x,y)
    plt.xlabel('Time (ms)')
    plt.ylabel('Acceleration, x-axis (m/$s^2$)')
    plt.show()

def plot_button():
    x, y = load("pickles/f1_but")

    plt.plot(x,y)
    plt.xlabel('Time (ms)')
    plt.ylabel('Active-low digital push-button')
    plt.show()

if __name__ == "__main__":
    plot_button()
