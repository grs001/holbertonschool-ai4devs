# Prompt Use Cases

Prompt patterns are structured approaches to requesting AI assistance for coding tasks. This document categorizes common use cases where specific prompt patterns improve coding workflows.

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

### Code Simplification
- **Goal**: Reduce complexity and improve maintainability
- **Input**: Complex nested logic or redundant code
- **Output**: Simplified equivalent code
- **Example**: "Simplify this nested if-else statement into a switch or ternary operator."

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

### Performance Bottleneck Identification
- **Goal**: Find performance issues in code
- **Input**: Code that runs slowly
- **Output**: Identified bottlenecks + optimization suggestions
- **Example**: "Why is this O(n²) algorithm slow for large datasets?"

---

## Documentation

### Code Comment Generation
- **Goal**: Add clear, concise comments explaining code logic
- **Input**: Code without comments
- **Output**: Same code with helpful comments
- **Example**: "Add docstrings and inline comments to this Python function."

### README and API Documentation
- **Goal**: Create user-friendly documentation
- **Input**: Code or project overview
- **Output**: Formatted documentation with examples
- **Example**: "Write a comprehensive README for this GitHub repository."

### Technical Specification Writing
- **Goal**: Document system design and architecture
- **Input**: Project description or code structure
- **Output**: Formal technical specification
- **Example**: "Create a technical specification document for this database schema."

---

## Testing

### Test Case Generation
- **Goal**: Create comprehensive test cases covering edge cases
- **Input**: Function signature and intended behavior
- **Output**: Unit tests with various scenarios
- **Example**: "Generate pytest test cases for this function, including edge cases and error conditions."

### Test Validation
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

## Security and Best Practices

### Vulnerability Identification
- **Goal**: Identify potential security issues
- **Input**: Code that handles user input or sensitive data
- **Output**: Vulnerability list + remediation steps
- **Example**: "Does this code have SQL injection vulnerabilities?"

### Best Practice Review
- **Goal**: Ensure code follows industry standards
- **Input**: Code snippet
- **Output**: Analysis of compliance + recommendations
- **Example**: "Review this error handling code against Python PEP 8 and exception best practices."

### Type Safety and Validation
- **Goal**: Improve type checking and input validation
- **Input**: Code with weak typing or missing validation
- **Output**: Improved code with type hints and validators
- **Example**: "Add type hints and input validation to this Python function."

---

## API and Integration

### API Integration Assistance
- **Goal**: Help implement API calls and data parsing
- **Input**: API documentation + desired functionality
- **Output**: Implementation code + error handling
- **Example**: "Show me how to call the GitHub API and parse the JSON response in Python."

### Data Structure Conversion
- **Goal**: Transform data between formats
- **Input**: Current data format + desired format
- **Output**: Conversion code
- **Example**: "Convert this CSV data into a JSON structure."

### Error Handling Patterns
- **Goal**: Implement robust error handling
- **Input**: Code with minimal or no error handling
- **Output**: Code with comprehensive try-catch and recovery logic
- **Example**: "Add proper error handling and retry logic to this API client."

---

## Summary

| Category | Use Cases | Total |
|----------|-----------|-------|
| Code Quality | 3 | 3 |
| Debugging | 3 | 3 |
| Documentation | 3 | 3 |
| Testing | 3 | 3 |
| Security & Best Practices | 3 | 3 |
| API & Integration | 3 | 3 |
| **Total** | | **18** |

Each use case represents a common pattern where AI assistance accelerates development, improves code quality, and reduces debugging time.
