import numpy as np
import scipy as sp
import pandas as pd
import h5py
from matplotlib import pyplot as plt

from scipy.io import loadmat

def excel2panda(filepath):
    df = pd.read_excel(filepath, index_col=0, true_values=['x'])
    TFdf = df.notna()
    TFdf.head()
    return(TFdf)


def image_viewing_mat_to_dict(filename):
    mat_data = loadmat(filename)
    data = dict()
    vecdata = dict()
    # monkey name
    data['monkey'] = mat_data['monkey'][0]
    # Recording start time
    data['time'] = mat_data['time'][0]
    # Recording end time
    data['date'] = mat_data['date'][0]

    # image trial number
    data['image_trl'] = mat_data['image_data'][:, 0]
    # image idx (corresponds to image_name)
    data['image_idx'] = mat_data['image_data'][:, 1]
    # session (sometimes there are brakes in image viewing)
    data['image_session'] = mat_data['image_data'][:, 2]
    # is this image a repeat?
    data['image_is_repeat'] = mat_data['image_data'][:, 3]

    # Ordinal fixation stats
    # data['fix_stats'] = pd.DataFrame(imdata['fix_stats'],
                                     #columns=['fixation_num', 'image_trial', 'prev_sac', 'next_sac', 'start_tme',
                                      #       'end_tme', 'x_center', 'y_center'])
    # Ordinal saccade stats
    #data['sac_stats'] = pd.DataFrame(imdata['sac_stats'],
                                     #columns=['saccade_num', 'image_trial', 'prev_fix', 'next_fix', 'start_tme',
                                      #        'end_tme', 'magnitude', 'angle'])

    # eyedata (upsampled)
    data['eyepos'] = mat_data['eyepos']

    # neuralynx timestamp
    data['tme'] = mat_data['tme'][0]
    # trial index
    data['trlidx'] = mat_data['trlidx'][0]
    # saccade index
    data['sac'] = mat_data['sac'][0]
    # image names
    data['image_names'] = mat_data['image_names'][0]
    # fixation index
    data['fix'] = mat_data['fix'][0]
    # Was the monkey blinking? (binary, may be broken)
    data['blink'] = mat_data['blink'][0]

    return data


if __name__ == '__main__':
    TFImageDF = excel2panda('C:\\Users\Paige\\Documents\ImageViewingPaige\\SQList_ImageCategories.xlsx')
    print(TFImageDF.head())
    file1= image_viewing_mat_to_dict("C:\\Users\\Paige\\Documents\\ImageViewingPaige\\ImageTrialsData\\ImageTrials_GR_2019-09-12_09-57-19.mat")
    fig = 2
    plt.figure()
    eye = file1['eyepos'][0, fig]
    plt.plot(eye[:, 0], eye[:, 1])
    plt.show()