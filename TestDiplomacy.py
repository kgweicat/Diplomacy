
# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Diplomacy import diplomacy_read, diplomacy_print, diplomacy_solve

# -----------
# TestCollatz
# -----------


class TestDiplomacy (TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        s = "A Madrid Hold"
        i, j, k = diplomacy_read(s)
        self.assertEqual(i, "A")
        self.assertEqual(j, "Madrid")
        self.assertEqual(k, "Hold")

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        diplomacy_print(w, "A [dead]\nB Madrid\nC London")
        self.assertEqual(w.getvalue(), "A [dead]\nB Madrid\nC London")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO(
            "A Madrid Hold\nB Barcelona Move Madrid\nC London Support B")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB Madrid\nC London")

    def test_solve2(self):
        r = StringIO("A Madrid Hold")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A Madrid")

    def test_solve3(self):
        r = StringIO(
            "A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\nE Austin Support A")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB [dead]\nC [dead]\nD Paris\nE Austin")

# ----
# main
# ----


if __name__ == "__main__":
    main()

""" #pragma: no cover
$ coverage run --branch TestCollatz.py >  TestCollatz.out 2>&1


$ cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK


$ coverage report -m                   >> TestCollatz.out



$ cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          12      0      2      0   100%
TestCollatz.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""
