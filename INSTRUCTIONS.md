# PR Review Instructions for GitHub Copilot

## Overview
This document provides guidelines for GitHub Copilot to conduct comprehensive code reviews on pull requests for the **Akash-Agent** DevOps project.

## Review Checklist

### 1. Code Quality
- [ ] **Code Style & Formatting**: Verify consistent indentation, naming conventions, and formatting standards
- [ ] **Readability**: Ensure code is clear, well-structured, and easy to understand
- [ ] **DRY Principle**: Check for code duplication and suggest refactoring opportunities
- [ ] **SOLID Principles**: Verify adherence to Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion principles
- [ ] **Complexity**: Flag overly complex functions or methods that should be broken down
- [ ] **Comments & Documentation**: Ensure critical sections have adequate comments and documentation

### 2. Security Review
- [ ] **Secret Management**: Ensure no hardcoded secrets, API keys, or credentials in code
- [ ] **Input Validation**: Verify all user inputs are validated and sanitized
- [ ] **Authentication & Authorization**: Check proper access controls and permission validation
- [ ] **Dependency Security**: Review added dependencies for known vulnerabilities
- [ ] **SQL Injection**: If applicable, verify parameterized queries are used
- [ ] **CORS & Headers**: Validate security headers are properly configured
- [ ] **Environment Configuration**: Ensure sensitive data is stored in environment variables

### 3. Testing
- [ ] **Test Coverage**: Verify adequate unit tests are added/updated
- [ ] **Edge Cases**: Check for tests covering boundary conditions and error scenarios
- [ ] **Integration Tests**: Ensure integration tests are included where applicable
- [ ] **Test Quality**: Validate that tests are meaningful and not just for coverage
- [ ] **CI/CD**: Confirm all tests pass in the CI/CD pipeline

### 4. DevOps & Infrastructure
- [ ] **AWS Configuration**: Review AWS service configurations for security best practices
- [ ] **EC2 Setup**: Verify EC2 instance configurations are optimized and secure
- [ ] **Networking**: Check security groups, VPC configurations, and network access rules
- [ ] **Logging & Monitoring**: Ensure proper logging is implemented and monitored
- [ ] **Infrastructure as Code**: If using CloudFormation/Terraform, verify syntax and best practices
- [ ] **Cost Optimization**: Identify potential cost-saving opportunities

### 5. Performance
- [ ] **Algorithm Efficiency**: Check for inefficient algorithms (O(n²) loops, nested iterations)
- [ ] **Database Queries**: Review for N+1 problems and missing indexes
- [ ] **Caching**: Verify caching is implemented where appropriate
- [ ] **Resource Utilization**: Check for memory leaks or excessive resource consumption
- [ ] **Load Testing**: For backend changes, consider performance impact

### 6. Git & Version Control
- [ ] **Commit Messages**: Verify clear, descriptive commit messages following conventions
- [ ] **Commit History**: Check for logical, atomic commits (not too large or too small)
- [ ] **Branch Management**: Ensure branch is up-to-date with base branch
- [ ] **Merge Conflicts**: Identify and flag any merge conflicts

### 7. Documentation
- [ ] **README**: Update README.md if functionality has changed significantly
- [ ] **API Documentation**: Document new endpoints or API changes
- [ ] **CHANGELOG**: Verify CHANGELOG.md is updated with meaningful changes
- [ ] **Code Comments**: Ensure complex logic has explanatory comments
- [ ] **Configuration Docs**: Document any new configuration options

### 8. Workflow Files (GitHub Actions)
- [ ] **Syntax Validation**: Verify YAML syntax is correct
- [ ] **Secret Usage**: Ensure secrets are accessed correctly
- [ ] **Step Logic**: Review each step for correctness and efficiency
- [ ] **Error Handling**: Check for proper error handling and exit codes
- [ ] **Permissions**: Verify appropriate workflow permissions are set

### 9. Nginx Configuration (if applicable)
- [ ] **Server Config**: Review nginx server blocks for proper configuration
- [ ] **SSL/TLS**: If HTTPS is configured, verify certificate setup
- [ ] **Performance**: Check gzip, caching headers, and optimization settings
- [ ] **Security Headers**: Ensure security headers (CSP, X-Frame-Options, etc.) are present

## Review Guidelines

### When to Request Changes
- Security vulnerabilities or concerns
- Critical bugs or logical errors
- Major code quality issues affecting maintainability
- Missing or insufficient tests
- Performance concerns with significant impact
- Non-compliance with project standards

### When to Approve with Comments
- Minor style inconsistencies
- Suggestions for optimization (non-critical)
- Documentation improvements
- Best practice recommendations

### When to Approve
- Code follows standards and best practices
- Adequate test coverage
- No security concerns
- Clear and maintainable code
- Proper documentation

## Comment Format

Use the following format for review comments:

```
**Category**: [Code Quality | Security | Performance | Testing | Documentation | etc.]

**Issue**: Brief description of the issue

**Suggestion**: Recommended fix or improvement

**Resources**: Links to relevant documentation or best practices (if applicable)
```

## Approval Message Template

When approving, use this template:

```
✅ **Code Review Approved**

**Summary of Review:**
- Code quality: PASS
- Security check: PASS
- Test coverage: PASS
- Documentation: PASS

**Key Observations:**
- [Positive observations about the PR]

**Suggestions for Future:**
- [Optional improvements for next PRs]

Great work! This PR is ready to merge. 🎉
```

## Request Changes Message Template

When requesting changes, use:

```
⚠️ **Review Feedback - Changes Requested**

**Critical Issues (Must Fix):**
- [List critical issues]

**Minor Issues (Should Fix):**
- [List minor issues]

**Questions/Clarifications:**
- [List questions]

Once you address these points, the PR will be ready for approval.
```

## Special Considerations

### For DevOps Projects
- Verify infrastructure changes don't introduce security risks
- Confirm backward compatibility with existing deployments
- Check for proper rollback procedures
- Validate monitoring and alerting configurations

### For Workflow Files
- Ensure secrets are never logged or exposed
- Verify proper AWS IAM permissions are required
- Check timeout values are reasonable
- Validate artifact handling and cleanup

### For Nginx Configuration
- Verify performance optimizations are appropriate
- Check security headers are present
- Ensure SSL/TLS configuration is modern
- Validate logging configuration

## Review Timeline

- **Initial Review**: Start within 24 hours of PR creation
- **Follow-up**: Provide feedback within 24 hours of changes being pushed
- **Final Approval**: Once all feedback is addressed and tests pass

## Tools & Resources

- [AWS Best Practices](https://aws.amazon.com/architecture/best-practices/)
- [DevOps Best Practices](https://www.atlassian.com/devops)
- [Security Guidelines](https://owasp.org/www-project-cheat-sheets/)
- [Nginx Best Practices](https://www.nginx.com/blog/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## Questions?

If there are any unclear aspects of this guide or exceptions to these rules, please raise them in the PR discussion.
