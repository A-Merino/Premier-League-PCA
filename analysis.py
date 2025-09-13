from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
import utils as ut
vm = 'value_millions'

drop_list = [vm, 'link', 'Player_id', 'nationality', 'position', 'team', 'age',
            'games', 'games_starts', 'minutes', 'minutes_90s',
            'games_complete', 'games_subs', 'unused_subs']


def compute_pca(data, year):
    names = data['Name']

    if vm in data.columns:
        data = data.drop(drop_list, axis=1)
    else:  # 2025 doesn't have vm appended
        data = data.drop(drop_list[1:], axis=1)


    data = data.drop(['Name'], axis=1)

    pca = PCA(n_components=3)
    x = pca.fit_transform(data)

    dic = {
        'names': names,
        'x': x[:,0],
        'y': x[:,1],
        'z': x[:,2]
    }

    locs = pd.DataFrame(dic)
    ut.save_locs(locs, f'./pca_data/{year-1}-{year}full-pca.csv')

def plot_pca(x):  
    fig = plt.figure(1, figsize=(8,6))
    ax = fig.add_subplot(111, projection="3d")

    scatter = ax.scatter(
        x[:,0],
        x[:,1],
        x[:,2]
        )
    for i, txt in enumerate(names):
        ax.text(x[i,0],x[i,1],x[i,2], txt)

    plt.show()


def compute_pos_pca(data, pos):

    # gone = [i for i, row in data.iterrows() if row['position'] == pos]
    # print(gone)
    # data = data.drop(gone, axis=0)
    data = data[data['position'] == pos]
    compute_pca(data)