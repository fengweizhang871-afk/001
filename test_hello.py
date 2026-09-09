import unittest

from hello import hello


class HelloTestCase(unittest.TestCase):
    def test_default_greeting(self) -> None:
        self.assertEqual(hello(), "Hello, World!")

    def test_custom_name(self) -> None:
        self.assertEqual(hello("Python"), "Hello, Python!")


if __name__ == "__main__":
    unittest.main()
