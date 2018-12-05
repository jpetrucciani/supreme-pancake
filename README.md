# supreme-pancake

csv diff function

## requirements
- python3.5 +


The goal of this problem is to implement the `csv_diff` function in `csv_diff.py`. This function takes two csv file names and needs to return a dict of some information about what is different between the two csv files.


*You can use any python libraries you'd like outside of `csvdiff` or any similar library*


### The basic implementation of this method should assume
- we only care about added/removed rows, and whether or not the diff has an `error` (meaning the two files differ)
- column order is consistent (however two tests have out of order columns)
- columns are the same between the two files
- row order doesn't matter
- the inputs are always a csv (separated by commas ",")


*Modified rows should show as a removed row (the initial state of the row) and an added row (the new modified version of the row).*


## further improvements to implement
- allow for different types of separator for the csv files
- return columns that are missing/added if the columns don't match
- allow for column order to be ignored
- allow for ensuring that row order is enforced
- handle duplicate rows when checking (ensure that the row is duplicated the same number of times)
- optionally return rows as dicts (column name: row value) instead of lists/tuples


## running the tests

```bash
python3 test.py
```
