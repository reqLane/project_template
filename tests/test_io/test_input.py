import unittest
from app.io.input import read_file_python, read_file_pandas
from pandas import DataFrame


class ReadFilePythonTests(unittest.TestCase):
    def test_data_file_python(self):
        data_file_content = read_file_python("../../data/data_python.txt")
        self.assertEqual(data_file_content, "This is text\n"
                                            + "which is here\n"
                                            + "hello\n\n\n"
                                            + "THIS IS FOR ---PYTHON--- functions\n")

    def test_nonexistent_file_python(self):
        data_file_content = read_file_python("some/nonexistent/path/data.txt")
        self.assertIsNone(data_file_content)

    def test_exception_python(self):
        self.assertRaises(TypeError, read_file_python, ["../../data/data_python.txt"])


if __name__ == "__main__":
    unittest.main()
