import requests

def test_injection(base_url):
    """
    Test for SQL Injection vulnerability by injecting common SQL payloads
    into query parameters and checking for database error responses.
    """
    test_payloads = ["' OR '1'='1", "'; DROP TABLE users; --", "' OR 1=1 --"]
    findings = []
    vulnerable_endpoint = f"{base_url}/search?query="

    for payload in test_payloads:
        url = vulnerable_endpoint + payload
        response = requests.get(url)
        if "sql syntax" in response.text.lower() or "mysql" in response.text.lower():
            findings.append(f"Possible SQL Injection detected with payload: {payload}")
    return findings
