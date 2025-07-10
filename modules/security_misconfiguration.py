import requests

def test_security_misconfiguration(base_url):
    """
    Test for common security misconfigurations such as server headers
    exposing sensitive information.
    """
    findings = []
    response = requests.get(base_url)
    server_header = response.headers.get("Server", "")
    if server_header:
        findings.append(f"Server header exposed: {server_header}")
    if "X-Powered-By" in response.headers:
        findings.append(f"X-Powered-By header present: {response.headers['X-Powered-By']}")
    return findings
