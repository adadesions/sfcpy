from PIL import Image
from skimage.transform import pyramid_gaussian
import numpy as np

from sfcpy import HC_TABLE_PATH


# Main Hilbert Curve Functions
def read_hc_tape(file_path, order=2):
    """
    read_hc_tape :Read Hilbert Curve command from the table

    Read Hilbert Curve command from the table in this package.
    The command including these English alphabet {'o', 'u', 'd', 'l', 'r'}

    :param file_path: a path of HC table 
    :type file_path: string
    :param order: Hilbert curve's order, defaults to 2
    :param order: int, optional
    :return: a Hilbert curve string tape
    :rtype: string
    """

    order_str = 'Order {}'.format(order)
    encoded = ''
    is_found = False

    with open(file_path, 'r') as file:
        for line in file.readlines():
            if is_found:
                encoded = line
                break

            if order_str in line:
                is_found = True

    return encoded.replace('\n', '')


def get_hc_tape(order=2):
    """
    get_hc_tape :a function that call read_hc_tape function

    The short hand version of read_hc_tape function

    :param order: Hilbert curve's order ,defaults to 2
    :param order: int, optional
    :return: Hilbert curve string tape
    :rtype: string
    """

    # FILEPATH = './sfcpy/hc_lookup.txt'
    tape = read_hc_tape(HC_TABLE_PATH, order)

    return tape


def prepare_image(img_path):
    """
    prepare_image :To prepare image for multi-resoluition analysis

    To transform image to multi-resolution by Pyramid method

    :param img_path: path of image
    :type img_path: string
    :return: list of transformed images
    :rtype: tuple
    """

    im = Image.open(img_path)
    (w, h) = im.size
    max_dim = max(w, h)
    hc_order = int(np.ceil(np.log2(max_dim)))
    n = 2**hc_order
    im = im.resize((n, n))
    pyramid = tuple(pyramid_gaussian(im))

    return pyramid[-2::-1]


# Hilber Curve functional utilities
def left(point): return (point[0]-1, point[1])


def right(point): return (point[0]+1, point[1])


def up(point): return (point[0], point[1]-1)


def down(point): return (point[0], point[1]+1)


tape_reader = {
    'u': lambda step: up(step),
    'd': lambda step: down(step),
    'l': lambda step: left(step),
    'r': lambda step: right(step),
    'o': lambda step: tuple(step),
}


if __name__ == '__main__':
    hc_tape = get_hc_tape(2)
    print(hc_tape)
