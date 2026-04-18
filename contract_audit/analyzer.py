"""Smart contract analyzer for Solidity and Vyper."""

import re
from pathlib import Path
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
import json

@dataclass
class ContractInfo:
    name: str
    type: str  # solidity, vyper
    functions: List[Dict]
    state_vars: List[Dict]
    modifiers: List[str]
    imports: List[str]

class ContractAnalyzer:
    """Analyze smart contracts for security issues."""
    
    def __init__(self):
        self.patterns = {
            'reentrancy': r'call\{value:.*\}(.*\n)*?[^/]*\b(balance|transfer)\b',
            'unchecked_send': r'\.send\(|\.transfer\([^)]*\)(?!\s*;)',
            'tx_origin': r'tx\.origin',
            'selfdestruct': r'selfdestruct\(|suicide\(',
            'unchecked_math': r'\+\+|--|\+= |-= |\*= |/= ',
        }
    
    def analyze(self, contract_path: str) -> ContractInfo:
        """Analyze a contract file."""
        path = Path(contract_path)
        content = path.read_text()
        
        contract_type = 'vyper' if path.suffix == '.vy' else 'solidity'
        
        # Parse basic info
        name_match = re.search(r'contract\s+(\w+)|class\s+(\w+)', content)
        name = name_match.group(1) or name_match.group(2) or "Unknown" if name_match else "Unknown"
        
        # Extract functions
        func_pattern = r'function\s+(\w+)\s*\([^)]*\)\s*(\w+)?\s*\{'
        functions = []
        for match in re.finditer(func_pattern, content):
            functions.append({
                'name': match.group(1),
                'visibility': match.group(2) or 'public'
            })
        
        return ContractInfo(
            name=name,
            type=contract_type,
            functions=functions,
            state_vars=[],
            modifiers=[],
            imports=[]
        )
    
    def detect_issues(self, contract_path: str) -> List[Dict]:
        """Detect security issues in contract."""
        content = Path(contract_path).read_text()
        issues = []
        
        for issue_type, pattern in self.patterns.items():
            for match in re.finditer(pattern, content, re.MULTILINE):
                issues.append({
                    'type': issue_type,
                    'line': content[:match.start()].count('\n') + 1,
                    'severity': 'high' if issue_type in ['reentrancy', 'tx_origin'] else 'medium',
                    'description': f'Potential {issue_type} vulnerability detected'
                })
        
        return issues
