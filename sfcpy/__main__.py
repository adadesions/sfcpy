from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

from sfcpy.hilbert import get_hc_tape, prepare_image, tape_reader
from sfcpy.data import data


if __name__ == '__main__':
    imgs, tapes = [], []
    FILE_PATH = data("brain_cancer.jpg")

    original_image = Image.open(FILE_PATH)
    fig, ax = plt.subplots()
    ax.imshow(original_image, cmap='gray')
    nrows, ncols = 3, 3
    axes_num = nrows*ncols

    path, val = [], []
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    highest_order = axes_num+1

    imgs = prepare_image(FILE_PATH)
    for order in range(highest_order-axes_num, highest_order+1):
        tape = get_hc_tape(order)
        tapes.append(tape)

    for i, tape in enumerate(tapes):
        val_temp = []
        p_step = [0, 0]
        for t in tape:
            t_step = tape_reader[t](p_step)

            if t_step[0] < xlim[0] or t_step[0] > xlim[1]: break
            if t_step[1] < ylim[1] or t_step[1] > ylim[0]: break

            n_step = t_step[::]
            p_step = n_step[::]

            path.append(n_step)
            try:
                val_temp.append(imgs[i][n_step])
            except IndexError:
                continue
        val.append(val_temp)

    print('tape len:', len(tapes))
    print('imgs len:', len(imgs))
    fig1, ax1 = plt.subplots(nrows=nrows, ncols=ncols)
    count_val = 0

    for i in range(nrows):
        for j in range(ncols):
            order_str = 'Order {}'.format(highest_order-axes_num+count_val)
            ax1[i, j].set(title=order_str)
            ax1[i, j].plot(val[count_val], color='red', linewidth=3)
            count_val += 1

    print(tapes[1])
    plt.show()
