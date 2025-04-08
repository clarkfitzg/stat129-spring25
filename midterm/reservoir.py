from random import randrange, sample, shuffle
import unittest


def rsample(stream, size=10):
    """
    BROKEN!!!

    Produce a simple random sample with `size` elements from `stream`
    using reservoir sampling, without collecting stream into memory
    """
    res = []
    n = 0
    for x in stream:
        n = n + 1
        if n < size:
            res.append(x)
        else:
            coinflip = sample([True, False], 1)
            if coinflip:
                dice = randrange(size)
                res[dice] = x

    shuffle(res)
    return res


if __name__ == "__main__":
    import sys
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--lines", default=10,
        help="number of random lines to sample",
        type=int)

    args = parser.parse_args()
    s = rsample(sys.stdin, args.lines)
    for x in s:
        print(x, end = "")


class rsampleTest(unittest.TestCase):
    
    def test_defaults(self):
        g = (i**2 for i in range(20))
        s = rsample(g)
        self.assertEqual(len(s), 10)
        
    def test_too_small_input(self):
        d = range(5)
        s = rsample(d)
        self.assertEqual(set(s), set(d))

    def test_string(self):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        s = rsample(letters, 26)
        self.assertEqual(set(s), set(letters))

    #-------------------------------------------------------------
    # Following tests *should* pass with high probability ;)
    #-------------------------------------------------------------

    def test_permutation(self):
        n = 100
        d = range(n)
        s = rsample(d, n)
        self.assertEqual(len(s), n)
        self.assertNotEqual(s, list(d))

    def test_not_begin(self):
        n = int(1e6)
        d = range(n)
        s = rsample(d)
        self.assertTrue(1000 < max(s))

    def test_not_end(self):
        n = int(1e6)
        d = range(n)
        s = rsample(d)
        self.assertTrue(min(s) < (n - 1000))
