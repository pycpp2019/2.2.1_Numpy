import os
import random
import numpy as np

import main

EPS = 1e-6

def test_t1_file_stat():
    print()
    rng = np.random.RandomState(0xDEADBEE1)

    for i, n in enumerate([2, 10, 100, 1000, 1000000]):
        path = "test_/{}.txt".format(i)
        data = rng.randint(-100, 100 + 1, size=n)
        text = "\n".join([str(x) for x in data]) + "\n"
        try:
            with open(path, "w") as f:
                f.write(text)
            r = main.t1_file_stat(path)
            print(r)

            mean = data.mean()
            cm5 = np.mean((data - mean)**5)
            assert abs(r["mean"] - mean) < EPS
            assert abs(r["max"] - data.max()) < EPS
            assert abs(r["min"] - data.min()) < EPS
            assert abs(r["std_dev"] - data.std()) < EPS
            assert abs(r["5th_central_moment"] - cm5) < EPS
        except:
            os.remove(path)
            raise
        else:
            os.remove(path)

def test_t2_sort_int():
    print()
    rng = np.random.RandomState(0xDEADBEE2)

    for i, n in enumerate([0, 1, 10, 100, 1000, 1000000]):
        print("len(array) == {}".format(n))
        data = rng.randint(-100, 100 + 1, size=n)
        assert all(main.t2_sort_int(data.copy()) == np.sort(data))

def test_t3_sort_complex():
    print()
    rng = np.random.RandomState(0xDEADBEE3)

    print("len(complex_array) == 0")
    data = np.array([], dtype=np.complex)
    ret = main.t3_sort_complex(data.copy())
    assert len(ret) == 2
    assert ret[0].shape == (0,) and ret[1].shape == (0,)

    print("len(complex_array) == 1")
    data = np.array([1.0 + 1.0j])
    ret = main.t3_sort_complex(data.copy())
    assert len(ret) == 2
    assert ret[0].shape == (1,) and ret[1].shape == (1,)
    assert abs(ret[0][0] - data[0]) < EPS and abs(ret[1][0] - data[0]) < EPS

    for i, n in enumerate([5, 50, 500]):
        print("len(complex_array) == {}".format(4*n**2))

        re = 100.0*rng.randn(1, n)
        im = 100.0j*rng.randn(n, 1)
        data = (re + im).reshape(-1)
        conj = data.copy()
        conj.imag = -conj.imag
        data = np.concatenate((data, -data, conj, -conj))

        ordsort = np.sort(data)
        abssort = data[np.argsort(np.abs(data))]
        rresort = np.flip(np.sort(data), axis=0)
        ref = (abssort, rresort)

        ret = main.t3_sort_complex(data.copy())
        assert len(ret) == 2
        assert ret[0].shape == (4*n**2,) and ret[1].shape == (4*n**2,)

        assert np.max(np.abs(ret[1].real - ref[1].real)) < EPS
        assert np.max(np.abs(np.sort(ret[1]) - ordsort)) < EPS

        assert np.max(np.abs(np.abs(ret[0]) - np.abs(ref[0]))) < EPS
        assert np.max(np.abs(np.sort(ret[0]) - ordsort)) < EPS

def random_words(rng, k, n):
    charset = list("abcdefghijklmnopqrstuvwxyz")
    words = np.array(["".join(rng.choice(charset, size=rng.poisson(5))) for _ in range(k)])
    return rng.choice(words, size=n)

def test_t4_sort_string_len():
    print()
    rng = np.random.RandomState(0xDEADBEE4)

    for i, (k, n) in enumerate([(1, 1), (10, 10), (10, 100), (100, 1000), (1000, 1000000)]):
        print("len(array) == {}".format(n))
        data = random_words(rng, k, n)
        nplen = np.vectorize(len)
        ret = main.t4_sort_string_len(data.copy())
        ref = data[np.argsort(nplen(data))]
        assert ret.shape == (n,)
        assert np.all(nplen(ret) == nplen(ref))
        assert np.all(np.sort(ret) == np.sort(ref))

def test_t5_sort_string_tuple():
    print()
    rng = np.random.RandomState(0xDEADBEE4)

    for i, (k, n) in enumerate([(1, 1), (10, 10), (10, 100), (100, 1000), (1000, 1000000)]):
        print("len(array) == {}".format(n))
        data = random_words(rng, k, n)
        ret = main.t5_sort_string_tuple(tuple(data))
        ref = tuple(np.sort(data))
        assert type(ret) is tuple
        assert len(ret) == n
        assert ret == ref
