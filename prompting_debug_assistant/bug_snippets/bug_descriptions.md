# Bug Descriptions

This document describes the intended behavior and known issues for each buggy code snippet in the bug_snippets directory. Snippets are written in Python, JavaScript, and C, and cover a range of common programming errors.

## Table of Contents
- [Bug 1 – bug1.py](#bug-1--bug1py)
- [Bug 2 – bug2.py](#bug-2--bug2py)
- [Bug 3 – bug3.js](#bug-3--bug3js)
- [Bug 4 – bug4.js](#bug-4--bug4js)
- [Bug 5 – bug5.py](#bug-5--bug5py)
- [Bug 6 – bug6.c](#bug-6--bug6c)

---

## Bug 1 – bug1.py

### Intended Behavior
Return the last n items of a list. For example, `last_n_items([10,20,30,40,50], 3)` should return `[30, 40, 50]`.

### Issue Type
Off-by-one error.

### Notes
The loop uses `range(len(items) - n, len(items) + 1)` instead of `range(len(items) - n, len(items))`. When `n == len(items)`, the loop attempts to access `items[5]` on a 5-element list, which raises an `IndexError: list index out of range`.

---

## Bug 2 – bug2.py

### Intended Behavior
Return `True` if a string is a palindrome, ignoring spaces and letter case. For example, `is_palindrome("A man a plan a canal Panama")` should return `True`.

### Issue Type
Logical error.

### Notes
The function strips spaces but never calls `.lower()` before comparing characters. This causes `'A'` and `'a'` to be treated as different characters, so valid mixed-case palindromes incorrectly return `False`.

---

## Bug 3 – bug3.js

### Intended Behavior
Calculate the average of an array of numbers and return a string such as `"Average score: 86.60%"`. An empty array should return `"Average score: 0.00%"`.

### Issue Type
Runtime error.

### Notes
The loop condition is `i <= numbers.length` instead of `i < numbers.length`. On the final iteration, `numbers[numbers.length]` is `undefined`. Adding `undefined` to a number produces `NaN`, which propagates silently and causes `.toFixed(2)` to return `"NaN"` instead of the expected value.

---

## Bug 4 – bug4.js

### Intended Behavior
Scan an array and return a new array of values that appear more than once, without repetition. For example, `[1,2,3,2,4,3,5,1]` should return `[2, 3, 1]`.

### Issue Type
Syntax error.

### Notes
The `for` loop is written as `for (let i = 0; i < arr.length i++)`, missing the semicolon between `arr.length` and `i++`. This causes a `SyntaxError` at parse time, preventing the entire script from running.

---

## Bug 5 – bug5.py

### Intended Behavior
Accept a list of numeric strings, compute the mean, median, and standard deviation, and print each value formatted to two decimal places.

### Issue Type
Misuse of data types.

### Notes
The `statistics.mean()`, `statistics.median()`, and `statistics.stdev()` functions require numeric types. The input list contains strings like `"12"` and `"45"`. Passing them directly raises a `TypeError`. Each element must be converted with `int()` or `float()` before calling these functions.

---

## Bug 6 – bug6.c

### Intended Behavior
Compute the factorial of a positive integer iteratively. For example, `factorial(5)` should return `120` and `factorial(1)` should return `1`.

### Issue Type
Logical error (wrong loop boundary).

### Notes
The loop condition is `while (i < n)` instead of `while (i <= n)`. The loop exits before multiplying by `n` itself. As a result, `factorial(5)` returns `24` (equal to `4!`) instead of the correct value `120`. The multiplication table function is unaffected.
