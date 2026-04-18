# Smart Contract Audit Engine

AI-powered smart contract security audit engine with automated vulnerability detection.

## Features

- **Static analysis** - Detect reentrancy, overflow, access control issues
- **Pattern matching** - Identify dangerous code patterns
- **Multi-format reports** - JSON, HTML, PDF outputs
- **Severity scoring** - CVSS-based risk assessment

## Usage

```python
from contract_audit import ContractAnalyzer, VulnerabilityDetector, AuditReporter

analyzer = ContractAnalyzer()
info = analyzer.analyze("./MyContract.sol")

issues = analyzer.detect_issues("./MyContract.sol")

reporter = AuditReporter()
report = reporter.generate(issues, "MyContract")
```
