import pandas


def console_output(text):
    """
    Writes text provided to the console.

    Args:
        text (str): Text to write to the console.
    """
    print(text)
    return None


def write_file_python(text, path_to_file):
    """
    Writes text provided to the specified file.
    Uses only python built-in methods.

    Args:
        text (str): Text to write to the file.
        path_to_file(str): Path to the specified file.
    """
    try:
        with open(path_to_file, 'w') as file:
            file.write(text)
    except FileNotFoundError:
        print(f"File {path_to_file} not found")
    return None


def write_file_pandas(dataframe, path_to_file):
    """
    Writes dataframe provided to the specified file.
    Uses methods provided by pandas library.

    Args:
        dataframe (pandas.DataFrame): Dataframe object to write to the file.
        path_to_file(str): Path to the specified file.
    """
    try:
        dataframe.to_csv(path_to_file, index=False)
    except FileNotFoundError:
        print(f"File {path_to_file} not found")
