## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.
**Issue Type**: Off-by-one error.
**Notes**: Loop uses len(items)+1 causing IndexError when n == len(items).

## Bug 2 – bug2.py
**Intended Behavior**: Check if a string is a palindrome, ignoring spaces and case.
**Issue Type**: Logical error.
**Notes**: Strips spaces but never lowercases, so "A man a plan a canal Panama" returns False.

## Bug 3 – bug3.js
**Intended Behavior**: Calculate average of numbers and format as percentage string.
**Issue Type**: Runtime error (off-by-one + NaN propagation).
**Notes**: Loop condition i <= numbers.length accesses undefined index, producing NaN.

## Bug 4 – bug4.js
**Intended Behavior**: Find and return all duplicate values in an array.
**Issue Type**: Syntax error.
**Notes**: Missing semicolon in for loop (arr.length i++) causes SyntaxError.

## Bug 5 – bug5.py
**Intended Behavior**: Compute mean, median, stdev from a list of numeric strings.
**Issue Type**: Data type misuse.
**Notes**: statistics functions expect numbers but receive strings, causing TypeError.

## Bug 6 – bug6.c
**Intended Behavior**: Compute factorial of an integer iteratively.
**Issue Type**: Logical error (wrong loop boundary).
**Notes**: while(i < n) skips multiplying by n itself, so factorial(5) returns 24 instead of 120.
