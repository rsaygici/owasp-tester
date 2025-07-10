import requests

def test_ssrf(base_url):
    """
    Test for Server Side Request Forgery by trying to make the server fetch an external URL.
    """
    vulnerable_url = f"{base_url}/fetch?url=http://example.com"
    findings = []
    response = requests.get(vulnerable_url)
    
    if response.status_code == 200 and "Example Domain" in response.text:
        findings.append("Possible SSRF vulnerability detected.")
    return findings
