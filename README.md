
# OWASP Top 10 Vulnerability Tester

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
Checks if protected pages can be accessed without credentials (e.g., /admin, /user/1234).
🧪 Example Outputs:

`$ python3 broken_access_control.py --url https://example.com`

`[+] Testing: https://example.com/admin`

`[!] Potential Broken Access Control detected: 200 OK`

### ✔️ Injection
Tests for SQL or command injection via input fields or query parameters.
🧪 Example Outputs:

`$ python3 injection.py --url https://example.com/search?q=test`

`[+] Testing parameter: q`

`[!] Possible SQL Injection point detected: payload "' OR 1=1 --" returned suspicious response.`

### ✔️ Security Misconfiguration
Tests for improper server or application configurations.
🧪 Example Outputs:

`$ python3 security_misconfiguration.py --url https://example.com`

`[!] Missing HTTP security headers:
    - X-Content-Type-Options
    - Content-Security-Policy`

`[!] Found exposed panel: https://example.com/server-status`

### ✔️ Identification and Authentication Failures
Looks for weak or broken authentication mechanisms.
🧪 Example Outputs:

`$ python3 authentication_failure.py --url https://example.com/login`

`[+] Trying default credentials: admin:admin`

`[!] Login successful – Possible weak authentication mechanism`

### ✔️ Vulnerable and Outdated Components
Identifies outdated packages or technologies.
🧪 Example Outputs:

`$ python3 vulnerable_components.py --url https://example.com`

`[!] Detected Apache version 2.2.22 – known vulnerabilities present.`

### ✔️ Software and Data Integrity Failures
Checks for unsigned or tampered client-side scripts or code.
🧪 Example Outputs:

`$ python3 software_data_integrity_failures.py --url https://example.com`

`[!] External script https://cdn.example.com/lib.js is missing 'integrity' attribute.`

### ✔️ Remote Code Execution (RCE)
Tests input fields for command injection vectors that might execute server-side code.
🧪 Example Outputs:
`$ python3 remote_code_execution.py --url https://example.com/ping?host=127.0.0.1`

`[!] Possible RCE vulnerability: payload '&& whoami' resulted in command output 'www-data'`

### ✔️ Cross-Site Scripting (XSS)
Detects reflected and stored XSS vulnerabilities.
🧪 Example Outputs:

`$ python3 cross_site_scripting.py --url https://example.com/search?q=test`

`[!] Reflected XSS found at parameter q with payload: <script>alert('XSS')</script>`

### ✔️ Server-Side Request Forgery (SSRF)
Tests endpoints to see if they fetch external resources insecurely.
🧪 Example Outputs:

`$ python3 server_side_request_forgery.py --url https://example.com/fetch?url=http://127.0.0.1:80`

`[!] Potential SSRF: Received response from internal IP 127.0.0.1`

### ✔️ Account Takeover (ATO)
Tests user flows for account hijacking vectors like insecure password resets.
🧪 Example Outputs:

`$ python3 account_takeover.py --url https://example.com/forgot-password`

`[!] Email enumeration possible – server reveals if user exists.`

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

- **CompTIA Security+ Certificate**
- **Cyber Security 101 Certificate (TryHackMe)**
- **Cybersecurity Engineering Certificate (OAK Academy)**
- **Six Sigma Foundations** ([LinkedIn Certificate](https://www.linkedin.com/learning/certificates/5e8c79ab77ee4588850aeb7d1dfff5d51adb9953a7de17662b77ff41e9626932?trk=backfilled_certificate))

---

© 2025 Reşat Saygıcı | Cybersecurity Enthusiast & Ethical Hacker
