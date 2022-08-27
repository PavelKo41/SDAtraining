"""
unittest

python -m unittest "filename.py" #esli dobavit v konce -f to do pervoj owibki budet testirovat

#from test_func import area_of_square : sozdat otdelno test_func tuda perenesti i togda tut testnut mozno

"""
import unittest


class TestSomething(unittest.TestCase):
    def test_is_equals(self):
        self.assertEqual(10, 10)  #check if a == b

    @unittest.skip("Skipping example")  #skipif mozno ispolzovat esli dobavit konkretnko s kakogo momenta skipat
    # @unittest.skipIf(sys.platform.startswith("win"), "skipping test for windows")
    def test_is_equal_fails(self):
        self.assertEqual(True, False)

    def test_not_equal(self):
        self.assertNotEqual("Yellow", "Blue")

    def test_is_in(self):
        self.assertIn(3, [7, 4, 5, 6, 3])

    def test_is_upper(self):
        txt = "name".upper()
        self.assertEqual("NAME", txt)


if __name__ == '__main__':
    unittest.main()

