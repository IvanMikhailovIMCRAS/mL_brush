import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = np.loadtxt("file.txt").T
    X = data[3]
    chi = data[4]
    new_chi = 1 / (2 + X) * (np.tanh(chi-0.5) + 1 + X)
    rev_eta = (1 + data[0] / data[1])**(-1)
    columns = {
        "rev_eta": rev_eta,
        "rev_p": 1 / data[2],
        "X": data[3],
        "new_chi": new_chi,
        "phi": data[5]        
    }
    df = pd.DataFrame(columns)
    df.to_csv('comb_brush_mean_phi.csv', encoding='utf-8', index=False, header=True)
    df = pd.read_csv("comb_brush_mean_phi.csv") 
    print(df.head(10))
    sns.histplot(df[['rev_eta','new_chi']], kde=True)
    plt.show()
    print(df[['X','phi']].describe())
    print(df[df['phi']>0.99])
    
    # corr = df[['rev_eta', 'rev_p', 'X', 'new_chi', 'phi']].corr(method="spearman")
    # print(corr)
    # sns.heatmap(corr, cmap="crest")
    # plt.show()