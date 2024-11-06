import numpy as np
from sfbox_api import barbwire

def calc(n: int, m: int, p: int, X: float, chi: float) -> float:
    n_layers = 1 +  m * p + max(n, m)
    theta = (1 +  m * p + m) * X
    frame = barbwire(p=p, n=n, m=m, q=1, root=m, theta=theta, chi=chi, n_layers=n_layers, geometry='flat')
    frame.run()
    phi = frame.profile['pol']
    return np.sum(phi**2) / np.sum(phi)

if __name__ == '__main__':
    n = 50
    m = 3
    p = 30
    X = 0.3
    chi = 0.5
    x_vals = np.arange(2, 16, 2)
    phi_vals = []
    # f = open('file.txt', 'w')
    # f.close()
    # for X in [0.01, 0.05, 0.1, 0.2, 0.4, 0.8]:
    for X in [0.03, 0.07, 0.3, 0.5, 0.6, 0.7]:
        for m in [3, 5, 7, 9, 11, 16]:
        # for m in [2, 4, 6, 8, 10, 12]:
            # for n in [2, 4, 8, 16, 32, 64]:
            for n in [5, 15, 25, 40, 55, 75]:
                for p in [5, 10, 15, 20, 30, 40]:
                    for chi in [0.0, 0.2, 0.35, 0.5, 0.7, 1.0]:
                        try:
                            phi_mean = calc(n, m, p, X, chi)
                            phi_vals.append(phi_mean)
                            with open('file.txt', 'r+') as f:
                                f.seek(0, 2)
                                f.write(f"{n} {m} {p} {X} {chi} {phi_mean} \n")
                            print(f"{n} {m} {p} {X} {chi} {phi_mean} - OK!")
                        except TimeoutError:
                            print(f"{n} {m} {p} {X} {chi} {phi_mean} - Error!")
