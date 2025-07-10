
# OWASP Vulnerability Tester

This project is a Python-based security testing tool designed to evaluate web applications against the OWASP Top 10 vulnerabilities. Each module targets a specific vulnerability category and provides automated tests to identify potential issues.

## Features

- Modular architecture for easy testing
- Supports common web vulnerabilities
- Easy to expand with custom tests
- Command-line interface

## Requirements

- Python 3.8+
- `requests`
- `beautifulsoup4`

You can install dependencies using:

```bash
pip install -r requirements.txt
```

## Modules

Each Python module targets one of the OWASP Top 10 vulnerabilities.

### ✔️ Broken Access Control
Performs access control tests by trying to access unauthorized resources.

### ✔️ Injection
Detects injection flaws such as SQL, NoSQL, OS, and LDAP injections.

### ✔️ Security Misconfiguration
Tests for improper server or application configurations.

### ✔️ Identification and Authentication Failures
Looks for weak or broken authentication mechanisms.

### ✔️ Vulnerable and Outdated Components
Identifies outdated packages or technologies.

### ✔️ Software and Data Integrity Failures
Checks for unsigned or tampered client-side scripts or code.

### ✔️ Insecure Design
Looks for missing or insecure design elements that may cause vulnerabilities.

### ✔️ Remote Code Execution (RCE)
Attempts to inject and execute arbitrary code remotely.

### ✔️ Cross-Site Scripting (XSS)
Detects reflected and stored XSS vulnerabilities.

### ✔️ Server-Side Request Forgery (SSRF)
Tests endpoints to see if they fetch external resources insecurely.

## Usage

```bash
python main.py --url http://example.com
```

You can also run individual modules:

```bash
python modules/injection.py --url http://example.com
```

## Certificates

This project is backed by my training and certifications:

- **CompTIA Pentest+ Certificate**
- **Cyber Security 101 Certificate (TryHackMe)**
- **Cybersecurity Engineering Certificate (OAK Academy)**
- **Six Sigma Foundations** ([LinkedIn Certificate](https://www.linkedin.com/learning/certificates/5e8c79ab77ee4588850aeb7d1dfff5d51adb9953a7de17662b77ff41e9626932?trk=backfilled_certificate))

---

© 2025 Reşat Saygıcı | Security Researcher & Developer
