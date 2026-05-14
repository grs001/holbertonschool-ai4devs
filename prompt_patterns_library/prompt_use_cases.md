# Prompt Use Cases

Prompt patterns are structured approaches for requesting AI assistance in coding workflows. This document categorizes common situations where specific prompt patterns improve productivity.

---

## Code Quality

### Refactoring
- **Goal**: Improve readability and performance
- **Input**: Source function in [LANGUAGE]
- **Output**: Optimized code + explanation of improvements
- **Example**: "Refactor this Python function to be more Pythonic and reduce time complexity."

### Style Enforcement
- **Goal**: Enforce consistent naming and formatting standards
- **Input**: Code block with inconsistent style
- **Output**: Rewritten code following style guide
- **Example**: "Reformat this JavaScript code to follow Airbnb style guide."

---

## Debugging

### Error Diagnosis
- **Goal**: Identify root cause of runtime or logic errors
- **Input**: Error message + code snippet
- **Output**: Root cause analysis + suggested fixes
- **Example**: "This code throws IndexError: list index out of range. Can you identify the issue?"

### Logic Verification
- **Goal**: Trace through code logic to find bugs
- **Input**: Code and expected vs actual output
- **Output**: Step-by-step trace + bug identification
- **Example**: "Expected [30,40,50] but got IndexError. Walk through this loop logic."

### Performance Optimization
- **Goal**: Find and fix performance bottlenecks
- **Input**: Code that runs slowly
- **Output**: Identified bottlenecks + optimization suggestions
- **Example**: "Why is this O(n²) algorithm slow for large datasets? Suggest an O(n) alternative."

---

## Documentation

### Code Comments and Docstrings
- **Goal**: Add clear comments explaining code logic
- **Input**: Code without comments
- **Output**: Same code with helpful comments and docstrings
- **Example**: "Add docstrings and inline comments to this Python function."

### README and API Documentation
- **Goal**: Create user-friendly documentation
- **Input**: Code or project overview
- **Output**: Formatted documentation with examples
- **Example**: "Write a comprehensive README for this GitHub repository including setup and usage."

---

## Testing

### Test Case Generation
- **Goal**: Create comprehensive test cases covering edge cases
- **Input**: Function signature and intended behavior
- **Output**: Unit tests with various scenarios
- **Example**: "Generate pytest test cases for this function, including edge cases and error conditions."

### Test Validation and Coverage
- **Goal**: Verify tests cover intended functionality
- **Input**: Code and existing test suite
- **Output**: Analysis of coverage gaps + new test cases
- **Example**: "Are these tests sufficient? What edge cases are missing?"

### Mock and Fixture Creation
- **Goal**: Create test doubles and test data
- **Input**: Function that requires external dependencies
- **Output**: Mocks, stubs, and fixtures
- **Example**: "Create mock objects and fixtures for testing this API client."

---

## Summary

Total categories: **4**
Total use cases: **11**

| Category | Count |
|----------|-------|
| Code Quality | 2 |
| Debugging | 3 |
| Documentation | 2 |
| Testing | 3 |
| **Total** | **10** |
