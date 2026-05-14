# Bug Descriptions

Overview: This document lists buggy code snippets in Python, JavaScript, and C, describing the intended behavior, issue type, and notes for each.

---

## Bug 1 – bug1.py
### Intended Behavior
Return the last n items of a list. For example, last_n_items([10,20,30,40,50], 3) should return [30, 40, 50].
### Issue Type
Off-by-one error.
### Notes
The loop uses range(len(items) - n, len(items) + 1) which goes one step too far. When n == len(items), it accesses an index that does not exist, raising an IndexError.

---

## Bug 2 – bug2.py
### Intended Behavior
Return True if a string is a palindrome, ignoring spaces and letter case. For example, is_palindrome("A man a plan a canal Panama") should return True.
### Issue Type
Logical error.
### Notes
The function strips spaces but never calls .lower(). So 'A' and 'a' are treated as different characters, causing valid mixed-case palindromes to incorrectly return False.

---

## Bug 3 – bug3.js
### Intended Behavior
Calculate the average of a number array and return a formatted string like "Average score: 86.60%". An empty array should return "Average score: 0.00%".
### Issue Type
Runtime error.
### Notes
The loop condition is i <= numbers.length instead of i < numbers.length. The last iteration reads numbers[numbers.length] which is undefined. This corrupts the total with NaN, producing a wrong result.

---

## Bug 4 – bug4.js
### Intended Behavior
Return a unique list of all values that appear more than once in an array. For example, findDuplicates([1,2,3,2,4,3,5,1]) should return [2, 3, 1].
### Issue Type
Syntax error.
### Steps to Reproduce
1. Save the file as bug4.js.
2. Run it with: node bug4.js
3. Observe that Node.js throws a SyntaxError before executing any code.
### Notes
The for loop is written as i < arr.length i++ with no semicolon between them. This is invalid JavaScript syntax and throws a SyntaxError at parse time, preventing the script from running at all.

---

## Bug 5 – bug5.py
### Intended Behavior
Accept a list of numeric strings, then compute and print the mean, median, and standard deviation formatted to two decimal places.
### Issue Type
Misuse of data types.
### Notes
The statistics functions require int or float values. The input list contains strings like "12" and "45". Passing them directly raises a TypeError. Values must be converted with int() or float() first.

---

## Bug 6 – bug6.c
### Intended Behavior
Compute the factorial of a positive integer iteratively and print a multiplication table. For example, factorial(5) should return 120, factorial(1) should return 1, and print_table(3) should print a correct 3x3 multiplication grid.
### Issue Type
Logical error (wrong loop boundary).
### Notes
The loop condition is while (i < n) instead of while (i <= n). The loop exits before multiplying by n itself, so factorial(5) returns 24 (equal to 4!) instead of the correct value 120. The print_table function is correct and unaffected by this bug.
