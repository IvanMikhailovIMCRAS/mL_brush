import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # data = np.loadtxt("file.txt").T
    # columns = {
    #     "n": data[0],
    #     "m": data[1],
    #     "p": data[2],
    #     "X": data[3],
    #     "chi": data[4],
    #     "phi": data[5]
    # }
    # df = pd.DataFrame(columns)
    # df.to_csv('comb_brush_mean_phi.csv', encoding='utf-8', index=False, header=True)
    df = pd.read_csv("comb_brush_mean_phi.csv") 
    # print(df.head(10))
    # sns.histplot(df[['X','chi']], kde=True)
    # plt.show()
    print(df[['X','phi']].describe())
    print(df[df['phi']>0.99])
    
    corr = df[['n','m', 'p', 'X', 'chi', 'phi']].corr()
    print(corr)
    # sns.heatmap(corr, cmap="crest")
    # plt.show()