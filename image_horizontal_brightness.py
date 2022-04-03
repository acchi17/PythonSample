import os
import argparse
import glob
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def main(img_dirpath):
    num_fig_save = 0
    cnt_fig_save = 0
    num_row_plot = 2
    num_col_plot = 4
    i, j = 0, 0
    fig, axes = plt.subplots(num_row_plot, num_col_plot, dpi=100, figsize=(12,8))
    files = glob.glob(img_dirpath + '/*')
    num_fig_save = -1* (-len(files) // (num_row_plot * num_col_plot)) # 切り上げ
    for file in files:
        _, ext = os.path.splitext(file)
        if(ext == '.bmp'):
            #print(file)
            img = np.array(Image.open(file).convert('L'), dtype=float)
            #print(img.shape)
            #print(img)
            img /= 255
            #img = img.transpose(1, 0)
            y = np.sum(img, axis=0)
            x = np.arange(1, len(y)+1, 1)
            #print(x)
            #print(y)
            axes[i, j].plot(x, y)
            axes[i, j].set_title(os.path.basename(file))
            j += 1
            if (j >= num_col_plot):
                j = 0
                i += 1
                if(i >= num_row_plot):
                    i = 0
                    cnt_fig_save += 1
                    fig.tight_layout()
                    fig.savefig(img_dirpath + '/ResultFig' + str(cnt_fig_save) + '.png')
                    for row in axes:
                        for ele in row:
                            ele.clear()
                    # axes[0, 0].clear()
                    # axes[0, 1].clear()
                    # axes[1, 0].clear()
                    # axes[1, 1].clear()
                    
    if (num_fig_save > cnt_fig_save):
        cnt_fig_save += 1
        fig.savefig(img_dirpath + '/ResultFig' + str(cnt_fig_save) + '.png')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dirpath', type=str)
    args = parser.parse_args()

    main(args.dirpath)