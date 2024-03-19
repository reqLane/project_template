import pandas


def console_input():
    """
    Asks the user for text input from console and returns it as a string.

    Returns:
        str. The input user provided.
    """
    user_input = input("Please enter your text: ")
    return user_input


def read_file_python(path_to_file):
    """
    Reads content of the specified file and returns it as a string.
    Uses only python built-in methods.

    Args:
        path_to_file(str): Path to the file to be read.

    Returns:
        str. The content of the specified file.
    """
    try:
        with open(path_to_file, 'r') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print(f"File \"{path_to_file}\" not found")
        return None


def read_file_pandas(path_to_file):
    """
    Reads content of the specified csv file and returns it as text.
    Uses methods provided by pandas library.

    Args:
        path_to_file(str): Path to the file to be read.

    Returns:
        str. The content of the specified file.
    """
    try:
        data = pandas.read_csv(path_to_file)
        return data.to_string()
    except FileNotFoundError:
        print(f"File \"{path_to_file}\" not found")
        return None
