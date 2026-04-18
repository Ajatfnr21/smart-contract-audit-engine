"""Generate audit reports."""

from datetime import datetime
from typing import List, Dict, Any
import json

class AuditReporter:
    """Generate security audit reports."""
    
    def generate(self, findings: List[Dict], contract_name: str) -> Dict[str, Any]:
        """Generate audit report."""
        severity_counts = {'critical': 0, 'high': 0, 'medium': 0, 'low': 0}
        for finding in findings:
            severity_counts[finding.get('severity', 'low')] += 1
        
        return {
            'contract': contract_name,
            'audit_date': datetime.now().isoformat(),
            'findings': findings,
            'summary': {
                'total': len(findings),
                **severity_counts
            },
            'score': max(0, 100 - severity_counts['critical']*25 - severity_counts['high']*15 - severity_counts['medium']*5)
        }
    
    def to_html(self, report: Dict) -> str:
        """Generate HTML report."""
        html = f"""<!DOCTYPE html>
<html><head><title>Audit: {report['contract']}</title></head>
<body>
<h1>Security Audit: {report['contract']}</h1>
<p>Date: {report['audit_date']}</p>
<p>Score: {report['summary']['score']}/100</p>
<h2>Findings ({report['summary']['total']})</h2>
<ul>
"""
        for f in report['findings']:
            html += f"<li><strong>{f['vulnerability']}</strong> ({f['severity']})<br>{f['description']}</li>"
        
        html += "</ul></body></html>"
        return html
    
    def to_json(self, report: Dict) -> str:
        """Generate JSON report."""
        return json.dumps(report, indent=2)
