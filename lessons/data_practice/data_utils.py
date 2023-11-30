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

# x: list[dict[str, str]] = [{"Comp": "110", "Bio": "100"}, {"Comp": "210", "Bio": "200"}]

# list[dict]:
# [{'Day': 'Monday', 'Low': '56', 'High': '75'}, {'Day': 'Tuesday', 'Low': '53', 'High': '72'}, {'Day': 'Wednesday', 'Low': '50', 'High': '72'}]
# list holds dict[monStats], dict[tuesStats], dict[wedStats]

# dict[list]
# Day: list[days], Low : list[lows], High: list[highs]
# {'Day': ['Monday', 'Tuesday', 'Wednesday'], 'Low': ['56', '53', '50'], 'High': ['75', '72', '72']}
def columnar(d: list[dict[str,str]]) -> dict[str, list[str, str]]:
    modified: dict[str, list[str, str]] = {}
    # within the first item (dict) in the list,
    for idx in range(0, 1):
        # take each key from that dict and append it to the new empty dict
        for key in d[1]:
            modified[key] = list(column_vals(d, key))
    
    return modified

