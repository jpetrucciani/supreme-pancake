import csv


def csv_read(filename: str) -> list:
    """reads a csv file to a list of lists"""
    with open(filename, newline="") as csv_file:
        reader = csv.reader(csv_file)
        return [x for x in reader]


def csv_diff(file0: str, file1: str) -> dict:
    """
    this function takes two csv filenames
    returns a dict containing information on how the two csv files differ
    """
    rows_added = []
    rows_removed = []

    return {
        "error": rows_added or rows_removed,  # if there is a difference
        "added": rows_added,  # list of rows added
        "removed": rows_removed,  # list of the rows removed
    }
