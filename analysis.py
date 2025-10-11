from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
import utils as ut
import numpy as np
vm = 'value_millions'

drop_list = [vm, 'link', 'Player_id', 'nationality', 'position', 'team', 'age',
            'games', 'games_starts', 'minutes', 'minutes_90s',
            'games_complete', 'games_subs', 'unused_subs']


def compute_pca(data, year, out_type, dim=3, min_min=0):
    
    data = data[data['minutes'] > min_min]

    names = data['Name']

    if vm in data.columns:
        cd = data.drop(drop_list, axis=1)
    else:  # 2025 doesn't have vm appended
        cd = data.drop(drop_list[1:], axis=1)


    pda = cd.drop(['Name'], axis=1)

    pca = PCA(n_components=dim)
    x = pca.fit_transform(pda)
    pca.fit(pda)

    mi = [np.abs(pca.components_[i]).argmax() for i in range(pca.components_.shape[0])]
    col = list(data.columns)
    nam = [col[mi[i]] for i in range(pca.components_.shape[0])]
    # print(pca.components_)
    print(pca.explained_variance_)
    print(pca.explained_variance_ratio_)
    print(nam)
    dic = {
        'names': names,
        'x': x[:,0],
        'y': x[:,1]
        # 'z': x[:,2]
    }

    locs = pd.DataFrame(dic)
    total = pd.merge(data, locs, left_on="Name", right_on="names")
    plot_pca(x)
    # ut.save_locs(total, f'./pca_data/{year-1}-{year}-{'full' if min_min == 0 else str(min_min)}-{dim}D-pca', out_type)

def plot_pca(x):  
    fig = plt.figure(1, figsize=(8,6))
    ax = fig.add_subplot(111)

    scatter = ax.scatter(
        x[:,0],
        x[:,1]
        # x[:,2]
        )

    plt.show()


def compute_pos_pca(data, pos):

    # gone = [i for i, row in data.iterrows() if row['position'] == pos]
    # print(gone)
    # data = data.drop(gone, axis=0)
    data = data[data['position'] == pos]
    compute_pca(data)