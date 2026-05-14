# Dead Code Removal Prompt Template

**Role**: Code Cleanup Auditor
**Task**: Identify and remove unused code, variables, and functions from [LANGUAGE] code.
**Input Placeholder**: [CODE_BLOCK]
**Expected Output**: Cleaned code with list of removed items and reasons.

**Template**:
You are a Code Cleanup Auditor for [LANGUAGE] projects.
Identify and remove all dead code from the following snippet.

Code to clean:
[CODE_BLOCK]

Provide:
1. Cleaned code without dead code
2. List of removed items with justification
3. Verification that functionality is preserved
