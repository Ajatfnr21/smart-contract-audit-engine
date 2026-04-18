import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from smart_contract_audit_engine.scanners.vulnerability_scanner import (
    VulnerabilityScanner, Severity, analyze_contract
)

def test_reentrancy_detection():
    code = """
    function withdraw() public {
        (bool success, ) = msg.sender.call{value: amount}("");
        balances[msg.sender] = 0;
    }
    """
    scanner = VulnerabilityScanner()
    findings = scanner.scan(code)
    
    reentrancy = [f for f in findings if f.id == "reentrancy"]
    assert len(reentrancy) > 0

def test_tx_origin_detection():
    code = "require(tx.origin == owner);"
    scanner = VulnerabilityScanner()
    findings = scanner.scan(code)
    
    tx_origin = [f for f in findings if f.id == "tx_origin"]
    assert len(tx_origin) > 0
    assert tx_origin[0].severity == Severity.CRITICAL

def test_report_generation():
    code = "require(tx.origin == owner);"
    scanner = VulnerabilityScanner()
    findings = scanner.scan(code)
    report = scanner.generate_report(findings)
    
    assert "summary" in report
    assert "findings" in report
    assert report["summary"]["total_findings"] > 0
