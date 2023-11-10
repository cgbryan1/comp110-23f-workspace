"""Testing dictionary.py functionality, EX07."""

__author__ = "730657997"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


def test_invert1() -> None:
    """Use case 1, using unique last names."""
    first_last: dict[str, str] = {"Caroline": "Bryan", "Catie": "Ginther", "Talia": "Sices"}
    assert invert(first_last) == {"Bryan": "Caroline", "Ginther": "Catie", "Sices": "Talia"}


def test_invert2() -> None:
    """Use case 2, testing a dictionary with a single key-value pair."""
    first_last: dict[str, str] = {"Caroline": "Bryan"}
    last_first: dict[str, str] = {"Bryan": "Caroline"}
    assert invert(first_last) == last_first


def test_invert3() -> None:
    """Use case 3 - if same last names, the function is programmed to raise a KeyError with a custom message."""
    """Could also be an edge case? I wasn't sure which this one would qualify as, sorry!"""  
    with pytest.raises(KeyError):
        first_last: dict[str, str] = {"Caroline": "Bryan", "Jennifer": "Medley", "Morgan": "Bryan"}
        invert(first_last)


def test_invert4() -> None:
    """Edge case, testing an empty dictionary."""
    first_last: dict[str, str] = {}
    last_first: dict[str, str] = {}
    assert invert(first_last) == last_first


def test_fav_color1() -> None:
    """Use case 1, should return first color because there are equal appearances."""
    fav_colors: dict[str, str] = {"Caroline": "Red", "Jennifer": "Blue", "Noa": "Purple"}
    assert favorite_color(fav_colors) == "Red"


def test_fav_color2() -> None:
    """Use case 2, should return most popular color."""
    fav_colors: dict[str, str] = {"Caroline": "Red", "Jennifer": "Blue", "Noa": "Red"}
    assert favorite_color(fav_colors) == "Red"


def test_fav_color3() -> None:
    """Edge case, testing that function returns an empty list."""
    fav_colors: dict[int, str] = {"": ""}
    assert favorite_color(fav_colors) == ""


def test_fav_color4() -> None:
    """Just for fun - seeing if it wouold work with ints!"""
    fav_colors: dict[int, int] = {1: 2}
    assert favorite_color(fav_colors) == 2


def test_count1() -> None:
    """Use case 1, uses expected list with multiple of each key."""
    pets: list[str] = ["dog", "cat", "dog", "fish", "hamster", "hamster", "dog", "cat", "dog", "fish", "hamster"]
    result: dict[str, int] = {"dog": 4, "cat": 2, "fish": 2, "hamster": 3}
    assert count(pets) == result


def test_count2() -> None:
    """Use case 2, only one value for each key."""
    pets: list[str] = ["dog", "cat", "fish", "hamster"]
    result: dict[str, int] = {"dog": 1, "cat": 1, "fish": 1, "hamster": 1}
    assert count(pets) == result


def test_count3() -> None:
    """Edge case using an empty dictionary."""
    test_list: list[str] = list()
    expected_result: dict[str, int] = {}
    assert count(test_list) == expected_result


def test_alpha1() -> None:
    """Use case 1, using different names."""
    names: list[str] = ["caroline", "catie", "anna", "avery", "noa", "zoe", "zoe", "hannah"]
    c: list[str] = ["caroline", "catie"]
    a: list[str] = ["anna", "avery"]
    n: list[str] = ["noa"]
    z: list[str] = ["zoe", "zoe"]
    h: list[str] = ["hannah"]

    alphabetized: dict[str, list[str]] = {"a": a, "c": c, "h": h, "n": n, "z": z}
    assert alphabetizer(names) == alphabetized


def test_alpha2() -> None:
    """Use case 2, testing different capitalizations."""
    names: list[str] = ["Caroline", "catie", "anna", "Avery", "Zoey", "Zoe", "zoe", "Andie"]
    c: list[str] = ["Caroline", "catie"]
    a: list[str] = ["anna", "Avery", "Andie"]
    z: list[str] = ["Zoey", "Zoe", "zoe"]
    alphabetized: dict[str, list[str]] = {"a": a, "c": c, "z": z}
    assert alphabetizer(names) == alphabetized


def test_alpha3() -> None:
    """Edge case, using a list of ints instead of strings."""
    with pytest.raises(TypeError):
        names: list[str] = [1, 2, 3, 2]
        alphabetizer(names)


def test_attend1() -> None:
    """Use case 1, adding a student to an empty list."""
    names1: list[str] = ["Anna"]
    names2: list[str] = list()
    names3: list[str] = ["Toby", "Peter"]
    names4: list[str] = list()
    names5: list[str] = ["Linus"]
    names6: list[str] = ["Andie", "Noa"]
    names7: list[str] = ["Keith"]
    roster: dict[str, list[str]] = {"Monday": names1, "Tuesday": names2, "Wednesday": names3, "Thursday": names4, "Friday": names5, "Saturday": names6, "Sunday": names7}
    update_attendance(roster, "Tuesday", "Elizabeth")
    assert roster["Tuesday"] == ["Elizabeth"]


def test_attend2() -> None:
    """Use case 2, adding a student to an existing list."""
    names1: list[str] = list()
    names2: list[str] = ["Anna", "Robert"]
    names3: list[str] = ["Toby", "Peter"]
    names4: list[str] = list()
    names5: list[str] = ["Linus"]
    roster: dict[str, list[str]] = {"Monday": names1, "Tuesday": names2, "Wednesday": names3, "Thursday": names4, "Friday": names5}
    update_attendance(roster, "Tuesday", "Elizabeth")
    assert roster["Tuesday"] == ["Anna", "Robert", "Elizabeth"]


def test_attend3() -> None:
    """Use case 3, trying to assign a student to a day not in the roster."""
    # Program says: {'Saturday': ['Elizabeth']} != {'Saturday': 'Elizabeth'}
    # Why don't both save as lists? Is it an ish w my og program?
    names1: list[str] = list()
    names2: list[str] = ["Anna", "Robert"]
    names3: list[str] = ["Toby", "Peter"]
    names4: list[str] = list()
    names5: list[str] = ["Linus"]
    roster: dict[str, list[str]] = {"Monday": names1, "Tuesday": names2, "Wednesday": names3, "Thursday": names4, "Friday": names5}
    update_attendance(roster, "Saturday", "Elizabeth")
    names6: list[str] = ["Elizabeth"]
    assert roster == {"Monday": names1, "Tuesday": names2, "Wednesday": names3, "Thursday": names4, "Friday": names5, "Saturday": names6}


def test_attend4() -> None:
    """Use case 4, trying to double mark a student present."""
    names1: list[str] = ["Anna", "Robert"]
    names2: list[str] = ["Toby", "Peter"]
    roster: dict[str, list[str]] = {"Monday": names1, "Tuesday": names2}
    update_attendance(roster, "Monday", "Anna")
    assert roster == {"Monday": names1, "Tuesday": names2}


def test_attend5() -> None:
    """Edge test using an empty dictionary."""
    names: list[str] = list()
    roster: dict[str, list[str]] = {}
    update_attendance(roster, "Monday", names)
