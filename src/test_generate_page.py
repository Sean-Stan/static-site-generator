import unittest

from generate_page import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        title = extract_title("# Hello")
        result = "Hello"
        self.assertEqual(title, result)

    def test_extract_title_fail(self):
        with self.assertRaises(Exception) as context:
            extract_title(" Hello")
        self.assertEqual(str(context.exception), "No h1 header found")

if __name__ == "__main__":
    unittest.main()