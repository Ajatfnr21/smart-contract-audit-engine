#!/usr/bin/env python3
"""
Smart Contract Audit Engine - CLI
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from smart_contract_audit_engine.scanners.vulnerability_scanner import analyze_contract

def main():
    parser = argparse.ArgumentParser(
        description="AI-Powered Smart Contract Security Audit Engine"
    )
    parser.add_argument("contract", help="Path to Solidity contract file")
    parser.add_argument("--output", "-o", help="Output file for report (JSON)")
    parser.add_argument("--format", choices=["json", "console"], default="console",
                     help="Output format")
    
    args = parser.parse_args()
    
    if not Path(args.contract).exists():
        print(f"Error: Contract file not found: {args.contract}")
        sys.exit(1)
    
    print("Scanning contract for vulnerabilities...")
    report = analyze_contract(args.contract)
    
    if args.format == "json":
        output = json.dumps(report, indent=2)
        if args.output:
            with open(args.output, 'w') as f:
                f.write(output)
            print(f"Report saved to {args.output}")
        else:
            print(output)
    else:
        print("\n" + "=" * 70)
        print("AUDIT REPORT")
        print("=" * 70)
        print(f"Total Findings: {report['summary']['total_findings']}")
        print(f"  Critical: {report['summary']['critical']}")
        print(f"  High: {report['summary']['high']}")
        print(f"  Medium: {report['summary']['medium']}")
        print(f"  Low: {report['summary']['low']}")
        print(f"  Info: {report['summary']['info']}")
        print("=" * 70)
        
        for finding in report["findings"]:
            emoji = {"critical": "CRIT", "high": "HIGH", "medium": "MED", 
                    "low": "LOW", "info": "INFO"}.get(finding["severity"], "INFO")
            
            print(f"\n[{emoji}] {finding['title']}")
            print(f"   Line {finding['line']}: {finding['code']}")
            print(f"   {finding['description']}")
            print(f"   Fix: {finding['recommendation']}")

if __name__ == "__main__":
    main()
