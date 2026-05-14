## Bug 1 – bug1.py
**Intended Behavior**: Return the last `n` items of a list as a new list. For example, `last_n_items([10,20,30,40,50], 3)` should return `[30, 40, 50]`.
**Issue Type**: Off-by-one error.
**Notes**: The loop uses `range(len(items) - n, len(items) + 1)` instead of `range(len(items) - n, len(items))`. When `n == len(items)`, the loop accesses `items[len(items)]` which does not exist, raising an `IndexError`.

## Bug 2 – bug2.py
**Intended Behavior**: Check whether a string is a palindrome, ignoring letter case and spaces. For example, `is_palindrome("A man a plan a canal Panama")` should return `True`.
**Issue Type**: Logical error.
**Notes**: The function strips spaces but never calls `.lower()` on the cleaned string before comparing characters. This causes uppercase and lowercase versions of the same letter to be treated as different, so mixed-case palindromes incorrectly return `False`.

## Bug 3 – bug3.js
**Intended Behavior**: Calculate the average of an array of numbers and return a formatted string such as `"Average score: 86.60%"`. For an empty array, return `"Average score: 0.00%"`.
**Issue Type**: Runtime error.
**Notes**: The loop condition is `i <= numbers.length` instead of `i < numbers.length`. On the final iteration, `numbers[numbers.length]` is `undefined`. Adding `undefined` to a number produces `NaN`, which silently corrupts the result and causes `.toFixed(2)` to return `"NaN"` instead of the expected value.

## Bug 4 – bug4.js
**Intended Behavior**: Scan an array and return a new array containing only the values that appear more than once, with no duplicates in the output. For example, `[1,2,3,2,4,3,5,1]` should return `[2, 3, 1]`.
**Issue Type**: Syntax error.
**Notes**: The `for` loop is written as `for (let i = 0; i < arr.length i++)`, missing the semicolon between `arr.length` and `i++`. This is invalid JavaScript syntax and throws a `SyntaxError` at parse time, preventing the entire script from running.

## Bug 5 – bug5.py
**Intended Behavior**: Accept a list of numeric strings read from a CSV, convert them to numbers, and print the mean, median, and standard deviation formatted to two decimal places.
**Issue Type**: Misuse of data types / library misuse.
**Notes**: The raw input list contains strings such as `"12"` and `"45"`. The `statistics.mean()`, `statistics.median()`, and `statistics.stdev()` functions require numeric types (`int` or `float`). Passing strings directly raises a `TypeError`. Each element must be converted using `int()` or `float()` before calling these functions.

## Bug 6 – bug6.c
**Intended Behavior**: Compute the factorial of a positive integer using an iterative loop. For example, `factorial(5)` should return `120`, and `factorial(1)` should return `1`.
**Issue Type**: Logical error (wrong loop boundary).
**Notes**: The loop condition is `while (i < n)` instead of `while (i <= n)`. This causes the loop to exit before multiplying by `n` itself. As a result, `factorial(5)` returns `24` (equal to `4!`) instead of `120`. The multiplication table function is correct and is not affected by this bug.
