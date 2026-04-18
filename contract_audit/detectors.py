"""Vulnerability detectors for smart contracts."""

from typing import List, Dict

class VulnerabilityDetector:
    """Detect common smart contract vulnerabilities."""
    
    VULNERABILITIES = {
        'reentrancy': {
            'description': 'Reentrancy attack possible',
            'severity': 'critical',
            'patterns': ['call{value:', '.call(', 'external call before state change']
        },
        'integer_overflow': {
            'description': 'Integer overflow/underflow possible',
            'severity': 'high',
            'patterns': ['unchecked arithmetic', 'no SafeMath']
        },
        'access_control': {
            'description': 'Missing access control',
            'severity': 'critical',
            'patterns': ['no onlyOwner', 'public function modifying state']
        },
        'front_running': {
            'description': 'Transaction order dependence',
            'severity': 'medium',
            'patterns': ['use block.timestamp', 'miners can manipulate']
        }
    }
    
    def detect(self, contract_code: str) -> List[Dict]:
        """Detect vulnerabilities in contract code."""
        findings = []
        code_lower = contract_code.lower()
        
        for vuln_name, info in self.VULNERABILITIES.items():
            for pattern in info['patterns']:
                if pattern.lower() in code_lower:
                    findings.append({
                        'vulnerability': vuln_name,
                        'severity': info['severity'],
                        'description': info['description'],
                        'recommendation': f'Review and fix {vuln_name}'
                    })
                    break
        
        return findings
