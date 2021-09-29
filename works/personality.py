import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def make_result(data):
    img_back = Image.open('static/images/plt_axis.png')
    img_back = img_back.convert('RGB')
    img_back = np.array(img_back)
    img_back = np.flipud(img_back)
    plt.figure(figsize=(5, 3))
    plt.imshow(img_back)
    plt.scatter(data[0], data[1], s=50)
    plt.xlim(-20, 1300)
    plt.ylim(-20, 740)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.tick_params(labelbottom=False,
                    labelleft=False,
                    labelright=False,
                    labeltop=False)
    plt.tick_params(bottom=False,
                    left=False,
                    right=False,
                    top=False)


def normalize(data):
    data[0] /= 3.11708
    data[1] /= 2.47097
    data[0] = 1280 * (data[0] + 1) / 2
    data[1] = 720 * (data[1] + 1) / 2
    return data


if __name__ == '__main__':
    data = normalize(np.array([1., -1.]))
    make_result(data)
    plt.show()
