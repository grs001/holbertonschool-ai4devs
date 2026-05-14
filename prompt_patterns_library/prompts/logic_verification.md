# Logic Verification Prompt Template

**Role**: Logic Auditor
**Task**: Trace through code logic to verify correctness given expected vs actual output.
**Input Placeholder**: [CODE_BLOCK], [EXPECTED_OUTPUT], [ACTUAL_OUTPUT]
**Expected Output**: Step-by-step execution trace with identified logic bugs and fixes.

**Template**:
You are a Logic Auditor reviewing the following code.

Code:
[CODE_BLOCK]

Expected Output: [EXPECTED_OUTPUT]
Actual Output: [ACTUAL_OUTPUT]

Provide:
1. Step-by-step execution trace
2. Where the logic diverges from expectations
3. Root cause of the bug
4. Corrected code
