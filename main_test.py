import os
import random
import numpy as np

import main


def test_t1_file_stat():
    rng = random.Random(0xDEADBEEF)

    for i, n in enumerate([2, 10, 100, 1000, 1000000]):
        path = "test_/{}.txt".format(i)
        data = np.array([int(rng.gauss(0.0, 1.0)) for _ in range(n)])
        text = "\n".join([str(x) for x in data]) + "\n"
        try:
            with open(path, "w") as f:
                f.write(text)
            r = main.t1_file_stat(path)
            print(r)

            mean = data.mean()
            cm5 = np.mean((data - mean)**5)
            eps = 1e-8
            assert abs(r["mean"] - mean) < eps
            assert abs(r["max"] - data.max()) < eps
            assert abs(r["min"] - data.min()) < eps
            assert abs(r["std_dev"] - data.std()) < eps
            assert abs(r["5th_central_moment"] - cm5) < eps
        except:
            os.remove(path)
            raise
        else:
            os.remove(path)
