# Bug Descriptions

Overview: This document describes buggy code snippets in Python, JavaScript, and C, outlining the intended behavior, issue type, and detailed notes for each bug.

---

## Bug 1 – bug1.py

### Intended Behavior
Return the last `n` items of a list. For example, `last_n_items([10, 20, 30, 40, 50], 3)` should return `[30, 40, 50]`.

### Issue Type
Off-by-one error.

### Notes
The loop uses `range(len(items) - n, len(items) + 1)` which goes one index too far. When `n == len(items)`, the loop attempts to access `items[len(items)]`, which does not exist, raising an `IndexError`.

---

## Bug 2 – bug2.py

### Intended Behavior
Return `True` if a string is a palindrome, ignoring spaces and letter case. For example, `is_palindrome("A man a plan a canal Panama")` should return `True`.

### Issue Type
Logical error.

### Notes
The function strips spaces but never calls `.lower()` on the cleaned string. This causes uppercase and lowercase characters to be treated as different, so valid mixed-case palindromes incorrectly return `False`.

---

## Bug 3 – bug3.js

### Intended Behavior
Calculate the average of a number array and return a formatted string like `"Average score: 86.60%"`. An empty array should return `"Average score: 0.00%"`.

### Issue Type
Runtime error.

### Notes
The loop condition is `i <= numbers.length` instead of `i < numbers.length`. The last iteration reads `numbers[numbers.length]` which is `undefined`. Adding `undefined` to a number produces `NaN`, which silently corrupts the result.

---

## Bug 4 – bug4.js

### Intended Behavior
Return a unique list of all values that appear more than once in an array. For example, `findDuplicates([1, 2, 3, 2, 4, 3, 5, 1])` should return `[2, 3, 1]`.

### Issue Type
Syntax error.

### Steps to Reproduce
1. Save the file as `bug4.js`.
2. Run it with: `node bug4.js`
3. Observe that Node.js throws a `SyntaxError` before executing any code.

### Notes
The for loop is written as `i < arr.length i++` with no semicolon between the condition and increment. This is invalid JavaScript syntax and throws a `SyntaxError` at parse time, preventing the script from running.

---

## Bug 5 – bug5.py

### Intended Behavior
Accept a list of numeric strings, then compute and print the mean, median, and standard deviation formatted to two decimal places.

### Issue Type
Misuse of data types.

### Notes
The `statistics.mean()`, `statistics.median()`, and `statistics.stdev()` functions require numeric types. The input list contains strings like `"12"` and `"45"`. Passing them directly raises a `TypeError`. Each element must be converted with `int()` or `float()` before calling these functions.

---

## Bug 6 – bug6.c

### Intended Behavior
Compute the factorial of a positive integer iteratively and print a multiplication table. For example, `factorial(5)` should return `120`, `factorial(1)` should return `1`, and `print_table(3)` should print a correct 3×3 multiplication grid.

### Issue Type
Logical error (wrong loop boundary).

### Notes
The loop condition is `while (i < n)` instead of `while (i <= n)`. The loop exits before multiplying by `n` itself, so `factorial(5)` returns `24` (equal to `4!`) instead of the correct value `120`. The `print_table` function is correct and unaffected by this bug.
