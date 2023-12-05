"""Working with CSV files."""

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read a CSV file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    # complicated type and execution so dw about it too much:
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_vals(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    # for value in list:
    for row in table:
        # append every value under key header
        result.append(row[header])
    return result

def columnar(table: list[dict[str,str]]) -> dict[str, list[str]]:
    """Reformat data so it's a dictionary with column headers as keys"""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of the table to get the headers
    first_row: dict[str,str] = table[0]
    for key in first_row:
        # for each key (header), make a dictionary entry with all the column values
        result[key] = column_vals(table, key)
    return result