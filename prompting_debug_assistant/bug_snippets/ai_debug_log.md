# AI Debug Log

## Bug 1 – bug1.py
**AI Diagnosis**: The loop uses `range(len(items) - n, len(items) + 1)` which exceeds the list boundary. When `n == len(items)`, it tries to access an index beyond the list, raising `IndexError: list index out of range`.
**Suggested Fix**: Use Python slicing instead: `return items[-n:] if n > 0 else []`
**Alternative Fixes Tested**: None needed.
**Result**: Fix works as expected.

## Bug 2 – bug2.py
**AI Diagnosis**: The function removes spaces but never converts to lowercase. When comparing `'A'` with `'a'`, they are treated as different characters, so mixed-case palindromes incorrectly return `False`.
**Suggested Fix**: Add `.lower()` after removing spaces: `cleaned = s.replace(" ", "").lower()`
**Alternative Fixes Tested**: None needed.
**Result**: Fix works as expected.

## Bug 3 – bug3.js
**AI Diagnosis**: Loop condition `i <= numbers.length` accesses one index too far. When accessing `numbers[5]` on a 5-element array, the result is `undefined`. Adding `undefined` produces `NaN`, corrupting the calculation.
**Suggested Fix**: Change loop condition to `i < numbers.length` and add empty array check: `if (numbers.length === 0) return 0;`
**Alternative Fixes Tested**: None needed.
**Result**: Fix works as expected.

## Bug 4 – bug4.js
**AI Diagnosis**: The for loop syntax is invalid: `i < arr.length i++` is missing a semicolon between the condition and increment. This causes a `SyntaxError` at parse time.
**Suggested Fix**: Add semicolon: `for (let i = 0; i < arr.length; i++)`
**Alternative Fixes Tested**: None needed.
**Result**: Fix works as expected.

## Bug 5 – bug5.py
**AI Diagnosis**: The `statistics` module functions require numeric types. The input list contains strings, which causes `TypeError: unsupported operand type(s)`.
**Suggested Fix**: Convert strings to integers before processing: `data = [int(x) for x in data]`. Also add check for `stdev()` which requires at least 2 values.
**Alternative Fixes Tested**: Using `float()` instead of `int()` also works.
**Result**: Fix works as expected.

## Bug 6 – bug6.c
**AI Diagnosis**: The loop condition `while (i < n)` exits before multiplying by `n` itself. For `factorial(5)`, the loop computes 1×2×3×4 = 24, not 1×2×3×4×5 = 120.
**Suggested Fix**: Change loop to `for (int i = 1; i <= n; i++)` with `result *= i;`
**Alternative Fixes Tested**: Using `while (i <= n)` with `i++` also works.
**Result**: Fix works as expected.
