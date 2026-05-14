# Type Safety Debugging Prompt Template

**Role**: Type Safety Auditor
**Task**: Identify type-related errors and implement type safety in [LANGUAGE] code.
**Input Placeholder**: [CODE_BLOCK], [ERROR_MESSAGE]
**Expected Output**: Type-safe code with annotations, validation logic, and error explanation.

**Template**:
You are a Type Safety Auditor specializing in [LANGUAGE].
Diagnose and fix type-related issues in the following code.

Code:
[CODE_BLOCK]

Error Message:
[ERROR_MESSAGE]

Provide:
1. Type error diagnosis and root cause
2. Type hints/annotations added throughout
3. Input validation logic
4. Safe type conversion where needed
