## Bug 1 – bug1.py
**Intended Behavior**: Return the last `n` items of a list as a new list.
**Issue Type**: Off-by-one error.
**Notes**: The loop range uses `len(items) + 1` as the upper bound instead of `len(items)`. This causes an `IndexError` when `n == len(items)` because the loop tries to access an index that does not exist in the list.

## Bug 2 – bug2.py
**Intended Behavior**: Check whether a string is a palindrome, ignoring spaces and letter case.
**Issue Type**: Logical error.
**Notes**: The function removes spaces but never converts the string to lowercase before comparing characters. As a result, `"A man a plan a canal Panama"` incorrectly returns `False` due to case mismatch between `'A'` and `'a'`.

## Bug 3 – bug3.js
**Intended Behavior**: Calculate the average of an array of numbers and return it formatted as a percentage string with two decimal places.
**Issue Type**: Runtime error (off-by-one loop + NaN propagation).
**Notes**: The loop condition uses `i <= numbers.length` instead of `i < numbers.length`. The last iteration accesses `numbers[numbers.length]` which is `undefined`. Adding `undefined` to the total produces `NaN`, which silently propagates into the final formatted result.

## Bug 4 – bug4.js
**Intended Behavior**: Find all duplicate values in an array and return them as a unique list.
**Issue Type**: Syntax error.
**Notes**: The `for` loop declaration is missing a semicolon between the condition and the increment expression: `arr.length i++` should be `arr.length; i++`. This causes a `SyntaxError` that prevents the entire script from executing.

## Bug 5 – bug5.py
**Intended Behavior**: Accept a list of numeric strings, compute the mean, median, and standard deviation, and print a formatted summary.
**Issue Type**: Misuse of data types / library misuse.
**Notes**: The `statistics` module functions (`mean`, `median`, `stdev`) require numeric types (`int` or `float`). The input list contains strings, which causes a `TypeError`. All values must be converted with `int()` or `float()` before being passed to these functions.

## Bug 6 – bug6.c
**Intended Behavior**: Compute the factorial of a given positive integer using an iterative loop, then print a multiplication table.
**Issue Type**: Logical error (wrong loop boundary).
**Notes**: The `while` loop condition is `i < n` instead of `i <= n`, meaning the loop exits before multiplying by `n` itself. For example, `factorial(5)` returns `24` (which equals `4!`) instead of the correct value `120`. The multiplication table function is correct and unaffected by this bug.
