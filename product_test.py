import unittest
from product import Product

class TestProduct(unittest.TestCase):
    def test_calculateTotal_posetive(self):
        product = Product("T-shirt", 10.0, 2)
        total = product.calculateTotal()
        self.assertEqual(total, 20.0)

    def test_calucltateTotal_zero_quantity(self):
        product = Product("T-shirt", 10.0, 0)
        total = product.calculateTotal()
        self.assertEqual(total, 0.0)

    def test_calucltateTotal_negative_quantity(self):
        product = Product("T-shirt", 10.0, -1)
        with self.assertRaises(ValueError):
            total = product.calculateTotal()



if __name__ == "__main__":
    unittest.main()