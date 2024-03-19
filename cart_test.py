import unittest
from cart import ShoppingCart
from product import Product


class TestShoppingCart(unittest.TestCase):
    def test_getcartTotal_empty_cart(self):
        cart = ShoppingCart()
        total = cart.getCartTotal()
        self.assertEqual(total, 0.0)
    
    def test_getCartTotal_with_product(self):
        cart = ShoppingCart()
        cart.addProdyct(Product("shirt", 20.0, 1))
        cart.addProdyct(Product("shirt2", 10.0, 2))
        total = cart.getCartTotal()
        self.assertEqual(total, 40.0)


if __name__ == '__main__':
    unittest.main()

    