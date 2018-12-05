import csv


# you are free to use this csv_read method, or write your own!
def csv_read(filename: str) -> list:
    """reads a csv file to a list of lists"""
    with open(filename, newline="") as csv_file:
        reader = csv.reader(csv_file)
        return [x for x in reader]


def csv_diff(file0: str, file1: str, sep: str = ",") -> dict:
    """
    this function takes two csv filenames
    returns a dict containing information on how the two csv files differ
    """

    return {
        "error": True,  # if there is a difference
        "added": [],  # list of rows added
        "removed": [],  # list of the rows removed
    }
