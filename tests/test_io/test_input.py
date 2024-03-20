import unittest
from app.io.input import read_file_python, read_file_pandas
from pandas import DataFrame
from pandas.errors import EmptyDataError


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

    def test_data_file_pandas(self):
        data_file_content = read_file_pandas("../../data/data_pandas.csv")
        expected = DataFrame({
            "Name": ["John", "Alice", "Bob"],
            "Age": [25, 30, 35],
            "City": ["New York", "Los Angeles", "Chicago"]
        }).to_string()
        self.assertEqual(data_file_content, expected)

    def test_nonexistent_file_pandas(self):
        data_file_content = read_file_pandas("some/nonexistent/path/data.txt")
        self.assertIsNone(data_file_content)

    def test_exception_pandas(self):
        self.assertRaises(EmptyDataError, read_file_pandas, "../../data/empty.csv")


if __name__ == "__main__":
    unittest.main()
