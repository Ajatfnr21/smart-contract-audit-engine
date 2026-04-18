from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="smart_contract_audit_engine",
    version="0.1.0",
    author="Ajatfnr21",
    author_email="ajatfingerstyle21@gmail.com",
    description="AI-powered smart contract security audit engine with automated vulnerability detection and taint analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ajatfnr21/smart-contract-audit-engine",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.10",
    install_requires=[
        "web3>=6.0.0",
        "requests>=2.31.0",
        "pandas>=2.0.0",
    ],
)
