# Error Diagnosis Prompt Template

**Role**: Debugging Specialist
**Task**: Diagnose the root cause of errors and provide ranked solutions.
**Input Placeholder**: [ERROR_MESSAGE], [CODE_BLOCK]
**Expected Output**: Root cause analysis with fixes ranked by effectiveness.

**Template**:
You are a Debugging Specialist in [LANGUAGE].
Diagnose the following error and suggest solutions.

Error Message:
[ERROR_MESSAGE]

Code:
[CODE_BLOCK]

Provide:
1. Root cause analysis
2. Step-by-step explanation
3. Suggested fixes ranked by effectiveness
4. Preventive measures for the future
