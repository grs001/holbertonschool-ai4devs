# Bug Descriptions

This document describes the intended behavior and known issues for each buggy code snippet in the bug_snippets directory. Snippets are written in Python, JavaScript, and C, and cover a range of common programming errors.

## Table of Contents
- [Bug 1 – bug1.py](#bug-1--bug1py)
- [Bug 2 – bug2.py](#bug-2--bug2py)
- [Bug 3 – bug3.js](#bug-3--bug3js)
- [Bug 4 – bug4.js](#bug-4--bug4js)
- [Bug 5 – bug5.py](#bug-5--bug5py)
- [Bug 6 – bug6.c](#bug-6--bug6c)

## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.
**Issue Type**: Off-by-one error.
**Notes**: The function fails when n == len(items) because the loop range exceeds the list boundary, raising an IndexError.

## Bug 2 – bug2.py
**Intended Behavior**: Return True if a string is a palindrome, ignoring spaces and case.
**Issue Type**: Logical error.
**Notes**: The function fails on mixed-case inputs because it never lowercases the string before comparing characters.

## Bug 3 – bug3.js
**Intended Behavior**: Return the average of a number array formatted as a percentage string.
**Issue Type**: Runtime error.
**Notes**: The loop runs one index too far, accessing undefined, which causes NaN to propagate into the result.

## Bug 4 – bug4.js
**Intended Behavior**: Return a list of all duplicate values found in an array.
**Issue Type**: Syntax error.
**Notes**: The for loop is missing a semicolon before the increment, causing a SyntaxError that prevents execution.

## Bug 5 – bug5.py
**Intended Behavior**: Compute and print mean, median, and standard deviation from a list of numeric strings.
**Issue Type**: Misuse of data types.
**Notes**: The function passes raw strings to statistics functions which require numeric types, raising a TypeError.

## Bug 6 – bug6.c
**Intended Behavior**: Compute the factorial of a given integer using an iterative loop.
**Issue Type**: Logical error.
**Notes**: The loop condition uses i < n instead of i <= n, so the function skips multiplying by n and returns a wrong result.
