import json
from csv_diff import csv_diff


COL_INSENSITIVE = False


def test_csv(
    filename: str,
    new_filename: str,
    base_dir: str = "./data/",
    should_error: bool = False,
    expected_added: int = 0,
    expected_removed: int = 0,
    debug: bool = False,
) -> None:

    info = csv_diff(
        "{}{}".format(base_dir, filename), "{}{}".format(base_dir, new_filename)
    )

    passing = False
    if (should_error and info["error"]) or (not should_error and not info["error"]):
        passing = True
    else:
        if expected_added == len(info["added"]) and expected_removed == len(
            info["removed"]
        ):
            passing = True

    print(
        "\n\n[{}] {} - {}\n{}".format(
            "PASS" if passing else "FAIL", filename, new_filename, "-" * 50
        )
    )
    if debug:
        print(json.dumps(info, sort_keys=True, indent=2))


if __name__ == "__main__":
    """run against some tests"""
    test_csv(
        "small.csv",
        "small_incorrect.csv",
        should_error=True,
        expected_added=3,
        expected_removed=3,
    )

    # should pass
    test_csv("small.csv", "small_row_unordered.csv")

    # should pass if you support column order insensitive
    # otherwise will show 5 added, 5 removed
    test_csv(
        "small.csv",
        "small_col_unordered.csv",
        should_error=not COL_INSENSITIVE,
        expected_added=5,
        expected_removed=5,
    )

    # should pass if you support column order insensitive
    # otherwise will give many added/removed
    test_csv(
        "large.csv",
        "large_col_ordered.csv",
        should_error=not COL_INSENSITIVE,
        expected_added=1000,
        expected_removed=1000,
    )

    # should have many added many removed
    test_csv(
        "large.csv",
        "large_incorrect.csv",
        should_error=True,
        expected_added=30,
        expected_removed=15,
    )
