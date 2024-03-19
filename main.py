from app.io.input import console_input, read_file_python, read_file_pandas
from app.io.output import console_output, write_file_python, write_file_pandas


def main():
    console_text = console_input()
    file_text_python = read_file_python("data/data_python.txt")
    file_text_pandas = read_file_pandas("data/data_pandas.csv")
    console_output(console_text)
    console_output(file_text_python)
    console_output(file_text_pandas)
    write_file_python(console_text, "data/console_file.txt")
    write_file_python(file_text_python, "data/python_file.txt")
    write_file_python(file_text_pandas, "data/pandas_file.txt")


if __name__ == '__main__':
    main()
